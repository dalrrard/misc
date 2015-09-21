__author__ = 'dalton'


def printer(x):
    print(''.join(['X' if i == 1 else ' ' for i in x]))

def updater(line):
    return [0] + [line[i-1] ^ line[i+1] for i in range(1,len(line)-1)] + [0]

line = input('Enter:')
line = [int(i) for i in line]
line = [0] + line + [0]
counter = 0

while counter <= 50:
    printer(line)
    line = updater(line)
    counter += 1
