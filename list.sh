# scraping the webpage and getting all the list of movie songs . 
mkdir {Hindi,Malayalam,Tamil}  Hindi/{19{3..9}0,20{0,1}0}s  Tamil/{19{3..9}0,20{0,1}0}s  Malayalam/{19{5..9}0,20{0,1}0}s
for i in {Hindi,Malayalam,Tamil} ; do
    cd $i
    for j in *; do
        cd $j
        echo listing $i/$j ...
        python3 ../../list.py http://mio.to/$i/Movie+Songs/albums/decade/`echo $j | sed -r 's/([0-9]+)s/\1/'` >> list 
        sleep 1s
        echo 1 > count
        cd ..
    done
    cd ..
done
