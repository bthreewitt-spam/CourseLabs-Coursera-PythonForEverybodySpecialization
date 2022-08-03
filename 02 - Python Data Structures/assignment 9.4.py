# 9.4 Write a program to read through the mbox-short.txt and figure out who has
# sent the greatest number of mail messages. The program looks for 'From ' lines
# and takes the second word of those lines as the person who sent the mail. The
# program creates a Python dictionary that maps the sender's mail address to a
# count of the number of times they appear in the file. After the dictionary is
# produced, the program reads through the dictionary using a maximum loop to find
# the most prolific committer.

file = open(input("Enter file:"))

authors = dict()

for line in file:
    if not line.startswith("From "):
        continue
    authors[line.split()[1]] = authors.get(line.split()[1], 0) + 1

occurrences = None
author = None

for n in authors:
    if occurrences is None:
        occurrences = authors[n]

    if occurrences < authors[n]:
        occurrences = authors[n]
        author = n

print(author, occurrences)
