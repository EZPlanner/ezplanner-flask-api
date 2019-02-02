import sys
sys.path.insert(0, '../')
from scripts.pdfparser import parser


print(parser('test/t.pdf'))