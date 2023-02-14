num=9
echo "Vamos a multiplicar por:" $num
for i in `seq 1 10`; do
    echo $num*$i = $(($num*$i))
done
