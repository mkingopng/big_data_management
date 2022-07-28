# Example: using JSON data
Now let's use MRJob to work with JSON data. When you click the panel on the right you'll get a connection to a server 
that has a JSON file in your home directory, called "data.json". It contains data about which students are enrolled in 
which courses. You can open the file to inspect its contents.

Let's use MRJob to produce a list of courses and their number of students. The results should be something like this:

```
ZZEN9021: 1
ZZEN9311: 3
ZZEN9313: 4
ZZSC5806: 4
ZZSC5905: 4
ZZSC9001: 2
```

In the panel on the right is a MRJob program to do this. Note that we have imported the `json` library, and used the 
`json.loads()` function to load the JSON data into a variable called "people". 

You can run the job and see the results by using the following command:

`python job.py data.json`
