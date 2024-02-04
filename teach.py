PLACEHOLDER = "[name]"

with open(r"Input\Names\invited_names.txt", "r") as file_names:
    names = file_names.readlines()

with open(r"Input\Letters\starting_letter.txt", "r") as file_letter:
    letter_contents = file_letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(rf".\Output\ReadyToSend\letter_for_{stripped_name}", "w") as file_ready:
            file_ready.write(new_letter)
