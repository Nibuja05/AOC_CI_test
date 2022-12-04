build() {
	echo "Build!"
}

validate() {
	echo "Validate!"
	# res=`make run-1 INPUT="./input.txt"`
	# solution=`cat ./solution`
	# if [ "$res" = "$solution" ]; then
	# 	echo "Success!"
	# 	exit 1
	# else
	# 	echo "Failure! $res"
	# 	exit 0
	# fi
}
# check_solution

run() {
	echo "Run!"
}

helpFunction()
{
   echo ""
   echo "Usage: $0 -b parameterA -b parameterB -c parameterC"
   echo -e "\t-b Description of what is parameterA"
   echo -e "\t-v Description of what is parameterB"
   echo -e "\t-r Description of what is parameterC"
   exit 1 # Exit script after printing help
}

while getopts "12bd:i:" opt
do
   case "$opt" in
	  1 ) echo Part 1 ;;
	  2 ) echo Part 2 ;;
      b ) build ;;
      d ) echo Selected Tag $OPTARG ;;
      i ) echo Input is $OPTARG ;;
      ? ) helpFunction ;; # Print helpFunction in case parameter is non-existent
   esac
done