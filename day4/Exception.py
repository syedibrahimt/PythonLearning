try:
    f = open('sample.txt', 'r')
    f.write('This is the next line')
except IOError:
    print('### COULD NOT FIND THE FILE ###')
else:
    print('### SUCCESS ###')
    f.close()
