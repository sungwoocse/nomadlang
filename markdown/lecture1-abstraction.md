## Page 1

1.Computer Abstractions and Technology
Seongil  Wi
Department of Computer Science and EngineeringCSE261: Computer Architecture

## Page 2

The Post -PC Era2


## Page 3

The Post -PC Era
•Personal Mobile Device (PMD)
−Battery operated
−Connects to the Internet
−Smart phones, tablets, electronic glasses
•Embedded computers
−IoT (Internet of Things) and edge devices
−Hidden as components of systems
▪Car, TV, airplane, robot, drone, surveillance camera, satellite, etc.
−Stringent power/performance/cost constraints
•Cloud computing
−Amazon, Microsoft, and Google 
−Software as a Service (SaaS)
−Portion of software run on a PMD or embedded computer and a portion run in the Cloud3


## Page 4

Technology Trends
•Electronics technology continues to evolve
−Increased capacity4


## Page 5

Technology Trends
•Electronics technology continues to evolve
−Increased capacity
−Increased performance
−Reduced cost5
Year Technology Relative performance/cost
1951 Vacuum tube 1
1965 Transistor 35
1975 Integrated circuit (IC) 900
1995 Very large scale IC (VLSI) 2,400,000
2013 Ultra large scale IC 250,000,000,000

## Page 6

You will learn fundamental principles  
used in modern computer architectures 
to improve the performance of 
computations
What is the structure 
of a computer?

## Page 7

Computer Abstractions

## Page 8

Overview of the Computer8
Your 
programComputation
results Computer


## Page 9

Let’s Abstract the Computer 9
Your 
programComputation
results


## Page 10

Let’s Abstract the Computer 10
Abstraction layer #1:
Application softwareAbstraction layer #2:
System softwareAbstraction layer #3:
Hardware
Your 
programComputation
results

## Page 11

Wait, Why Abstraction?
1.Abstraction hides unnecessary details, making things easier to 
understand
2.Abstraction allows each developer to focus on their parts  of a 
problem
3.Abstraction allows us to build complex systems  by combining 
simple ideas (because abstracted ideas can be easily combined 
to form more complex ideas)11

## Page 12

Let’s Abstract the Computer 12
Abstraction layer #1:
Application softwareAbstraction layer #2:
System softwareAbstraction layer #3:
Hardware
Your 
programComputation
results

## Page 13

Let’s Abstract the Computer 13
Abstraction layer #1:
Application softwareAbstraction layer #2:
System softwareAbstraction layer #3:
Hardware
Your 
programComputation
results#include < stdio.h>
swap(int v[],  int k)
{
  int temp;
  temp = v[k];
  v[k] = v[k+1];
  v[k+1] = temp;
}
High-level language
010001010010
001101001001Compiler
Assembler
OS
Machine languageswap:
  multi $2, $5, 4
  add $2, $4, $2
  …
Assembly language

## Page 14

Let’s Abstract the Computer 14
Abstraction layer #1:
Application softwareAbstraction layer #2:
System softwareAbstraction layer #3:
Hardware
Your 
programComputation
results#include < stdio.h>
swap(int v[],  int k)
{
  int temp;
  temp = v[k];
  v[k] = v[k+1];
  v[k+1] = temp;
}
High-level language
010001010010
001101001001Compiler
Assembler
OS
Machine languageswap:
  multi $2, $5, 4
  add $2, $4, $2
  …
Assembly languageCompilation

## Page 15

Compilation
•Converting a high-level language  into a machine language  that 
the computer can understand15
int test ( int a){
    return 32;
}010001010100100101
010010001000001010
111000110101010100
101010000101010010
1110010101001 01110Compile
High-level 
language Machine 
language

## Page 16

Levels of Program Code16#include < stdio.h>
swap(int v[],  int k)
{
  int temp;
  temp = v[k];
  v[k] = v[k+1];
  v[k+1] = temp;
}
Compiler
swap:
  multi $2, $5, 4
  add $2, $4, $2
  …•High -level language
−Closer to problem domain
−Provides for productivity and 
portability 
•Assembly language
−The last human -readable format
−Textual representation of instructions

## Page 17

Levels of Program Code17#include < stdio.h>
swap(int v[],  int k)
{
  int temp;
  temp = v[k];
  v[k] = v[k+1];
  v[k+1] = temp;
}
Compiler
swap:
multi $2, $5, 4
  add $2, $4, $2
  …•High -level language
