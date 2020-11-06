f = open('filename')
text_modes = ['r', 'w', 'a', 'r+']
binary_modes = ['br', 'bw', 'ba', 'br+']

f = open('filename', 'w')
f.write('The world is changed.\nI taste it in the water.\n')
f.close()

f = open('filename', 'r+')
f.read()
'The world is changed.\nI taste it in the water.\n'
f.tell()
# 47

f.read()
''
f.seek(0)
f.tell()
# 0

print(f.read())
f.close() # файлы всегда нужно закрывать
# The world is changed.
# I taste it in the water

f = open('filename', 'r+')
f.readline()
f.close()

'The world is changed.\n'
f = open('filename', 'r+')
f.readlines()
['The world is changed.\n', 'I taste it in the water.\n']

with open('filename') as f:
    print(f.read())

