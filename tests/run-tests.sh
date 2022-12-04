#!/usr/bin/env bash
set -x

MAKE="make -s"

help() {
  # Display help
  echo $0
  echo
  echo "Run tests and timings for solutions"
  echo "Syntax: $0 -h|-l"
  echo "Options:"
  echo "  -h  Show this help"
  echo "  -l  List directories considered for tests"
  echo " TBD"
}

entry-points() {
  day=$1
  find "./$1" -maxdepth 2 -type f -regex '.*/\(M\|m\|GNUm\)akefile' 
}

build-project() {
  dir=$(dirname $1)
  $MAKE -C $dir build
}

run-project-1() {
  dir=$(dirname $1)
  input=$2
  $MAKE INPUT="$input" -C $dir run-1
}

run-project-2() {
  dir=$(dirname $1)
  input=$2
  $MAKE INPUT="$input" -C $dir run-2
}

verify-solution() {
  day=$1
  first_second=$2
  solution=$3
  expect=$(jq --raw-output ".day$day.$first_second" solutions.json)
  [[ "$solution" == "$expect" ]]
}

day=
first_second=second
list_only=false
build_only=false
verify_only=false
input=
while getopts "hlb12d:i:" option; do
   case $option in
      h) # display Help
         help
         exit;;
      l) # List only
         list_only=true;;
      b) # Build only
         build_only=true;;
      v) # Verify only
         verify_only=true;;
      1) # Run first variant
         first_second=first;;
      2) # Run second variant
         first_second=second;;
      i) # Set input
         input=$(realpath "$OPTARG");;
      d) # Set day
         day=$(printf "%02g" $OPTARG);;
     \?) # Invalid option
         echo "Error: Invalid option!"
         help
         exit;;
   esac
done

[[ -z "$day" ]] && printf "Missing -d DAY\n" && exit 1;

if [[ "$list_only" = "true" ]]; then
  entry-points "$day"
  exit
fi

entry-points "$day" | while read path; do
  build-project "$path" || printf "Failed to build project '$path'!\n"
done
[[ $build_only = "true" ]] && exit;

[[ -z "$input" ]] && printf "Missing -i INPUT_FILE\n" && exit 1;

entry-points $day | while read path; do
  if [[ "$first_second" = "first" ]]; then
    solution=$(run-project-1 "$path" "$input")
  elif [[ "$first_second" = "second" ]]; then
    solution=$(run-project-2 "$path" "$input")
  fi
  verify-solution $day $first_second $solution || exit 1
done

[[ $verify_only = "true" ]] && exit;

# FUCK BASH
# (┛◉Д◉)┛彡┻━┻
commands=$(entry-points "$day" | while read path; do
  dir=$(dirname $path)
  cmd=$($MAKE -n INPUT=$input -C $dir run-1)
  printf "%s\n" "--prepare"
  printf "%s\n" "cd $dir"
  printf "%s\n" "$cmd"
done)
echo $commands
hyperfine -N $commands
