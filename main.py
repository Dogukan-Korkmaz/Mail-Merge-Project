def make_letter():
    with open(r"Input\Letters\starting_letter.txt", "r") as file_letter:
        # line = file_letter.readline()
        # x = line.replace(line[5:11], get_name()[0])
        # line = x
        lines = file_letter.readline()
        x = lines.replace(lines[5:11], get_name()[0])
        print(lines[5:11])
            # print(x, end="")


def get_name():
    names = []
    with open(r"Input\Names\invited_names.txt", "r") as file_names:
        lines = file_names.readlines()
        for line in lines:
            striped_line = line.strip()
            names.append(striped_line)
    return names



make_letter()