−Closer to problem domain
−Provides for productivity and 
portability 
•Assembly language
−The last human -readable format
−Textual representation of instructionsInstruction : a command 
that hardware understands

## Page 18

Levels of Program Code18#include < stdio.h>
swap(int v[],  int k)
{
  int temp;
  temp = v[k];
  v[k] = v[k+1];
  v[k+1] = temp;
}
Compiler
swap:
multi $2, $5, 4
  add $2, $4, $2
  …•High -level language
−Closer to problem domain
−Provides for productivity and 
portability 
•Assembly language
−The last human -readable format
−Textual representation of instructions
•Hardware representation
−Binary digits (bits)
−Encoded instructions and data
−1s and 0s (often displayed in “hex”)Instruction : a command 
that hardware understands
010001010010
001101001001Assembler

## Page 19

Levels of Program Code19#include < stdio.h>
swap(int v[],  int k)
{
  int temp;
  temp = v[k];
  v[k] = v[k+1];
  v[k+1] = temp;
}
Compiler
swap:
multi $2, $5, 4
  add $2, $4, $2
  …•High -level language
−Closer to problem domain
−Provides for productivity and 
portability 
•Assembly language
−The last human -readable format
−Textual representation of instructions
•Hardware representation
−Binary digits (bits)
−Encoded instructions and data
−1s and 0s (often displayed in “hex”)Instruction : a command 
that hardware understands
010001010010
001101001001AssemblerDirectly mapped
to each other

## Page 20

Let’s Abstract the Computer 20
Abstraction layer #1:
Application softwareAbstraction layer #2:
System softwareAbstraction layer #3:
Hardware
Your 
programComputation
results#include < stdio.h>
swap(int v[],  int k)
{
  int temp;
  temp = v[k];
  v[k] = v[k+1];
  v[k+1] = temp;
}
High-level language
010001010010
001101001001Compiler
Assembler
OS
Machine languageswap:
  multi $2, $5, 4
  add $2, $4, $2
  …
Assembly languageExecute the 
programCompilation

## Page 21

Hardware Components of a Computer21
Abstraction layer #1:
Application softwareAbstraction layer #2:
System softwareAbstraction layer #3:
Hardware
Your 
programComputation
results#include < stdio.h>
swap(int v[],  int k)
{
  int temp;
  temp = v[k];
  v[k] = v[k+1];
  v[k+1] = temp;
}
High-level language
010001010010
001101001001Compiler
Assembler
OS
Machine languageswap:
  multi $2, $5, 4
  add $2, $4, $2
  …
Assembly languageExecute the 
programCompilation

## Page 22

Hardware Components of a Computer22
Main memoryHard disk
I/O devices 
(e.g., mouse, monitor)Processor 
(CPU)
(e.g., Intel I7)

## Page 23

Hardware Components of a Computer23
Main memoryHard diskDisk
I/OProgram
fetch
+
Data
load/storePerform 
operationsSave the 
dataSave the 
data
Processor 
(CPU)
(e.g., Intel I7)
I/O devices 
(e.g., mouse, monitor)

## Page 24

A Safe Place for Data
•Volatile main memory
−Loses instructions and data when power off
−E.g., DRAM
•Non-volatile secondary memory
−HDD, SSD
−Magnetic disk
−Flash memory
−Optical disk (CDROM, DVD)24


## Page 25

Hardware Components of a Computer25
Main memoryHard disk Processor 
(CPU)
(e.g., Intel I7)01010010
00110110
Program A
11001110
01000110
Program B01101101
11010111
Program C

## Page 26

Hardware Components of a Computer26
Main memoryHard disk
 Processor 
(CPU)
(e.g., Intel I7)Control
(brain)
Datapath01010010
00110110
Program A
11001110
01000110
Program B01101101
11010111
Program C

## Page 27

Hardware Components of a Computer27
Main memoryHard disk
 Processor 
(CPU)
(e.g., Intel I7)01010010
00110110
Program A
11001110
01000110
Program B01101101
11010111
Program C
Control
(brain)
DatapathTell what to do

## Page 28

Hardware Components of a Computer28
Main memoryHard disk
 Processor 
(CPU)
(e.g., Intel I7)Control
(brain)
Datapath01010010
00110110
Program A
11001110
01000110
Program B01101101
11010111
Program CTell what to do
Perform 
operations on data

