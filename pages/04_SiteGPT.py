from langchain_community.document_loaders import SitemapLoader
from langchain.schema.runnable import RunnableLambda, RunnablePassthrough
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import streamlit as st

# Set page config first
st.set_page_config(
    page_title="SiteGPT",
    page_icon="🖥️",
)

# Display the title and description
st.markdown(
    """
    # SiteGPT
            
    Ask questions about the content of a website.
            
    Start by writing the URL of the website on the sidebar.
"""
)

# Get the URL input in the sidebar
with st.sidebar:
    url = st.text_input(
        "Write down a URL",
        placeholder="https://example.com",
    )

# Initialize ChatOpenAI
llm = ChatOpenAI(
    temperature=0.1,
)

# Define the answers prompt
answers_prompt = ChatPromptTemplate.from_template(
    """
    Using ONLY the following context answer the user's question. If you can't just say you don't know, don't make anything up.
                                                  
    Then, give a score to the answer between 0 and 5.

    If the answer answers the user question the score should be high, else it should be low.

    Make sure to always include the answer's score even if it's 0.

    Context: {context}
                                                  
    Examples:
                                                  
    Question: How far away is the moon?
    Answer: The moon is 384,400 km away.
    Score: 5
                                                  
    Question: How far away is the sun?
    Answer: I don't know
    Score: 0
                                                  
    Your turn!

    Question: {question}
"""
)

# Define the get_answers function
def get_answers(inputs):
    docs = inputs["docs"]
    question = inputs["question"]
    answers_chain = answers_prompt | llm
    return {
        "question": question,
        "answers": [
            {
                "answer": answers_chain.invoke(
                    {"question": question, "context": doc.page_content}
                ).content,
                "source": doc.metadata["source"],
                "date": doc.metadata["lastmod"],
            }
            for doc in docs
        ],
    }

# Define the choose prompt
choose_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            Use ONLY the following pre-existing answers to answer the user's question.

            Use the answers that have the highest score (more helpful) and favor the most recent ones.

            Cite sources and return the sources of the answers as they are, do not change them.

            Answers: {answers}
            """,
        ),
        ("human", "{question}"),
    ]
)

# Define the choose_answer function
def choose_answer(inputs):
    answers = inputs["answers"]
    question = inputs["question"]
    choose_chain = choose_prompt | llm
    condensed = "\n\n".join(
        f"{answer['answer']}\nSource:{answer['source']}\nDate:{answer['date']}\n"
        for answer in answers
    )
    return choose_chain.invoke(
        {
            "question": question,
            "answers": condensed,
        }
    )

# Define the parse_page function
def parse_page(soup):
    header = soup.find("header")
    footer = soup.find("footer")
    if header:
        header.decompose()
    if footer:
        footer.decompose()
    return (
        str(soup.get_text())
        .replace("\n", " ")
        .replace("\xa0", " ")
        .replace("CloseSearch Submit Blog", "")
    )

# Define the load_website function
@st.cache_data(show_spinner="Loading website...")
def load_website(url):
    try:
        splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
            chunk_size=1000,
            chunk_overlap=200,
        )
        loader = SitemapLoader(
            url,
            parsing_function=parse_page,
        )
        loader.requests_per_second = 2
        docs = loader.load_and_split(text_splitter=splitter)
        
        if not docs:
            st.warning("No documents were loaded from the website. The sitemap might be empty or inaccessible.")
            return None
        
        vector_store = FAISS.from_documents(docs, OpenAIEmbeddings())
        return vector_store.as_retriever()
    except Exception as e:
        st.error(f"An error occurred while loading the website: {str(e)}")
        return None

# Main logic
if url:
    if ".xml" not in url:
        with st.sidebar:
            st.error("Please write down a Sitemap URL.")
    else:
        retriever = load_website(url)
        if retriever is not None:
            query = st.text_input("Ask a question to the website.")
            if query:
                chain = (
                    {
                        "docs": retriever,
                        "question": RunnablePassthrough(),
                    }
                    | RunnableLambda(get_answers)
                    | RunnablePassthrough()
                    | RunnableLambda(choose_answer)
                )
                result = chain.invoke(query)
                st.markdown(result.content.replace("$", "\$"))
        else:
            st.error("Failed to load the website. Please try a different URL or check your internet connection.")