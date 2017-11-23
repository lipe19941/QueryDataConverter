# QueryConverter

import re
import datetime


arquivoread = open("Arrumar.txt","r")
for linha in arquivoread:
    data = re.findall(r'\b\d{4}-\d\d?-\d\d?\b', linha)
    data_form = ''.join(map(str, data))
    pos_sub = linha.find(data_form)

    dia = data_form[8:10]
    mes = data_form[5:7]
    ano = data_form[0:4]
    

    
    if data_form !="":
        nova_data = "%s/%s/%s"%(dia,mes,ano)
        linha_nova = linha[0:pos_sub] + nova_data + linha[pos_sub+10:]
        #linha a ser comitada no txt
        print(linha_nova)
        arquivowrite = open("Arrumado.txt","a")
        arquivowrite.write(linha_nova)
        arquivowrite.close()
    else:
        arquivowrite = open("Arrumado.txt","a")
        arquivowrite.write(linha)
        arquivowrite.close()

arquivoread.close()


    
    
