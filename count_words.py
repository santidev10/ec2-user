#!/usr/bin/env python3
import sys

f = open(sys.argv[1])
words_dict = {}
for line in f:
    for word in line.lower().split():
        word = word.strip("'?,.;!-/\"")
        if word not in words_dict:
            words_dict[word] = 1
        else:
            words_dict[word] += 1

print(sorted(words_dict))
print()
print()
sorted_list = sorted(words_dict)
for i in sorted_list:
    print(i, "--->" , words_dict[i])

f.close()


