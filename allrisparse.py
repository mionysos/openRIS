#!/usr/bin/env python
# coding: utf8
#fuy0u4llr15

import urllib2
from bs4 import BeautifulSoup

#errechnet die DRS der 7. Legislatur von T-K
#beoetigt die DRS-Nr.
#gibt die laufende Nr. der DRS im ALLRIS zurück
def drsrechner(drs):
        drsnr = 4099 + drs
        return drsnr

#holt sich den Antrag vom ALLRIS T-K
#benoetigt die laufenden DRS-Nr. im ALLRIS
def antragholen(drsnr):
        response = urllib2.urlopen('http://www.berlin.de/ba-treptow-koepenick/bvv-online/vo020.asp?VOLFDNR=' + str(drsnr))
        print 'http://www.berlin.de/ba-treptow-koepenick/bvv-online/vo020.asp?VOLFDNR=' + str(drsnr)
        html = response.read()
        return html


#HTML (Antrag) wird geparst
#benötigt das HTML
def antragparsen(html):
        soup = BeautifulSoup(html)
        scripts = soup.find_all('script')
        for script in scripts:
            script.decompose()        
        return soup


#parst den Antrag nach Antragstext und Begründug
#benoetigt die HTML datei der DRS
def antragstext(soup):
        antragtext = ""
        begruendungstext = ""
        ueberweisungstext = ""
        antragtext = ""
        ausschussbeschluss = ""
        beschluss = ""
        
        text = ""
        spans = soup.find_all('span')
        for span in spans:
            #print span
            #print unicode(span.contents[0])
            text = text + unicode(span.contents[0])
            a = span.find('a')
            if a != None:
                #print "!!!!!!!!!"
                text = text + unicode(a.contents[0])
                try:
                        text = text + unicode(span.contents[2])
                except:
                        pass
            #print text
        link = True
        while link == True:
                if "<a href=" in text:
                        linkanfang = text.find(u"<a href=")
                        linkende = text.find(u"</a>")
                        text = text[:linkanfang] + text[linkende+4:]
                else:
                        link = False
        #print text
        antraganfang = text.find(u"Die Bezirksverordnetenversammlung Treptow-Köpenick von Berlin möge beschließen:")
        antragende = text.find(u"Begründung:")
        antragtext = text[antraganfang:antragende]
        text = text[antragende:]
        #print text
        
        begruendunganfag = text.find(u"Begründung:")
        begruendungende = text.find(u"In der Sitzung der BVV am")
        #print begruendunganfag
        #print begruendungende
        begruendungstext = text[begruendunganfag:begruendungende]
        text = text[begruendungende:]
        #print text
        
        ueberweisunganfang = text.find(u"In der Sitzung der BVV am")
        ueberweisungende = text.find(u"überwiesen:") + len("überwiesen:")
        #print ueberweisunganfang
        #print ueberweisungende
        ueberweisungstext = text[ueberweisunganfang:ueberweisungende]
        text = text[ueberweisungende:]
        #print text
              
        ausschussanfang = text.find(u"Der Ausschuss für ")
        ausschussende = text.find(u"Die Bezirksverordnetenversammlung Treptow-Köpenick von Berlin beschließt:")
        #print ausschussanfang
        #print ausschussende
        ausschussbeschluss = text[ausschussanfang:ausschussende]
        text = text[ausschussende:]
        #print text        
        
        beschlussanfang = text.find(u"Die Bezirksverordnetenversammlung Treptow-Köpenick von Berlin beschließt:")
        #print ausschussanfang
        #print ausschussende
        beschluss = text[beschlussanfang:]
        #print text                        
                        
                        
       
        print antragtext
        print begruendungstext
        print ueberweisungstext
        print antragtext
        print ausschussbeschluss
        print beschluss

#parst den Antrag nach dem Titel
#benoetigt die HTML datei der DRS        
def title(soup):
        titel = ""
        i = 0
        tds = soup.find_all("td")
        for td in tds:
            if i==7 :
                title = td.contents[1]
            i += 1
        return title[2:]

def initiator(soup):
        initiator =  ""
        i = 0
        
        inis = soup.find_all("td")
        for ini in inis:
            if i == 16: 
                initiator = ini.contents[0]
            i += 1
        print initiator
        return initiator

        