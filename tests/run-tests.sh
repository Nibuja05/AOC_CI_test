#!/usr/bin/env bash
set -x

MAKE="make -s"
OUTPUT="website/data/"

echo $(cat ./website/data/01.json)

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
  find "../$1" -maxdepth 2 -type f -regex '.*/\(M\|m\|GNUm\)akefile' 
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
  name=$4
  expect=$(jq --raw-output ".day$day.$first_second" solutions.json)
  valid="false"
  if [[ "$solution" == "$expect" ]]; then
    valid="true"
  fi
  file="$OUTPUT$day.json"
  content=$(jq -n --arg valid "$valid" --argjson results "[]" '$ARGS.named')
  query='{.'"$name"' = '"$content"'} '"$file"''
  res=$(jq --argjson variable "$content" '.'"$name"' = $variable' "$file")
  echo "$res" > "$file"
}

is-valid() {
  day=$1
  name=$2
  file="$OUTPUT$day.json"
  echo "$(jq '.'"$name"'.valid' "$file")"
}

get-name() {
  path=$1
  dir=$(dirname $1)
  echo $(echo "$dir" | sed -e 's/.*\///g')
}

day=
first_second=second
list_only=false
build_only=false
verify_only=false
input=
while getopts "hlbv12d:i:" option; do
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

# [[ -z "$input" ]] && printf "Missing -i INPUT_FILE\n" && exit 1;
if [[ -z "$input" ]]; then
  input="../../tests/inputs/$day"
fi

if [[ $verify_only = "true" ]]; then

  entry-points $day | while read path; do
    if [[ "$first_second" = "first" ]]; then
      solution=$(run-project-1 "$path" "$input")
    elif [[ "$first_second" = "second" ]]; then
      solution=$(run-project-2 "$path" "$input")
    fi
    [[ -z "$solution" ]] && solution="empty"
    name=$(get-name "$path")
    verify-solution $day $first_second $solution $name || exit 1
  done
  exit;
fi

# [[ $verify_only = "true" ]] && exit;

# FUCK BASH
# (┛◉Д◉)┛彡┻━┻

# commands=$(entry-points "$day" | while read path; do
#   dir=$(dirname $path)
#   cmd=$($MAKE -n INPUT=$input -C $dir run-1)
#   cmdRaw="$MAKE -n INPUT=$input -C $dir run-1"
#   # printf "%s\n" "--prepare"
#   # printf "%s\n" "sudo cd $dir"
#   # printf "sudo cd $dir ; "
#   # printf "$dir/"
#   # printf "%s\n" "$cmd"
#   printf "%s\n" "python3"
#   # (cd $dir; pwd)
# done)
# printf "\n\n\n"
# echo $commands
# hyperfine -N $commands --export-json blub.json

entry-points "$day" | while read path; do
  printf "\n\n\n"
  dir=$(dirname $path)
  name=$(get-name "$path")
  cmd=$($MAKE -n INPUT=$input -C $dir run-1)
  cmdRaw="$MAKE -n INPUT=$input -C $dir run-1"

  valid=$(is-valid "$day" "$name")
  if [[ $valid = '"true"' ]]; then

    # FUCK BASH
    # (┛◉Д◉)┛彡┻━┻
    command="python3" # need to run true command here, not this placeholder
    hyperfine $command --export-json temp.json

    results=$(jq '.results' temp.json)
	rm temp.json
    out=$(jq -n --argjson test "$results" '$ARGS.named')
    file="website/data/$day.json"
    res=$(jq --argjson variable "$results" '.'"$name"'.results = $variable' "$file")
    echo "$res" > "$file"
  fi
done