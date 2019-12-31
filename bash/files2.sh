#!/bin/bash

FOLDERS=( "Documents" "Desktop" )

for x in "${FOLDERS[@]}"; do
	z="${x}"
	echo $z
	LSEQ="$(ls -1 ${x} | wc -l)"
		
	for q in $(seq 1 ${LSEQ}); do
		z="${z}/${LSEQ}"
		mkdir "${z}"
		
	done
done