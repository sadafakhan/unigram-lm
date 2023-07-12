# unigram-lm
```unigram-lm``` takes NYT text files, cleans the data of SGML tags and irregular characters, and tallies the words to output a word-frequency list. 

Args:
* ```./input```: directory path to the folder containing the text files.

Returns: 
* ```output.txt```: text file containing the calculated word-frequency list. 

To run: 
```
python3 src/run.sh input > output/output.txt
```

PROJECT 2 OF LING473 (08/16/2021) 