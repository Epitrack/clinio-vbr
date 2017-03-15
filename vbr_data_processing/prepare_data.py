import sys
import json
from pprint import pprint
import glob, os
import csv
import codecs
from bs4 import BeautifulSoup
import glob, os
import csv
import codecs
import io
import json
from pprint import pprint
import re

_URL = "../../snout-api/public/train_clinio.csv"

f = codecs.open("dados_treinamento.csv", 'w', "utf-8")
csv.register_dialect('virgula', delimiter='|')
writer = csv.writer(f,dialect='virgula',quoting=csv.QUOTE_NONE)

with open(_URL, 'r') as csvfile:
    content = csv.reader(csvfile, delimiter=',')
    for row in content:
        print(row)
        writer.writerow((row[1].upper(),row[0].upper().strip()))
f.close()