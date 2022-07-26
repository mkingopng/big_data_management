# Adding a combiner
Here is the word frequency job again, but with a combiner added.

Try running the job:

```$ python job.py text.txt```

Note that in this simple example, the combiner does the same thing as does the reducer. However, in most applications, 
you need to write a different combiner to locally aggregate the mapper output. 

In this week's assessment, you will need to do a task about average value computation, and you are required to use a 
combiner for that task. The combiner and the reducer will be different in that task.