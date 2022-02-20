read yes_or_no
# check if the input is y or Y
if [ $yes_or_no == "y" ] || [ $yes_or_no == "Y" ]; then
echo "YES"
elif [ $yes_or_no == "n" ] || [ $yes_or_no == "N" ]; then
echo "NO"
else
echo "Please enter y or Y"
fi
exit 0