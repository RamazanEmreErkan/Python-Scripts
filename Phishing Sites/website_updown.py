import urllib.request

lst = [
"http://adana.biz",
"http://adana.ml",
"https://adanadask.com",
"https://adanadask.net",
"http://adanadepremi.com",
"https://adanato.org.tr",
"http://adanaform.com",
"http://adanato.org",
"http://adanaturkey.com",
"http://adanayardim.org",
"https://afaad.net",
"http://afaad.com",
"https://afad-kahramanmaras.net",
"https://afad-online.org",
"https://afad.org.tr",
"https://afad.com",
"https://afad.online",
"https://afad.site",
"http://afad.xyz",
"http://afad.de",
"http://afad.ru",
"http://afad.org",
"http://afad.net",
"http://afad.cf",
"http://afad.ml",
"https://afadbagis.net",
"https://afadbagis.org",
"https://afadbagislari.net",
"https://afadbagisyap.com",
"https://afadd.xyz",
"http://afadd.com",
"https://afadestek.net",
"https://afadyardimyap.net",
"https://afat.com.tr",
"http://afat.online",
"http://afat.co",
"http://afat.de",
"http://afat.org",
"http://afat.ru",
"http://afat.xyz",
"http://afat.com",
"https://afatode.com",
"http://afatto.com",
"https://afd.com.tr",
"https://afd-online.org",
"https://afd.de",
"https://afd.net",
"https://afd.site",
"https://afdafad.xyz",
"https://afd.org",
"https://afd.org.tr",
"http://afd.online",
"http://afd.ru",
"http://afd.co",
"http://afdto.com",
"https://afet.org",
"https://afet.xyz",
"https://afet.site",
"https://afet.com",
"https://afet.org.tr",
"http://afet.ru",
"http://afet.net",
"http://afet.de",
"http://afetacilyardim.net",
"https://afetbagis.com",
"https://afetdestek.com.tr",
"https://afetdestek.org",
"https://afetdestek.com",
"https://afetdestek.net",
"http://afetto.com",
"https://afetyardim.com",
"https://afetyardim.co",
"https://afetyardim.com.tr",
"http://affadd.com",
"http://affd.com",
"https://affd.xyz",
"https://affd.de",
"https://affd.org",
"https://affd.ml",
"http://affd.net",
]
up = list()
down = list()

print(type(urllib.request.urlopen("http://yrd.co").getcode()))

for i in lst:
    try:
        if urllib.request.urlopen(i).getcode() == 200:
            print("up: ",i)
            up.append(lst)
    
    except:
        print("down: ",i)
        down.append(i)


print("up: ", len(up))
print("down: ", len(down))