PLACEHOLDER = "[name]"

with open("/Users/wasiu/PycharmProjects/Day 24/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("/Users/wasiu/PycharmProjects/Day 24/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        sname = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, sname)
        print(new_letter)
        with open(f"./Output/ReadyToSend/letter_for_{sname}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)