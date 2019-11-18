read n
i=1
for i in 1 2 3 4 5 6 7 8 9 10
do
     m=`expr $n \* $i`
     echo "$n * $i=$m"
     i=`expr $i + 1`
done