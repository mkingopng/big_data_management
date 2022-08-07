# Testing your mapper and reducer locally
With MRJob you can test your mapper() and reducer() methods individually to check that each is working properly.

To test your mapper, add the --mapper option to your run command:

```$ python job.py --mapper text.txt```

Similarly, to test your reducer add the --reducer option. In this case, you won't be able to use text.txt as the input 
to your job, because your reducer method is expecting a different kind of file - it's expecting the results of your mapper.

You have a couple of options.

First, you can send the results of your mapper to an output file and then pass that output file to your job. You can 
call the output file whatever you want - let's call it "output.txt". Here are the commands you should use:

```$ python job.py --mapper text.txt > output.txt```

```$ cat output.txt | sort -k1,1 | python job.py --reducer```

Second, you can run your mapper and pipe the results to your reducer, with a single command:

```$ python job.py --mapper text.txt | sort -k1,1 | python job.py --reducer```
