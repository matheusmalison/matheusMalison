#(I.I)Identificar no dataset o PIB per capita da cidade de Manaus entre os anos de 2010 a 2018
#(I.I)Identificar a partir da utilização do "import urllib.request"

import urllib.request

pagina=urllib.request.urlopen("file:///C:/Matheus-Python/pib_municipio_2010_a_2018.html")
texto=pagina.read().decode("utf8")

produto_interno_bruto_ini=texto.find("2010;AM;Amazonas;Manaus;Manaus")
pib2010=texto[produto_interno_bruto_ini+114:produto_interno_bruto_ini+115+7]

print("PIB Manaus 2010 ... " + pib2010)

produto_interno_bruto_ini=texto.find("2011;AM;Amazonas;Manaus;Manaus")
pib2011=texto[produto_interno_bruto_ini+114:produto_interno_bruto_ini+115+7]

print("PIB Manaus 2011 ... " + pib2011)

produto_interno_bruto_ini=texto.find("2012;AM;Amazonas;Manaus;Manaus")
pib2012=texto[produto_interno_bruto_ini+114:produto_interno_bruto_ini+115+7]

print("PIB Manaus 2012 ... " + pib2012)

produto_interno_bruto_ini=texto.find("2013;AM;Amazonas;Manaus;Manaus")
pib2013=texto[produto_interno_bruto_ini+114:produto_interno_bruto_ini+115+7]

print("PIB Manaus 2013 ... " + pib2013)

produto_interno_bruto_ini=texto.find("2014;AM;Amazonas;Manaus;Manaus")
pib2014=texto[produto_interno_bruto_ini+114:produto_interno_bruto_ini+115+7]

print("PIB Manaus 2014 ... " + pib2014)

produto_interno_bruto_ini=texto.find("2015;AM;Amazonas;Manaus;Manaus")
pib2015=texto[produto_interno_bruto_ini+114:produto_interno_bruto_ini+115+7]

print("PIB Manaus 2015 ... " + pib2015)

produto_interno_bruto_ini=texto.find("2016;AM;Amazonas;Manaus;Manaus")
pib2016=texto[produto_interno_bruto_ini+114:produto_interno_bruto_ini+115+7]

print("PIB Manaus 2016 ... " + pib2016)

produto_interno_bruto_ini=texto.find("2017;AM;Amazonas;Manaus;Manaus")
pib2017=texto[produto_interno_bruto_ini+114:produto_interno_bruto_ini+115+7]

print("PIB Manaus 2017 ... " + pib2017)

produto_interno_bruto_ini=texto.find("2018;AM;Amazonas;Manaus;Manaus")
pib2018=texto[produto_interno_bruto_ini+114:produto_interno_bruto_ini+115+7]

print("PIB Manaus 2018 ... " + pib2018)

#(I.II)Atribuir o resultado da soma dos PIB per capita da cidade de Manaus entre os anos de 2010 a 2018
#(I.II)Utilizar a função "def" para realizar a soma dos dados obtidos no item (I.I)

d1=27832.52 #Dado do PIB de 2010
d2=30303.38 #Dado do PIB de 2011
d3=29837.10 #Dado do PIB de 2012
d4=32201.90 #Dado do PIB de 2013
d5=33370.72 #Dado do PIB de 2014
d6=32597.83 #Dado do PIB de 2015
d7=33534.48 #Dado do PIB de 2016
d8=34373.88 #Dado do PIB de 2017
d9=36445.75 #Dado do PIB de 2018

def somar(): 
    r=d1+d2+d3+d4+d5+d6+d7+d8+d9 
    print(" A soma do PIB per capita entre os anos de 2010 e 2018 da cidade de Manaus" + " resulta em " + str(r))

somar()

media_aritmetica = d1+d2+d3+d4+d5+d6+d7+d8+d9 #soma dos dados

print(" O valor médio do PIB per capita da cidade de Manaus no período que abrange o dataset será de " + str((media_aritmetica)/9))