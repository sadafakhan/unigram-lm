import re
import os
import sys
from collections import defaultdict

word2count = defaultdict(int)
working_dir = sys.argv[1]

for file in os.listdir(working_dir):
    with open(os.path.join(working_dir, file), 'r', encoding='utf8') as f:
        content = f.readlines()

        for line in content:

            # remove tags & initial/final whitespaces, and split by remaining whitespace
            line = re.sub('<.*?>', '', line)
            line = line.strip()
            splits = re.split('\\s+', line)

            clean = []

            # remove words with unwanted characters or that start or end with a straight apostrophe
            # makes remaining words lowercase
            for word in splits:
                if re.search('[^A-Za-z\x27]', word) or word.startswith('\x27') or word.endswith('\x27'):
                    continue
                else:
                    clean.append(word.lower())

            # instantiates or increments key-value pairs
            for word in clean:
                if word == '':
                    continue
                elif word not in word2count:
                    word2count[word] = 1
                else:
                    word2count[word] += 1

for pair in sorted(word2count.items(), key=lambda x: x[1], reverse=True):
    print(str(pair[0]) + "\t" + str(pair[1]))