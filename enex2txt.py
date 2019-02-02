import argparse
import os
import re
import sys

from xml.etree import ElementTree as etree
from inscriptis import get_text

parser = argparse.ArgumentParser(description='single .enex convert')
parser.add_argument('--src', help='.enex source file')
parser.add_argument('--dest', help='.txt directory')
parser.add_argument('--dest-ext', help='suffix for .txt file titles', default='.raw.txt')

args = parser.parse_args()

root = etree.parse(args.src)

for n in root.findall('note'):
    title = n.find('title').text
    with open(os.path.join(args.dest, title + args.dest_ext), 'w') as dest:
        dest.write(get_text(n.find('content').text))
