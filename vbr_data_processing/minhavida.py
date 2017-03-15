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

f=codecs.open('dados/test.html', 'r')
content = f.read()
soup = BeautifulSoup(content,"html5lib")
# print(soup)

visaogeral = soup.find(id="visao-geral")
sintomas = soup.find(id="sintomas")
diagnostico_e_exames = soup.find(id="diagnostico-e-exames")
tratamento_e_cuidados = soup.find(id="tratamento-e-cuidados")
convivendo_prognostico = soup.find(id="convivendo-prognostico")

print(len(visaogeral.find_all("p")))
for p in visaogeral.find_all("p"):
    print(p)
# print(sintomas.find_all("p"))
# print(diagnostico_e_exames.find_all("p"))
# print(tratamento_e_cuidados.find_all("p"))
# print(convivendo_prognostico.find_all("p"))
