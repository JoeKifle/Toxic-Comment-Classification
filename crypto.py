from bs4 import BeautifulSoup
import requests
import os
import time

def checkPrice():
    try:
        urlElon = requests.get('https://charts.bogged.finance/?token=0xF7844CB890F4C339c497aeAb599aBDc3c874B67A')
        soupElon = BeautifulSoup(urlElon.content, 'html.parser')
        print(soupElon)
       # divElon = soupElon.find("div", {"class": "priceValue___11gHJ"})

    except:
        print("Error occured")
    

    return divElon.text, divNft.text


def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

while(True):
    priceElon, priceNft = checkPrice()
    balanceElon = float(priceElon[1:])*936230795
    balanceNFT =  float(priceNft[1:])*22305407467
    balance = balanceElon + balanceNFT
    print(balance)
    if  balance > 1500:
        notify("Investment Alert", "Your balance: {0}".format(balance))
        os.system('afplay /System/Library/Sounds/Basso.aiff')
    time.sleep(20)