## Page 29

Let’s Execute the Program!29
Main memoryHard disk
 Processor 
(CPU)
(e.g., Intel I7)Control
(brain)
Datapath01010010
00110110
Program A
11001110
01000110
Program B01101101
11010111
Program C

## Page 30

Let’s Execute the Program!30
Main memoryHard disk
 Processor 
(CPU)
(e.g., Intel I7)Control
(brain)
Datapath01010010
00110110
Program A
11001110
01000110
Program B01101101
11010111
Program C1. Load the 
Program A
Program AExecute program A
($ ./programA )
01010010
00110110

## Page 31

Let’s Execute the Program!31
Main memoryHard disk
 Processor 
(CPU)
(e.g., Intel I7)Control
(brain)
Datapath01010010
00110110
Program A
11001110
01000110
Program B01101101
11010111
Program C1. Load the 
Program A
2. Fetch the 
instruction
(One -by-one)01010010
Program AExecute program A
($ ./programA )
01010010
00110110

## Page 32

Let’s Execute the Program!32
Data A
Main memoryHard disk
 Processor 
(CPU)
(e.g., Intel I7)Control
(brain)
Datapath01010010
00110110
Program A
11001110
01000110
Program B01101101
11010111
Program C1. Load the 
Program A
010100103. Execute the 
instructionLoad/Store
the Data
2. Fetch the 
instruction
(One -by-one)Program AExecute program A
($ ./programA )
01010010
00110110

## Page 33

Inside the Processor (CPU)
•Datapath
−Perform operations on data
•Control
−Tell the datapath , memory, and I/O devices what to do 
according to program
•Registers/cache memory (=> next lecture)
−Small fast memory for immediate access to data33

## Page 34

Apple A12 Processor34


## Page 35

35
Abstraction layer #1:
Application softwareAbstraction layer #2:
System softwareAbstraction layer #3:
Hardware
Your 
programComputation
results#include < stdio.h>
swap(int v[],  int k)
{
  int temp;
  temp = v[k];
  v[k] = v[k+1];
  v[k+1] = temp;
}
High-level language
010001010010
001101001001Compiler
Assembler
OS
Machine languageswap:
  multi $2, $5, 4
  add $2, $4, $2
  …
Assembly languageAbstraction Helps us Deal with Complexity

## Page 36

High-level language36
Your 
programComputation
results
010001010010
001101001001Compiler
Assembler
OS
Machine languageswap:
  multi $2, $5, 4
  add $2, $4, $2
  …
Assembly language#include < stdio.h>
swap(int v[],  int k)
{
  int temp;
  temp = v[k];
  v[k] = v[k+1];
  v[k+1] = temp;
}Abstraction layer #1:
Application softwareAbstraction layer #2:
System softwareAbstraction layer #3:
Hardware
Application 
developerC language
specification
InterfaceAbstraction Helps us Deal with Complexity
Detailed knowledge of 
OS/HW is not necessary

## Page 37

High-level language37
Your 
programComputation
results
010001010010
001101001001Compiler
Assembler
OS
Machine languageswap:
  multi $2, $5, 4
  add $2, $4, $2
  …
Assembly language#include < stdio.h>
swap(int v[],  int k)
{
  int temp;
  temp = v[k];
  v[k] = v[k+1];
  v[k+1] = temp;
}Abstraction layer #1:
Application softwareAbstraction layer #2:
System softwareAbstraction layer #3:
Hardware
Application 
developerC language
specification
InterfaceAbstraction Helps us Deal with Complexity
Detailed knowledge of 
OS/hardware is not necessaryHide lower -level implementation details
while providing an interface

## Page 38

Your 
program
010001010010
001101001001Compiler
Assembler
OS
Machine languageswap:
  multi $2, $5, 4
  add $2, $4, $2
  …
Assembly language#include < stdio.h>
swap(int v[],  int k)
{
  int temp;
  temp = v[k];
  v[k] = v[k+1];
  v[k+1] = temp;
}
High-level language38
Computation
results
Abstraction layer #1:
Application softwareAbstraction layer #2:
System softwareAbstraction layer #3:
Hardware
Instruction Set 
Architecture
Interface
Program/System/OS/Compiler
developerDetailed knowledge of 
HW is not necessarySimilarly, We Can Consider the Hardware/Software Interface

## Page 39

