# Efficiency manager for LAHSA and SPLA shelters 

Goal: This project aims to provide an approach to efficient resource allocation that must divide between entities with different constraints. On considering the entities as two competing agents, the each entity assures to maximize it's efficient by picking suitable applicants. 

Analogy from Aritificial Intelligence:
The situation is practical use of gaming agents. Gaming agents like Chess playing agents tend to make the right most move considering steps ahead of time to yield maximum scores. An agent during its turn makes a move that maximizes its score, the opponent makes a move that minimizes the score of the agent to the best extent. This is the basis of the popular AI Minmax algorithm that uses alpha-beta pruning in huge search spaces. 

The competing agents here are LAHSA and SPLA that are described further below. 

Los Angeles Homeless Service Authority(LAHSA) and Safe Parking LA(SPLA) are two organization in Los Angeles that service the homeless community. LAHSA provides beds in shelters and SPLA manages spaces in parking lots for people living in their cars. Here, Both LAHSA and SPLA choose their respective applicants. However this system require an optimized use of the parking lot fora given partiulcar week. 

Application information:
Applicant ID: 5 
digitsGender: M/F/O
Age: 0-100Pets: Y/N
Medical conditions: Y/N
Car: Y/N
Driver’s License: Y/N
Days of the week needed: 0/1 for each day of the 7 days of the week (Monday-Sunday) 

Example applicant record: 00001F020NNYY1001000 for applicant id 00001, female, 20 years old, no pets, no medical conditions, with car and driver’s license, who needs housing for Monday and Thursday.

# Allotment constraints: 
SPLA and LAHSAalternate choosing applicants one by one.  They must choose an  applicant  if there is still a  qualified  oneon the list(no  passing).SPLA applicants must have a car and driver’s license, but no medical conditions.  LAHSA shelter can only serve women over 17 years old without pets. Both SPLA and LAHSA have limited resources that must be used efficiently.  Efficiency is calculated by how many of the spaces are used during the week.  For example, a SPLA parking lot has 10 spacesand can have at most 10*7 days = 70 different applicants for the week. SPLA tries to maximize its efficiency rate.

# Input: 
The file input.txt in the current directory of your program will be formatted as follows: 
First line: strictly positive 32-bit integer b, number of beds in the shelter, b<= 40.
Second line: strictly positive 32-bit integer p, the number of spaces in the parking lot
Third line: strictly positive 32-bit integer L, number of applicants chosen by LAHSA so far. 
Next Llines: Lnumber of Applicant ID (5 digits) , separated with the End-of-line character LF. 
Next line:strictly positive 32-bit integer S, number of applicants chosen by SPLA so far.
Next Slines: Snumber of Applicant ID (5 digits), separated with the End-of-line character LF.  
Next line: strictly positive 32-bit integer A, totalnumber of applicants
Next Alines: the list of Aapplicant information, separated with the End-of-line character LF.  

# Output: 
Next applicant chosen by SPLA:Applicant ID (5 digits)


