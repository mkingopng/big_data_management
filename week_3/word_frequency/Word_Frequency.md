# Word frequency
Let's now get some hands-on experience of MapReduce using Hadoop streaming.

Suppose that you want to know **the words in a text file and how frequently each word occurs**.

You could write a Python program to calculate the frequencies for you.

When you click the panel on the right you will get a terminal connection to a server. There is Python program called 
"frequency.py" on this server - it reads a file from standard input and prints the frequency of each word in the file 
to standard output. Read through the program to make sure you understand it.

There is also a sample text file called "text.txt". You can open the file to inspect its contents.

To run frequency.py with text.txt as input, enter the following into the terminal:

```$ python frequency.py < word_frequency_text.txt```

This command tells Python to run the program "frequency.py", and use "text.txt" as the input to the program (that's 
what the < is doing).

You should see the words in the file, and the frequency of each word.

So far this just an ordinary Python program working with an ordinary file in the server's local file system. But what 
if the file is stored in a Hadoop cluster? Then you'll need to use a different technique. In the next two slides we'll 
see how to do it using MapReduce.