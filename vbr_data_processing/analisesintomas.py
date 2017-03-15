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
import nltk
stopwords = nltk.corpus.stopwords.words('portuguese')
stopwords.append('é')
stopwords.append('O')
stopwords.append('.')
stopwords.append(',')

f = codecs.open("sintomas.csv", 'w', "utf-8")
csv.register_dialect('virgula', delimiter=',')
writer = csv.writer(f,dialect='virgula',quoting=csv.QUOTE_NONNUMERIC)

soup = BeautifulSoup(codecs.open('novos/sintomas.html', 'r'),"html5lib")
# print(soup)

tableSintomasEncontrados = soup.find(id="tableSintomasEncontrados")

print(len(tableSintomasEncontrados.find_all("tr")))
for p in tableSintomasEncontrados.find_all("tr"):
    try:
        writer.writerow((p.attrs['id'].replace("se_",""), p.find('td').get_text()))
    except:
        print()

f.close()