from dataclasses import dataclass

file = open('bot/tokens.txt')
read_file = list(map(str.strip, file.readlines()))
file.close()
d = dict()
for i in read_file:
    d[i.split()[0]] = i.split()[-1]

@dataclass
class token:
    all_tokens = d