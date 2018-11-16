def query_yes_no(question, default="yes"):
	valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == "":
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")

def start():
	while answer == "":
    answer = input('type "a" to continue ')

    if answer == "a":

        load()
        start()

    else:
        answer = ""