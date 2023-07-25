filenames = ['file1.txt', 'file2.txt']
for filename in filenames:
    # ... see code above
        #open file
        with open(filename, 'r') as f:
            lines = f.readlines()

        #find index of line to remove
        for index, line in enumerate(lines):
            if 'delete me' in line:
                #remove line
                lines.pop(index)
                break

#write new file
        with open(filename, 'w') as f:
            f.write(''.join(lines))