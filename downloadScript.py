#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import requests,bs4
from googletrans import Translator
from tkinter import filedialog
# from tkFileDialog import *
Text = ""
def getEnglishScript():
	linkVideo = str(input("link video:"))
	linkDown = "https://downsub.com/?url=" + linkVideo
	sourcePageDown = requests.get(linkDown)
	sourceTxt = bs4.BeautifulSoup(sourcePageDown.text,"html.parser")
	getLink  =sourceTxt.select('#show a[href]')
	linkScript = "https://downsub.com/" + getLink[1].get('href')
	file = requests.get(linkScript)
	clearScriptText = file.text
	return  clearScriptText
def saveFile(data):
	fout = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
	fout.write(data)
Text = getEnglishScript()
k = len(Text)
trans = Translator()
m = ''
fulltext =""
for i in range(0,k+5000,5000):
	m = trans.translate(Text[i:i+5000] ,dest = 'vi')
	fulltext += str(m)
	print (m.text)
saveFile(fulltext)
