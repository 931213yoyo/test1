# -*- coding: utf-8 -*-
from linepy import *
from datetime import datetime
from time import sleep
import time, datetime, random ,sys, re, string, os, json, codecs, timeit
ac=LINE()
ac.log("Auth Token:"+str(cl.authToken))
def ophelpMessage():
    ophelpmessage="""
Help 幫助
Kickall 全踢
"""
    return ophelpmessage

if text.lower=='Help'or'help'or'/help':
    ac.sendMessage(to,str(ophelpMessage))
else:
    ac.sendMessage(to,"Test out")
