read n
i=1
select i in 5 
do
     m=`expr $n \* $i`
     echo "$n * $i=$m"
     i=`expr $i + 1`
done