import os
import sys
import fileinput
from pprint import pprint 

files = []
for dirname, dirnames, filenames in os.walk('.'):
    # print path to all subdirectories first.
    for subdirname in dirnames:
        files.append(os.path.join(dirname, subdirname))

    # print path to all filenames.
    for filename in filenames:
        files.append(os.path.join(dirname, filename))

files = filenames

for filename in filenames:
    # ... see code above
        #open file
        with open(filename, 'r') as f:
            lines = f.readlines()

        #find index of line to remove
        for index, line in enumerate(lines):
            if '<text x="10" y="666" font-size="13" font-family="Arial" fill="#cccccc">https://urait.ru</text>' in line:
                #remove line
                print("Found one!")
                lines=[line.replace( '''<text x="10" y="666" font-size="13" font-family="Arial" fill="#cccccc">https://urait.ru</text></svg>''', "</svg>" ) for line in lines]
                #lines.pop(index)
                #lines.append(index, "</svg>") 
                #line.replace( '''<text x="10" y="666" font-size="13" font-family="Arial" fill="#cccccc">https://urait.ru</text></svg>''', "</svg>" )
                break

#write new file
        with open(filename, 'w') as f:
            f.write(''.join(lines))
