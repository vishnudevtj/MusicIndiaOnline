# As all the links has been created we cound now download all the movie

MOVIE_DIR=/root/mio
cd $MOVIE_DIR
for i in "$MOVIE_DIR"/{Hindi,Malayalam,Tamil};do
cd $i
    for j in *; do
    cd $j
    echo  $j
    if  [ ! -e "$i"/robot.txt ]
    then
        echo "Robot Does not exists !"
        COUNTER=$(cat count)
        while [ $COUNTER -lt `cat list | wc -l` ];do
            sed -n $COUNTER,$(($COUNTER+10))p list | parallel -P 2 python3 ../../mio.py  >> log 2>&1
            COUNTER=$(($COUNTER+10))
            echo $COUNTER > count
        done
        touch robot.txt
    else
        echo "Robot Exsist !"
    fi
    cd ..
    done
cd ..
done
