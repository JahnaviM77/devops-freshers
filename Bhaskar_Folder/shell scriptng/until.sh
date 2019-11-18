read n
i=1
until [ $i -gt 10 ]
do
     m=`expr $n \* $i`
     echo "$n * $i=$m"
     i=`expr $i + 1`
done
