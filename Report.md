# Nestor Escobedo Map Reduce Report

# To run the program
To run the program type into the shell

"python3 mapReduce.py"

# Problems encountered
In this lab I had the most issues figuring out how to divide the program
into parts to solve the problem so I read the file word into list and then used those list to 
perform the map reduce section. I also had issues to implement the lock functions in the program because
I did not have a good understanding on how they worked.

This lab took me around 5 hours to complete

# Performance 
1 thread = 17.541603915997257

2 threads = 17.20288541100308

4 threads = 22.631207314996573

8 threads = 14.714834195001458

# Analysis
It is hard for me to analyze the performance of this algorithm,
because it seems that there is no relation between the number of threads and the
time it takes for the program to run.
I believe that the overhead with the 4 threads is the most and it causes some processes to wait for other processes
so the program can keep running.

model name : 11th Gen Intel(R) Core(TM) i7-1165G7 @ 2.80GHz 4 40 240

