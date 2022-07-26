# Starting HDFS
Click on the panel to activate the terminal.

The first thing you need to do is start HDFS (the Hadoop file management system). Run the following command at the 
prompt in the terminal window (i.e. type or copy it at the prompt and then hit enter): 

```$ start-dfs.sh```

You have just run a Linux command. Linux is the operating system on the server you are connected to. Linux is an 
alternative to the operating systems Windows and MacOS, and is very commonly used as the operating system for servers. 
To work with Hadoop and HDFS, and the other pieces of software that are running on the server, you will have to use a 
few Linux commands. Don't worry - they're pretty simple, and will be explained.  

Linux uses a dollar sign ($) as a prompt. Throughout these slides, when you see $ followed by a command you know it's a 
Linux command. 

To check that HDFS has started successfully, run the following command:
```$ jps```

The command "jps" is short for "Java process status" - it lists all Java processes that are running. Since Hadoop nodes 
run as Java processes, you should see the following items on the list:

```
DataNode
SecondaryNameNode
NameNode
```

## Your default directory in HDFS

In HDFS, your default directory is /user/{your username}. On Ed, your username is user. Thus, your default directory is 
/user/user. To see the contents of this directory, use the following command ("ls" is short for "list"):

```$ hdfs dfs -ls```

Initially you'll get an error message saying there's no such file or directory. This is because your default directory 
does not yet exist. You can create it using the mkdir command (short for "make directory").

First create the directory /user, then create directory /user/user:

```$ hdfs dfs -mkdir /user```

```$ hdfs dfs -mkdir /user/user```

Alternatively, you can create both directories in one step by adding the -p option, which tells Hadoop to automatically 
create parent directories as required ("p" is for "parents"):

```$ hdfs dfs -mkdir -p /user/user```

Now try listing the contents again:

```$ hdfs dfs -ls```

You will get an empty result set, because there is nothing in this directory yet (but you won't get an error this time).

Rather than re-typing a command that you have already run, you click the up arrow - Linux will scroll through the 
previous commands, and when you get to the one you want you can just hit enter. 

## Adding a file

In addition to HDFS the server also has its own regular file system, called its local file system (note: "local" here 
means local to the server you are connected to - it does mean local to your personal computer, the one you are now 
using). There is file called "text.txt" in your home directory in this local file system. You can check the contents of 
your home directory by running the following command (note that there is no dash "-" in front of "ls" when you are 
working with the local file system):

```$ ls```

You should see the file "text.txt" listed.

You can copy this file into your default directory in HDFS using the -put command, followed by the name of the local 
file that you want to copy to HDFS:

```$ hdfs dfs -put text.txt```

You can check that the operation was successful by listing the contents of your default directory again:

```$ hdfs dfs -ls```

You should see text.txt in the results. There is a lot of information about the file listed - the name of the file is 
at the right-hand end.

## Creating sub-directories

You can create sub-directories in HDFS using the -mkdir command. For example, to create a subdirectory of your default 
directory called "files" use the following command:

```$ hdfs dfs -mkdir files```

You can check that the operation was successful by listing the contents of your default directory:

```$ hdfs dfs -ls```

You should now see the file "text.txt", which you added above, and the directory "files", which you just created.

## Moving files

You move files in HDFS using the -mv command. Let's move the file "text.txt" from your default directory into the files 
subdirectory. Use the following command:

```$ hdfs dfs -mv text.txt files```

After -mv  you specify the path of the file you want to move, and then the path of where you want to move it to.

To check that this worked, you can list the contents of your default directory as you have been doing - it should 
contain just the sub-directory files:

```$ hdfs dfs -ls```

You can list the content of files using the following command:

```$ hdfs dfs -ls files```

You should see the file "text.txt" listed in the files directory.

## Copying files

You can copy files in HDFS using the -cp command. Let's make a copy of text.txt in files, keeping it in the same 
directory, and calling it "text2.txt": 

```$ hdfs dfs -cp files/text.txt files/text2.txt```

To check that this worked, try listing the contents of the files directory:

```$ hdfs dfs -ls files```

## Renaming files

To rename a file, just move it to the same directory but with a different name. Let's rename "text2.txt" to 
"moreText.txt":

```$ hdfs dfs -mv files/text2.txt files/moretext.txt```

To check that this worked, try listing the contents of the files directory:
```$ hdfs dfs -ls files```

## Removing files

You can remove a file using the -rm command. Let's remove the file "moreText.txt" from the files directory:
```$ hdfs dfs -rm files/moretext.txt```

To check that this worked, try listing the contents of the files directory:
```$ hdfs dfs -ls files```

## Viewing files

To see the contents of a file you can use the -cat command ("cat" is short for "concatenate" - you can use -cat to concatenate the contents of files):

```$ hdfs dfs -cat files/text.txt```

## Getting files

To copy a file from HDFS to the local file system on the server you can use the -get command. The following command will copy the file "files/text.txt" in HDFS to "text2.txt" in your home directory in the local file system:

```$ hdfs dfs -get files/text.txt text2.txt```

To check that this worked, try listing the contents of your home directory in the local file system:

```$ ls```

## More commands

You can find a complete list of HDFS commands at the Hadoop website: 

https://hadoop.apache.org/docs/r2.4.1/hadoop-project-dist/hadoop-common/FileSystemShell.html