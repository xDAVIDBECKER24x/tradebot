from time import sleep
from analisys import MessageSender
from Login import *
from novadax import RequestClient as NovaClient
from datetime import datetime

novaClient = NovaClient(getAccessKey(), getPrivateKey())

pair = "LINK_BRL"
limitSellValue = 40
limitBuyValue = 20
flag = 1


def consultPrice(symbol):
    price = novaClient.get_ticker(symbol)
    return price


def verifyPrice(pair):
    while flag == 1:
        response = consultPrice(pair)
        sellValue = float(response['data']['bid'])
        buyValue = float(response['data']['ask'])
        currentTime = str(datetime.now().strftime("%H:%M:%S"))

        if sellValue >= limitSellValue:
            MessageSender.notifyPrice(str(sellValue))

        if buyValue <= limitBuyValue:
            MessageSender.notifyPrice(str(buyValue))

        print(currentTime + " : Sell " + str(sellValue))
        print(currentTime + " : Buy " + str(buyValue))

        sleep(1)

    return


verifyPrice(pair)
