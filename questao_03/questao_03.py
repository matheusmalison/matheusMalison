
import urllib.request

pagina=urllib.request.urlopen("file:///C:/Matheus-Python/pib_municipio_2010_a_2018.html")
texto=pagina.read().decode("utf8")

pib=input("Digite a localidade: ")
pib_pos=texto.find(pib)
pib_txt=texto[pib_pos:5566]
pib_per_capita_pos=pib_txt.find(".")
valor_pib=texto[pib_pos:pib_pos+pib_per_capita_pos+3]

if(pib_pos>-1):
    print("PIB per capita de " + pib)
    print("O valor do PIB..." + valor_pib)
else:
    print("Informação não encontrada")