import re
import sys
from xml.etree import ElementTree as etree
from inscriptis import get_text

root = etree.parse(sys.stdin)
notes = root.findall('note')
for n in notes:
    sys.stdout.write(get_text(n.find('content').text))
