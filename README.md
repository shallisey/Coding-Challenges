# Coding-Challenges

This is just where I will put some challenges that I am working through to see where I stand on solving problems.

## Advent of Code

This is something I am working on during my winter 2020 term break at Oregon State University.
At this point I have only completed 2 classes. CS-225 Discrete Structures in CS and CS-161 Intro to Computer Science I.

I am going to use this as a place to write down somethings I learned and maybe some challenges I faced. 

  #### Day 1
  On this first day I learned quite a bit of new things.  
  - How to open a txt file with python.  
  - I learned how to import different libraries.  
  - I gained a better understanding of how recursion works. 
    - I needed to find 2 numbers from a list that when added together would equal 2020.  
    - What I did was take the 0th index of the list and add that with every index other index in the list.  
    - If 2 of the numbers sum equals 2020 then the code returned those two numbers.  
    - If it did not find a sum of 2020, then I popped the 0th index and started the process over again until a sum of 202 was found.  
  Part 2 I needed to find combinations of 3 numbers that sum equals 2020.  
  - This is where I found inporting different libraries helpful. 
  - I used combinations from the itertools library.
    - It helped taking CS-225 because one of the modules was directly related to combinations and permutations.
  - The combinations function creates tuples of some length that you input, I needed tuples of length 3, from a list.
  ```
  lst_combo = combinations(lst, 3)
  ```
      
  
  #### Day 2
  - Here I learned that if you use .split() you can store what is split in variables.
  ```
  low, high = words[0].split('-')
  ```
  - For example lets say that words[0] = 1-4.
  - We call words[0].split('-') and store the number 1 in the low varaible, and 4 in the high variable.
  - Now these are stores as strings and not variables so later in the program I convert them to integers.
  ```
  if int(low) <= letter_count <= int(high):
  ```
    
    
  #### Day 3
  - The inputs were strings so, when I looped through the file and made a copy as a list.
  ```
  for i in extender_list:
        s = list(i)
  ```
  - I did this because I needed to update where spaces and trees where if I were to "land" on them.
  - You cannot alter strings from a loop because they are immutable. That is why I had to make copies as lists.
  - For this reason as well I needed to create a new list just so I could have an output that would correctly output the changes I made to the copy.
