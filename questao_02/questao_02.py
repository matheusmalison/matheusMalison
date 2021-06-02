#

import urllib.request

pagina=urllib.request.urlopen("file:///C:/Matheus-Python/AnyConv.com__pib_municipio_2010_a_2018.html")
texto=pagina.read().decode("utf8")

produto_interno_bruto_ini=texto.find("Alta Floresta D'Oeste")
pib2010=texto[produto_interno_bruto_ini+103:produto_interno_bruto_ini+103+8]

print("PIB Alta Floresta D'Oeste 2010 .... " + pib2010)

produto_interno_bruto_ini=texto.find("Ariquemes")
pib2010=texto[produto_interno_bruto_ini+91:produto_interno_bruto_ini+91+8]

print("PIB Ariquemes 2010 .... " + pib2010)

produto_interno_bruto_ini=texto.find("Cabixi")
pib2010=texto[produto_interno_bruto_ini+84:produto_interno_bruto_ini+84+8]

print("PIB Cabixi 2010 .... " + pib2010)

produto_interno_bruto_ini=texto.find("Cacoal")
pib2010=texto[produto_interno_bruto_ini+100:produto_interno_bruto_ini+100+8]

print("PIB Cacoal 2010 .... " + pib2010)

produto_interno_bruto_ini=texto.find("Cerejeiras")
pib2010=texto[produto_interno_bruto_ini+94:produto_interno_bruto_ini+94+8]

print("PIB Cerejeiras 2010 .... " + pib2010)

produto_interno_bruto_ini=texto.find("2010")
pib2010=texto[produto_interno_bruto_ini+94:produto_interno_bruto_ini+94+8]

print("PIB Cerejeiras 2010 .... " + pib2010)