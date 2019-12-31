#!/bin/bash
FISH="fish"
NONFISH=""
NOCOLOR="\033[0;0m"

read -p "preferred $FISH: " FISH
echo ""

if [ "$FISH" == "clam" ] || [ "$FISH" == "starfish" ]; then
	echo -e "$FISH is not a fish... \n"
	NONFISH="non-"
	
fi

echo -e "$FISH is a nice ${NONFISH}fish! \n"

if [ "$FISH" != "starfish" ]; then
	if  [[ "$FISH" =~ "fish" ]]; then
		echo -e "it's a $FISH fish fish! \n"
		
	fi
fi

say "$FISH is swimming in the water!"

read -p "do you have any questions about your ${FISH}? start your question with \"is my ${FISH}\". " QUES
echo ""

ANSWER=${QUES##*${FISH} }
ANSWER=${ANSWER%\?*}

echo -e "your $FISH is $ANSWER \n"

read -rsn1 CHAR
echo ""

if [ "$CHAR" == "F" ] || [ "$CHAR" == "f" ]; then
	echo -e "\033[2J"
	echo -e "\033[0;0f"

	for x in {30..37}; do
		COLOR="\033[1;${x}m"
		echo -e "${COLOR} ${FISH}! ${NOCOLOR}"
	
	done
fi

echo ""