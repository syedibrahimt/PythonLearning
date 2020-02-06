import re

patterns = ['text1', 'text2']

paragraph = 'This is the sample paragraph to eliminate the text1 and ext2 from this paragraph using the regular ' \
            'expression '

for pattern in patterns:
    if re.search(pattern, paragraph):
        print(f'MATCH FOUND for {pattern}')
    else:
        print(f'MATCH NOT FOUND for {pattern}')
