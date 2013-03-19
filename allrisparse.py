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
        spans = soup.find_all('span')
        
        i = 0

        moegebeschliessen = "Die Bezirksverordnetenversammlung Treptow-Köpenick von Berlin möge beschließen:"
        antragtext = ""
        
        begruendungbool = False
        begruendung = "Begründung:"
        begruendungstext = ""
        
        ueberweisungstext = ""
        ueberweisung =  ""
        ueberweisungsbool = False
        
        drsbool = False
        
        ausschussbeschluss = ""
        ausschussbeschlussbool = False
        
        beschluss = ""
        beschlussbool = False
        
        #for span in spans:
        #    print span
        
        for span in spans:
                print span
                #print span.contents[0]
                text = unicode(span.contents[0])
                
                if text[0:75] == u"Die Bezirksverordnetenversammlung Treptow-Köpenick von Berlin beschließt:" or beschlussbool == True:
                        beschlussbool = True
                        beschluss = beschluss + text
                
                elif text == u"Der Ausschuss für " or ausschussbeschlussbool == True:
                        ausschussbeschlussbool = True
                        if text[0:8] == u"<a href=":
                                ausschussbeschluss = ausschussbeschluss + unicode(span.a.contents[0])
                        else:
                                ausschussbeschluss = ausschussbeschluss + text
                        
                elif text == u"Drs. VII/" or drsbool == True:
                        drsbool = True
                
                elif text[0:8] == u"<a href=":
                        #print span.a.contents[0]
                        ueberweisungstext = ueberweisungstext + unicode(span.a.contents[0])
                
                elif ueberweisungsbool == True:
                        ueberweisungstext = ueberweisungstext + unicode(span.contents[0])                  
                
                elif text[0:26] == u"In der Sitzung der BVV am ":
                        ueberweisungsbool = True
                        ueberweisungstext = ueberweisungstext + unicode(span.contents[0])
                        
                        
                elif begruendungbool == True and ueberweisungsbool == False:
                        begruendungstext = begruendungstext + unicode(span.contents[0])           
                
                elif text == u"ndung: ":
                        begruendungbool = True
                        span.decompose()
                               
                elif text == u"Begründung: ":
                        begruendungbool = True
                        
                elif span.contents[0] == u"Begründung:":
                        begruendungbool = True
                
                #if span.contents[0] == u"In der Sitzung der BVV am ":
                        #ueberweisungsbool = True
                        #ueberweisungstext = ueberweisungstext + span.contents[0]
                        
                elif i>7 and text != u" " and begruendungbool == False and ueberweisungsbool == False:
                        antragtext = antragtext + unicode(span.contents[0])                
                i += 1
                
                        
                        
        print moegebeschliessen
        print antragtext
        print begruendung
        print begruendungstext
        print ueberweisungstext
        #print drstext
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

        