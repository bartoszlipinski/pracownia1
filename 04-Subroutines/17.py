def countLetter(string, letter):
    counter = 0
    for i in string:
        if i == letter:
            counter += 1
    return counter

print(countLetter("You never get a second chance to make a first impression", "e"))
