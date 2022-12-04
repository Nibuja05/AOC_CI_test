check_solution() {
	res=`make run-1 INPUT="./input.txt"`
	solution=`cat ./solution`
	if [ "$res" = "$solution" ]; then
		echo "Success!"
		exit 10
	else
		echo "Failure! $res"
		exit 0
	fi
}
check_solution