01. Clock
Write a program that prints the hours of the day from 0:0 to 23:59, each on a separate line.
The hours should be written in the format "{hour}:{minutes}".
Input	        Output
(no entrance)	0:0
              0:1
              0:2
              0:3
              0:4
              0:5
              0:6
              0:7
              0:8
              0:9
              0:10
              ...
              23:50
              23:51
              23:52
              23:53
              23:54
              23:55
              23:56
              23:57
              23:58
              23:59
    
02. Multiplication Table
Print the multiplication table for the numbers 1 to 10 to the console in the format:
"{first factor} * {second factor} = {result}".
Sample Input and Output
Input Output
(no entrance)	1 * 1 = 1
              1 * 2 = 2
              1 * 3 = 3
              1 * 4 = 4
              1 * 5 = 5
              1 * 6 = 6
              1 * 7 = 7
              1 * 8 = 8
              1 * 9 = 9
              1 * 10 = 10
              ...
              10 * 1 = 10
              10 * 2 = 20
              10 * 3 = 30
              10 * 4 = 40
              10 * 5 = 50
              10 * 6 = 60
              10 * 7 = 70
              10 * 8 = 80
              10 * 9 = 90
              10 * 10 = 100

03. Combinations
Write a program that calculates how many solutions in natural numbers (including zero) the equation has:
x1 + x2 + x3 = n
The number n is an integer and is entered from the console.
Sample input and output
Input Output Explanations                                                 Input Output Input Output
25    351    We generate all combinations of 5 numbers, the first one is: 20    231    5     21
             0+0+0=0, but since it is not equal to 25, we continue:
             0+0+1=1 – also not 25, etc.
            We reach the first valid combination:
            0 + 0 + 25 = 25, we increase the number of valid
            combinations by 1,
            the second valid combination is:
            0 + 1 + 24 = 25
            The third:
            0 + 2 + 23 = 25, etc.
            After generating all possible combinations,
            the number of valid ones is 351.
    
04. Sum of two numbers
Write a program that checks all possible combinations of a pair of numbers in the range of two given numbers. At the output,
it is printed which is the combination whose sum of the numbers is equal to a given magic number.
If there is no combination that meets the condition, a message is printed that it was not found.
Entrance
The input is read from the console and consists of three lines:
• First line – beginning of the interval – integer in the range [1...999]
• Second row – end of interval – integer in the interval [greater than the first number... 1000]
• Third row – the magic number – an integer in the range [1...10000]
Exit
One line should be printed on the console, according to the result:
• If a combination is found whose sum of the numbers is equal to the magic number
o "Combination N:{sequence number} ({first number} + {second number} = {magic number})"
• If no matching combination is found
o "{the number of all combinations} combinations - neither equals {the magic number}"

Sample Input and Output
Input  Output           Explanations                                             
1      Combination N:4  All combinations of two numbers between 1 and 10 are:    
10     (1 + 4 = 5)      1 1, 1 2, 1 3, 1 4, 1 5, ... 2 1, 2 2, ... 4 9, 4 10,    
5                       5 1 ... 10 9, 10 10                                      
                        The first combination whose sum of the numbers is equal
                        to the magic number 5 is the fourth (1 and 4)

Input  Output
88     Combination N:20025 
888    (112 + 888 = 1000)
1000

Input	Output                Explanations
23    4 combinations        All combinations of two numbers between 23 and 24 are: 23 23,
24    - neither equals 20   23 24, 24 23, 24 24 (total 4)
20	                        There are no pairs of numbers whose sum equals the magic 20

Input Output
88    641601 combinations 
888   - neither equals 2000
2000	




