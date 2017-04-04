from bs4 import BeautifulSoup
import glob
import nltk
import time
import logging
logging.getLogger().setLevel(logging.DEBUG)

stopwords = nltk.corpus.stopwords.words('portuguese')
stopwords.append('é')
stopwords.append('O')
stopwords.append('.')
stopwords.append(',')
stopwords.append(';')
stopwords.append('Sinônimos:')


for file in glob.glob("dados/*.txt"):
    with open(file) as data_file:
        content = data_file.read()
        logging.debug("{}".format(file))
        soup = BeautifulSoup(content, "html5lib")
        visaogeral = soup.find(id="visao-geral")
        sintomas = soup.find(id="sintomas")
        #
        if(visaogeral!=None):
            VISAO_GERAL_CONTENT = ''
            for p in visaogeral.find_all("p"):
                VISAO_GERAL_CONTENT+=p.text.strip()+'; '
            print(VISAO_GERAL_CONTENT)

        if(sintomas!=None):
            print("SINTOMAS")
            SINTOMAS_CONTENT = ''
            for p in sintomas.find_all("p"):
                SINTOMAS_CONTENT += p.text.strip() + '; '
            print(SINTOMAS_CONTENT)

    time.sleep(1)

# f=codecs.open('dados/test.html', 'r')
# content = f.read()
# soup = BeautifulSoup(content,"html5lib")
# # print(soup)
#
# visaogeral = soup.find(id="visao-geral")
# sintomas = soup.find(id="sintomas")
# diagnostico_e_exames = soup.find(id="diagnostico-e-exames")
# tratamento_e_cuidados = soup.find(id="tratamento-e-cuidados")
# convivendo_prognostico = soup.find(id="convivendo-prognostico")
#
# # print(len(visaogeral.find_all("p")))
# # for p in visaogeral.find_all("p"):
# #     print(p)
#
# print("visaogeral")
# visaogeral.find_all("p")
# print("sintomas")
# print(sintomas.find_all("p"))
# print("diagnostico_e_exames")
# print(diagnostico_e_exames.find_all("p"))
# print("tratamento_e_cuidados")
# print(tratamento_e_cuidados.find_all("p"))
# print("convivendo_prognostico")
# print(convivendo_prognostico.find_all("p"))
