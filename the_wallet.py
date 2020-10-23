import math
import requests
from bs4 import BeautifulSoup

#decimal range without rounding
def truncate(f, n):
    return math.floor(f * 10 ** n) / 10 ** n

r = requests.get("https://kur.doviz.com/serbest-piyasa/amerikan-dolari")

soup = BeautifulSoup(r.text, 'html.parser')

kurlar = soup.findAll("span", {"class": "value"})
kurlar = [tag.text for tag in kurlar]

str_kurlar = []

#removing dollar sign
for element in kurlar:
    str_kurlar.append(element.strip("$"))

#1.108 = 1108
int_kurlar = [sub.replace('.', '') for sub in str_kurlar]

#8,93 = 8.93
float_kurlar = [sub.replace(',' , '.') for sub in int_kurlar]

#str to float
float_kurlar = list(map(float, float_kurlar))


print('Kaç dolarınız var?')
dolar = int(input())
toplam = (dolar * (float_kurlar[1]))
print("Dolar Kuru:", float_kurlar[1], "₺")
print("Bakiyeniz:", truncate(toplam, 2), "₺")

input("Sonlandırın.")
