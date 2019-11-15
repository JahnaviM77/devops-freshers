add(){
r=`expr $1 + $2`

return $r
}

add 2 4

r=$?
echo $r