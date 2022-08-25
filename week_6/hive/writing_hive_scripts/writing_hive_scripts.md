# Writing HIVE scripts
Rather than executing HQL statements one-by-one in a Hive shell, you can bundle 
them into a script and execute them all together. This is also a good way to 
save your statements, edit them, and run them easily whenever you like.

Let's see how to do this.

When you click the panel on the right you'll get a terminal connection to a 
server that has Hadoop, YARN, and Hive installed and running, and has the file 
"text.txt" in your home directory.

It also has a file called "frequency.hql". This is just a file containing the 
HQL statements that we ran individually to get the frequency of words in 
text.txt. You can open the file and inspect its contents.

To execute the statements in the file, just enter the following command in the 
terminal:

> $ hive -f frequency.hql

This command tells Hive to execute the statements in the file called 
"frequency.hql".

You should see the commands being executed.