Instruction Set Architecture (ISA)
•The interface between hardware and low -level software
•Hardware abstraction visible to software (compiler or programmer)
−Instruction set
−Operand types
−Data types (integers, FPs, ...)
−Memory addressing modes
−...
Image from: D. Culler @ UC Berkeley39
software
hardwareInstruction Set Architecture

## Page 40

Now, you can understand the 
meaning of the subtitle in the 
textbook ☺

## Page 41

Instruction Set Architecture (ISA)41
Image from: https:// medium.com /@shb8086/tutorial -series -isa-fa9648c5e9e5

## Page 42

•Use abstraction  to simplify design
•Make the common case fast
•Performance via parallelism
•Performance via pipelining
•Performance via prediction
•Hierarchy  of memories
•Dependability  via redundancy42Seven Great Ideas in Computer Architecture
You do not need to memorize.
We will cover each topic!

## Page 43

You will learn fundamental principles  
used in modern computer architectures 
to improve the performance of 
computations
What is the structure 
of a computer?How we calculate the 
performance?break

## Page 44

Performance

## Page 45

Defining Performance
•Which airplane has the best performance?45
It depends on the metrics!

## Page 46

We Focus on the Time
•Most important thing: time, time, and time46

## Page 47

Metrics: CPU Time
•Most important thing: time, time, and time47
CPU Time =Instructions
Program×Clock cycles
Instruction ×Seconds
Clock cycle

## Page 48

Metrics: CPU Time
•Most important thing: time, time, and time48
CPU Time =Instructions
Program×Clock cycles
Instruction ×Seconds
Clock cycle
Our goal!

## Page 49

•Most important thing: time, time, and time49
CPU Time =Instructions
Program×Clock cycles
Instruction ×Seconds
Clock cycle
swap:
  multi $2, $5, 4
  add $2, $4, $2
  …# of instructions 
per program# of Instructions per Program (Instruction Count)
Affected by:
•Compiler
•Algorithm
•Programming language
•ISA

## Page 50

Clock Cycles per Instruction (CPI)
•Most important thing: time, time, and time50
CPU Time =Instructions
Program×Clock cycles
Instruction ×Seconds
Clock cycle
swap:
  multi $2, $5, 4
  add $2, $4, $2
  …

## Page 51

Clock Cycles per Instruction (CPI)
•Most important thing: time, time, and time51
CPU Time =Instructions
Program×Clock cycles
Instruction ×Seconds
Clock cycle
swap:
  multi $2, $5, 4
  add $2, $4, $2
  …CPU clocking: 
Operation of digital hardware 
governed by a constant -rate clock


## Page 52

Clock Cycles per Instruction (CPI)
•Most important thing: time, time, and time52
CPU Time =Instructions
Program×Clock cycles
Instruction ×Seconds
Clock cycle
1st 
Clock Cycle2nd 
Clock Cycle3rd  
Clock Cycle …swap:
  multi $2, $5, 4
  add $2, $4, $2
  …

## Page 53

Clock Cycles per Instruction (CPI)
•Most important thing: time, time, and time53
CPU Time =Instructions
Program×Clock cycles
Instruction ×Seconds
Clock cycle
1st 
Clock Cycle2nd 
Clock Cycle3rd  
Clock Cycle …swap:
multi $2, $5, 4
  add $2, $4, $2
  …CPI = 2Average CPI

## Page 54

Clock Cycle Period (Clock Cycle Time))
•Most important thing: time, time, and time54
CPU Time =Instructions
Program×Clock cycles
Instruction ×Seconds
Clock cycle
1st 
Clock Cycle2nd 
Clock Cycle3rd  
Clock Cycle …Clock Cycle Period:
e..g, 250 ps

## Page 55

FYI: CPU Frequency (Clock Rate)55
CPU Frequency (Hz) =1
Clock Cycle Period
Number of cycles per one second


## Page 56

Metrics: CPU Time
•Most important thing: time, time, and time56
CPU Time =Instructions
Program×Clock cycles
Instruction ×Seconds
Clock cycle
Affected by:
•ISA
•Hardware implementation

## Page 57

Metrics: CPU Time
•Most important thing: time, time, and time57
Let's skip the details for now.
We'll cover them properly later.CPU Time =Instructions
Program×Clock cycles
Instruction ×Seconds
Clock cycle

## Page 58

Power Trends

## Page 59

Power Trends59
Power  = Capacitive  load × Voltage2× CPU Frequency

