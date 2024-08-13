import streamlit as st
from langchain_community.document_loaders import SeleniumURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

# .env 파일에서 환경 변수 로드
load_dotenv()

# Streamlit 페이지 설정
st.set_page_config(
    page_title="SiteGPT",
    page_icon="🖥️",
)

st.markdown(
    """
    # SiteGPT
            
    Ask questions about the content of a website.
            
    Start by writing the URL of the website on the sidebar.
"""
)

# 사이드바에 URL 입력 필드 추가
with st.sidebar:
    url = st.text_input(
        "Write down a URL",
        placeholder="https://example.com",
    )

# URL이 입력되었을 때 실행
if url:
    # 로딩 표시
    with st.spinner("Loading and processing the webpage..."):
        # SeleniumURLLoader를 사용하여 웹 페이지 로드
        loader = SeleniumURLLoader(urls=[url])
        data = loader.load()
        
        # 텍스트 분할
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
        texts = text_splitter.split_documents(data)
        
        # 임베딩 및 벡터 저장소 생성
        embeddings = OpenAIEmbeddings()
        docsearch = FAISS.from_documents(texts, embeddings)
        
        # QA 체인 로드
        chain = load_qa_chain(OpenAI(), chain_type="stuff")
        
    st.success("Webpage processed successfully!")

    # 사용자 질문 입력
    query = st.text_input("Ask a question about the webpage:")

    if query:
        # 로딩 표시
        with st.spinner("Searching for an answer..."):
            # 관련 문서 검색
            docs = docsearch.similarity_search(query)
            
            # QA 체인을 사용하여 답변 생성
            answer = chain.run(input_documents=docs, question=query)
        
        # 답변 표시
        st.write("Answer:", answer)

else:
    st.info("Please enter a URL to start.")