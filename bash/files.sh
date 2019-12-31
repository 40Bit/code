#!/bin/bash

function arrayCount () {
	python -c "print(len([$1]))"

}

DIRECTORIES=("\"Documents\"" "\"Desktop\"")
echo -n "type in a string >>> "
read -r INPUT

for r in $(seq 0 "$(( $(arrayCount ${DIRECTORIES[*]}) ))"); do
	DIRECTORIES=("Documents" "Desktop")
	LINK="${DIRECTORIES[$r]}/${INPUT}/"
	
	DIRECTORIES=("\"Documents\"" "\"Desktop\"")

	for x in {0..5}; do
		mkdir "$LINK"
		LINK="${LINK}${INPUT}/"
	
	done
done