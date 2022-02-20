read x
read y
read z

# check if the inputs are the same
if [ $x == $y ] && [ $x == $z ] && [ $y == $z ]; then
    echo "EQUILATERAL"
elif [ $x == $y ] || [ $x == $z ] || [ $y == $z ]; then
    echo "ISOSCELES"
else
    echo "SCALENE"
fi

exit 0
