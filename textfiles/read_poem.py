# jabber = open('Jabberwocky.txt', 'r')
#
# for text in jabber:
#     print(text.rstrip())
#
# jabber.close()

with open('Jabberwocky.txt', 'r') as jabber:
    for line in jabber:
        print(line.strip())

with open('Jabberwocky.txt', 'r') as jabber2:
    lines = jabber2.readlines()

print(lines[2])
