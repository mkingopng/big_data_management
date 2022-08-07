# Try it: top-k most frequent pairs
In this challenge, you will practice how to pass a long function to Spark. 

The task is that, given a text file, find out the top-k most frequent co-occurring term pairs. The co-occurrence 
of (w, u) is defined as: u and w appear in the same line (this means that (w, u) and (u, w) are treated as the 
same pair, and the first term has a lower alphabetical order). Your Spark program should generate a list of k 
key-value pairs ranked in descending order according to their frequencies, where the keys are the pair of terms 
(in format of (w, u)) and the values are the co-occurring frequencies. If two pairs have the same frequency, 
sort them by the first term and then by the second term alphabetically. 

Your program should read "text.txt" as the input, and store the result in the directory "output" in your home 
folder. The parameter k is received from the command line. The code template has been provided, and please fill 
your code to complete this task.

Assume that k=5, you can run your program by `spark-submit topk_pair.py 5`, and the result is like:

```
('the,to', 61)
('not,the', 50)
('the,the', 45)
('can,the', 40)
('for,the', 40)
```

