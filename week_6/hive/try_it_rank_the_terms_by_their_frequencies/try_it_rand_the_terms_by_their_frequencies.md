# Try it: Rank the terms by their frequencies
In this activity, we use the ABC news dataset again. Your task is to use Hive 
to compute the frequency for each term within each year, and then sort the 
result by the year first, and then by the frequency in descending order. For 
the terms with the same frequency, rank them in alphabetical order.

You will practice how to use views, the built-in functions (such as explode() 
and substr()), and lateral view in this activity. In addition, you also need to 
use "order by" and the rank() function to sort the final result. The rank() 
function is similar to that in SQL. You can see some examples at this page: 
https://craftingschool.wordpress.com/2017/06/03/hive-rank-function/.

> $ hive -f script.hql
