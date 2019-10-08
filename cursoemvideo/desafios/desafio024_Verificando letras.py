#Opção tentativa
#cid = str(input('Em que cidade você nasceu? ')).strip()
#sep = cid.split()
#san = 'Santo'
#santo = [san, san.upper(), san.lower(), san.title(), san.capitalize()]
#print(sep[0] in (santo))

#Opção Original
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')
