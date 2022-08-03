# 10.2 Write a program to read through the mbox-short.txt and figure out the
# distribution by hour of the day for each of the messages. You can pull the hour out
# from the 'From ' line by finding the time and then splitting the string a second time
# using a colon.
#
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#
# Once you have accumulated the counts for each hour, print out the counts, sorted
# by hour as shown below.

file = open(input("Enter file:"))

hrCount = dict()
hrList = list()

for line in file:
    if line.startswith("From "):
        hr = line.split(':')
        hrCount[(hr[0])[-2:]] = hrCount.get((hr[0])[-2:], 0) + 1

for hour, count in hrCount.items():
    hrList.append((hour, count))

hrList.sort()
for hour, count in hrList:
    print(hour, count)
