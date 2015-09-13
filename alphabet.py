__author__ = 'dalton'

list = [
    'billowy',
    'biopsy',
    'chinos',
    'defaced',
    'chintz',
    'sponged',
    'bijoux',
    'abhors',
    'fiddle',
    'begins',
    'chimps',
    'wronged',
]
sorted_list = [''.join(sorted(list[i])) for i in range(len(list))]

for i in range(len(list)):
    if list[i] == sorted_list[i]:
        print(list[i] + ' IN ORDER')
    else:
        print(list[i] + ' NOT IN ORDER')