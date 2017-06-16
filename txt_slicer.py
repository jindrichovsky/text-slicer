# -*- coding: utf-8 -*–

from sys import argv, exit
from os.path import exists
from re import sub
from unicodedata import normalize


def normalize_str(text):
    try:
        text = unicode(text, 'utf-8')
    except(NameError, TypeError):
        pass

    text = normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode('utf-8')
    text = text.lower()
    text = '\n'.join(text.split())
    text = sub(r'[^a-z0-9\n]+', '', text)

    return str(text)


source_file = argv[1]
output_file = source_file.replace('.txt', '_normalized.txt')

if exists(output_file):
    overwrite = raw_input('File already exists. Overwrite? (Y/N) >')

    if overwrite.lower() == 'n':
        exit(0)
    else:
        pass

else:
    pass

with open(source_file, 'r') as f:
    source_text = f.read()

normalized_text = normalize_str(source_text)

with open(output_file, 'w') as f:
    f.write(normalized_text)

print 'Done!'
