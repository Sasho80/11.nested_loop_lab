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

05. Travel
Annie loves to travel and wants to visit several different destinations this year.
Once she has chosen a destination, she will estimate how much money she will need to go there and start saving.
When she has saved enough, she will be able to travel.
The console will first read the destination and the minimum budget (decimal number) that will be needed for the trip.
Then, several amounts (decimal numbers) that Annie saves by working will be read and when she manages to save enough for the trip,
she will leave, and the console should display: "Going to {destination}!"
When she has visited all the destinations she wants, she will enter "End" instead of destination and the program will end.

Sample input and output
Input      Output                    
Greece    Going to Greece!                        
1000.00   Going to Spain!                         
200.00                                          
200.00
300.00
100.00
150.00
240.00
Spain
1200.00
300.00
500.00
193.00
423.00
End

Input         Output 
France        Going to France!
2000.00       Going to Portugal!
300.00        Going to Egypt!
300.00
200.00
400.00
190.00
258.00
360.00
Portugal
1450.00
400.00
400.00
200.00
300.00
300.00
Egypt
1900.00
1000.00
280.00
300.00
500.00
End

06. Building
Write a program that prints the room numbers in a building (in descending order) to the console, provided that the following conditions are met:
• There are only offices on each even floor;
• There are only apartments on each odd floor;
• Each apartment is designated as follows: A{floor number}{apartment number}, apartment numbers start at 0;
• Each office is designated as follows: O{floor number}{office number}, office numbers also start at 0;
• There are always apartments on the top floor and they are larger than the others, so their numbers are preceded by 'L' instead of 'A'.
 If there is only one floor, then there are only large apartments!
Two integers are read from the console - the number of floors and the number of rooms per floor.

Sample input and output
Input	Output            Explanations
6     L60 L61 L62 L63   We have a total of 6 floors, with 4 rooms per floor. 
4	    A50 A51 A52 A53   The odd-numbered floors have only apartments, 
      O40 O41 O42 O43   and the even-numbered floors have only offices.
      A30 A31 A32 A33
      O20 O21 O22 O23
      A10 A11 A12 A13

Input	Output
9     L90 L91 L92 L93 L94
5	    O80 O81 O82 O83 O84
      A70 A71 A72 A73 A74
      O60 O61 O62 O63 O64
      A50 A51 A52 A53 A54
      O40 O41 O42 O43 O44
      A30 A31 A32 A33 A34
      O20 O21 O22 O23 O24
      A10 A11 A12 A13 A14

Input	Output
4     L40 L41 L42 L43
4	    A30 A31 A32 A33
      O20 O21 O22 O23
      A10 A11 A12 A13


