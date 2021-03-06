import math
import requests
from bs4 import BeautifulSoup

hisse_siteleri = [] 
  
hisse_sitesi_adedi = int(input("Kaç tane hisseniz var? ")) 

for i in range(0, hisse_sitesi_adedi): 
    hisse_siteleri_link = input("Hisse sitesini Bigpara.Hurriyet üzerinden girin: ")  
    hisse_siteleri.append(hisse_siteleri_link)
      
# print(hisse_siteleri)

hisse_siteleri_maliyetleri = []

for i in range (len(hisse_siteleri)):
    r = requests.get(hisse_siteleri[i])
    soup = BeautifulSoup(r.text, 'html.parser')
    h_s_maliyet_temp = soup.findAll("span", {"class": "value"})
    h_s_maliyet_temp = [tag.text for tag in h_s_maliyet_temp]
    hisse_siteleri_maliyetleri.append(h_s_maliyet_temp)
    hisse_siteleri_maliyetleri[i] = [sub.replace("," , ".") for sub in hisse_siteleri_maliyetleri[i]]
    hisse_siteleri_maliyetleri[i] = list(map(float, hisse_siteleri_maliyetleri[i]))

# print(hisse_siteleri_maliyetleri)


hisse_adlari = []

for i in range (len(hisse_siteleri)):
    r = requests.get(hisse_siteleri[i])
    soup = BeautifulSoup(r.text, 'html.parser')
    hisse_adlari_temp = soup.findAll("span", {"itemprop": "title"})
    hisse_adlari_temp = [tag.text for tag in hisse_adlari_temp]
    hisse_adlari.append(hisse_adlari_temp[3])


# print(hisse_adlari)


hisse_siteleri_maliyetleri_advance = [item[0] for item in hisse_siteleri_maliyetleri]

# print(hisse_siteleri_maliyetleri_advance)


lot_adedi = []
maliyet = []
kar_zarar = []

for i in range (len(hisse_siteleri)):
    lot_adedi_temp = int(input("Lot adedini girin: "))
    lot_adedi.append(lot_adedi_temp)

# print(lot_adedi)

for i in range (len(hisse_siteleri)):
    maliyet_temp = float(input("Maliyetleri girin: "))
    maliyet.append(maliyet_temp)

# print(maliyet)

for i in range (len(hisse_siteleri)):
    kar_zarar_temp = (lot_adedi[i] * hisse_siteleri_maliyetleri_advance[i]) - (lot_adedi[i] * maliyet[i])
    kar_zarar_temp = round(kar_zarar_temp, 2)
    kar_zarar.append(kar_zarar_temp)

# print(kar_zarar)


for i in range(len(hisse_siteleri)):
    print("Anlık değerleri \n", hisse_adlari[i], ":", hisse_siteleri_maliyetleri_advance[i])
    print("Lot adediniz \n", hisse_adlari[i], ":", lot_adedi[i])
    print("Maliyetiniz \n", hisse_adlari[i], ":", maliyet[i])
    print("\nKar/Zarar Durumunuz \n", hisse_adlari[i], ":", kar_zarar[i], "\n")

input("Sonlandırmak Boşluk tuşuna basın.")

# hisse linkleri:
# http://bigpara.hurriyet.com.tr/borsa/hisse-fiyatlari/sngyo-sinpas-gmyo-detay/
# http://bigpara.hurriyet.com.tr/borsa/hisse-fiyatlari/vakfn-vakif-fin-kir-detay/


# Yapılacak iyileştirmeler:
# -GUI