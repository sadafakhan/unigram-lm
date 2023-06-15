import re
import os
import sys
from collections import defaultdict
wd = sys.argv[1]

word2count = defaultdict(int)
for file in os.listdir(wd):
    with open(os.path.join(wd, file), 'r', encoding='utf8') as f:
        content = f.readlines()
        for line in content:
            # remove tags & initial/final whitespaces, and split by remaining whitespace
            line = re.sub('<.*?>', '', line)
            splits = line.strip().split()

            # remove words with unwanted characters, that start/end with a straight apostrophe, or are empty strings and makes words lowercase
            for word in splits:
                if not re.search('[^A-Za-z\x27]', word) and not word.startswith('\x27') and not word.endswith('\x27') and not word == '':
                    word2count[word.lower()] += 1

for k,v in sorted(word2count.items(), key=lambda x: x[1], reverse=True):
    print(k + "\t" + str(v))