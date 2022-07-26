# Word frequency (Local)
Now let's see an example in action.

Consider again the task of counting the frequency of words in a file. When you click the panel on the right you'll get 
a connection to a server that has a Python program called "job.py" in your home directory. This program uses MRJob to 
find the frequency of words in a file. 

Here is a walk-through of the program:

- First, we import the MRJob class from the ```mrjob.job``` module.

- Next, we define a class that inherits from the MRJob class. Here we have called it 'Job', but you can call it 
whatever you like. We define this class by defining a mapper method and a reducer method.

The ```mapper``` method takes a key and a value as arguments, and yields as many key-value pairs as we like. In this 
case, we ignore the key; the value is a single line of text, and for each word in the line we yield the pair 
```word, 1```.

The ```reducer``` method takes a key and a collection of values, and also yields as many key-value pairs as we like. In this 
case, the key is a word and the values are the frequencies of that word returned by the mappers; we yield the word and 
the sum of those frequencies, which is the total frequency of the word.

Finally, we add the last two lines. These lines pass control over to the command line arguments and execution to mrjob. 
You must include them every time - without them your job will not work.

## Running the job
On the server, there is also the file "text.txt", which contains some text (you can open the file to look at it). To 
count the frequency of words in this file, enter the following command into the terminal:

```$ python job.py text.txt```

You should see the results appear in the terminal.

You can pass multiple input files to the job by adding them to the enter of this command. Try passing text.txt twice, 
by entering the following command. You should get word frequencies that are twice the size (because the file is being 
counted twice).

```$ python job.py text.txt text.txt``` 

By default, your job is running locally, not using Hadoop. This is good for writing and testing your code, because it 
is fast. Ultimately you want our job to run on a file stored in your Hadoop cluster. We'll see how to do that in the 
next slide.