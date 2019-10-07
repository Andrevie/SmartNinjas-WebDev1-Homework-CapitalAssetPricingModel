
import math

#coding=utf-8
#Implementiere einen Rentenrechner
#Anfangskapital: 100
#Zinsen: 6%
#Laufzeit: Jahre
#Formel für die Zinseszinsrechnung: Anfangskapital * ((1+(Zinsatz/100)) ^ jeweiligen Jahre) Capital Asset Pricing Model = K(kapital) = (1+1/100)n
#Anfangskapital*math.pow(Zinsen,1)

#Lösung ist unten, muss gleich sein

#100*math.pow(1,2,3,4,5)

kapital = 100
zinssatz = 6
laufzeit = 5
jahr = 1

while jahr <= laufzeit:
    kapital = kapital * (1+(zinssatz/100))
    print(jahr,kapital)
    jahr = jahr + 1



'''
Ergebnis:
Anfangskapital:  100
Zinssatz:  6.0
Veranlagungszeitraum:  5
Kapital im Jahr 1 : 106.0
Kapital im Jahr 2 : 112.36
Kapital im Jahr 3 : 119.1016
Kapital im Jahr 4 : 126.247696
Kapital im Jahr 5 : 133.82255776
'''


