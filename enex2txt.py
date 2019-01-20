import re
import sys
from xml.etree import ElementTree as etree
from inscriptis import get_text

root = etree.parse(sys.stdin)
notes = root.findall('note')
print(len(notes))
for n in notes:
    c = n.find('content').text
    print(get_text(c))
