#chave python 
meu_dicionario_cursos = {"python":"60h","java":"80h","javaScrip":"60h"}

#exibir os itens do dicionario 
print(meu_dicionario_cursos)
#exibir elegantemete
for item in meu_dicionario_cursos.items():
    print(item)
#exibir elegantemete so as chaves 
for cha in meu_dicionario_cursos.keys():
    print(cha)
#exibir elegantemete so os valores
for val in meu_dicionario_cursos.values():
    print(val)
#adionar um elemento ao dicionario
meu_dicionario_cursos["google foundations"] = "40h"
meu_dicionario_cursos["python framewordk "] = "80h"
meu_dicionario_cursos["python pata data science"] = "60h"
#exibir qual a caga horaria do curso google foundations
for nome in meu_dicionario_cursos.items():
for carga in  meu_dicionario_cursos.values():  
    if carga == "google foundations":
        print(carga)
#exibir a carga horaria do curso de excel 
meu_dicionario_cursos["excel"] ="10h"
print(meu_dicionario_cursos)
