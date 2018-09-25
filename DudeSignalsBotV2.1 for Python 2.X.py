# coding=utf-8
import threading
import math
import datetime
from time import sleep
from binance.client import Client
import numpy as np
import os
apikey =""
apisecret = ""

print ("Welcome to DudeSignals.com stop/takeprofit bot!\n")


def getdata():
        f = open("login.txt", "r+")
        message=f.read()
        message = message.split('\n')
        f.close()
        return message
        
if os.path.exists("login.txt"):
        try:
                message = getdata()
                apikey =message[0]
                apisecret = message[1]
        except Exception as e:
                print("Your API caused an error. Please run the program again.")
                os.remove("login.txt")
                apikey= raw_input("Type your apikey\n")
                apisecret= raw_input("Type your apisecret\n")
                f = open("login.txt", "w+")
                f.write(apikey+"\n"+apisecret)
                f.close()
                
                
                
else:
        apikey= raw_input("Type your apikey\n")
        apisecret= raw_input("Type your apisecret\n")
        f = open("login.txt", "w+")
        f.write(apikey+"\n"+apisecret)
        f.close()
        

        



client = Client(apikey,apisecret)


def programa(symbol, targetact, targetlimit, stopact, stoplimit, quantity):        
   
        
        sold = 0
        last = 0
        print ("Trade activated! Keep this window open until your order gets activated.\n")

        while (sold ==0):
                coin1 = client.get_ticker(symbol=symbol)        
                

                
                
                last = float(coin1['lastPrice'])
                
                
                if last>=targetact:                        
                        client.order_limit_sell(symbol = symbol, quantity = quantity, price = targetlimit)
                        print ("Target order Activated for "+symbol+"\n")
                        sold =1
                if last<=stopact:                        
                        client.order_limit_sell(symbol = symbol, quantity = quantity, price = targetlimit)
                        print ("Stop order Activated for "+symbol+"\n")
                        sold =1

        print ("Thanks for using DudeSignals bot.\nObservation: If you want to close this trade setup you must close the bot and if you want to open a new trade go ahead :)\n")


z = 0
while (z ==0):
        sleep(1)
        flag = input("Type '1' and press enter to open a new trade!\n")
        
        if flag==1:
                
                symbol= raw_input("Type coin pair(Example: ETCBTC):\n")
                symbol= symbol.upper()
                targetact= input("Type your TARGET activation price:\n")
                targetlimit= input("Type your TARGET limit order price:\n")
                stopact= input("Type your STOP activation price:\n")
                stoplimit= input("Type your STOP limit order price:\n")
                quantity = input("Type how much units of the coin you want to sell:\n")
                t = threading.Thread(target=programa,args=(symbol, targetact, targetlimit, stopact,stoplimit , quantity))
                t.setDaemon(True)
                t.start()
                sleep(1)
                
                
        else:
                print("Invalid option.")