## Page 60

Power Trends60
Power  = Capacitive  load × Voltage2× CPU FrequencyFrequency (Hz)↑ 
⇒CPU Time ↓ 
1GHz
1000GHzWith the advancement of 
technology, the frequency can 
continue to increase

## Page 61

However, …61
Power  = Capacitive  load × Voltage2× CPU FrequencyFrequency (Hz)↑ 
⇒CPU Time↓ 
Power↑ ⇒
Heat ↑ 1GHz
1000GHz X1000 Power

## Page 62

However, There is the Power Wall62
Power  = Capacitive  load × Voltage2× CPU FrequencyFrequency (Hz)↑ 
⇒CPU Time↓ 
1GHz
1000GHz X1000 Power
Power↑ ⇒
Heat ↑ 

## Page 63

How about Reducing Voltage?63
Power  = Capacitive  load × Voltage2× CPU FrequencyFrequency (Hz)↑ 
⇒CPU Time↓ 
1GHz
1000GHz X40 Power5V
1V

## Page 64

How about Reducing Voltage?64
Power  = Capacitive  load × Voltage2× CPU FrequencyFrequency (Hz)↑ 
⇒CPU Time↓ 
1GHz
1000GHz X40 Power5V
1VHowever, we can’t reduce voltage 
further due to leakage power

## Page 65

Example
•Suppose a new simpler CPU has
−85% of capacitive load of old CPU
−15% voltage and 15% frequency reduction
•Q. What is the impact on power?65
0.52 0.85
F V C0.85 F 0.85) (V 0.85 C
PP4
old2
old oldold2
old old
oldnew==
=

## Page 66

Example
•Suppose a new simpler CPU has
−85% of capacitive load of old CPU
−15% voltage and 15% frequency reduction
•Q. What is the impact on power?66
0.52 0.85
F V C0.85 F 0.85) (V 0.85 C
PP4
old2
old oldold2
old old
oldnew==
=
The new processor uses about
half the power of the old processor 

## Page 67

The Power Wall 
•We can’t reduce voltage further due to leakage power
•We can’t remove more heat due to costs and complexities67
Flattened or 
dropped off recently 

## Page 68

Uniprocessor Performance68
25% per 
year

## Page 69

Uniprocessor Performance69
Constrained by power
(and long memory latency)  

## Page 70

How we address the power wall?
 ⇒ Multiprocessors!

## Page 71

Uniprocessor to Multiprocessors71
Uniprocessor : one 
processor (core) per chip

## Page 72

Uniprocessor to Multiprocessors72


## Page 73

Uniprocessor to Multiprocessors73
#1 #2
#3 #4


## Page 74

Uniprocessor to Multiprocessors74
#1 #2
#3 #4
Multiprocessors : more than 
one processor (core) per chip

## Page 75

Multiprocessors
•Multicore microprocessors
−More than one processor (core) per chip
•Requires explicitly parallel programming
−Programming for performance
−Load balancing
−Optimizing communication and synchronization75
Application 
developerCore #1 Core #2
Core #3 Core #4
import multiprocessing
multiprocessing.pool (processes=4)
...

## Page 76

•GPGPU (General Purpose GPU)
−Suited to embarrassingly parallel problems
−Matrix and vector computation
•Special purpose HW
−Google’s TPU (Tensor Processing Unit)
−Microsoft’s Brainwave 76Recent Evolution of Computer Architecture
Google’s TPU and its datacenter MS Project Brainwave


## Page 77

Conclusion

## Page 78

•Understand general principles (NOT about learning coding skills )
•How programs are translated into the machine language
−And how the hardware executes them!
•Instruction Set Architecture
•Below of the Instruction Set Architecture
•What determines program performance
−And how it can be improved78What will You Learn in This Course?

## Page 79

Why Learn this Stuff?
•You want to call yourself a “computer scientist”79


## Page 80

Why Learn this Stuff?
•You want to call yourself a “computer scientist”
•You want to build software that people use ( requires  performance)
•You need to make a purchasing decision or offer “expert” advice80

## Page 81

Summary
•Abstraction is fundamental to understanding computer systems
−In both hardware and software
•ISA is an interface between SW and HW
•Performance metric: CPU Time
•Power is a limiting factor
−Use parallelism to improve performance81
CPU Time =Instructions
Program×Clock cycles
Instruction ×Seconds
Clock cycle

## Page 82

Question?

