#
# Obligatorisk arbeidskrav / innlevering 2, PY1010 USN
# Oppgaver 1 til 6 - (kode for oppgaver etter oppgave 1 er utkommentert, ta bort for å kjøre koden for hver oppgave)
#

### oppgave 1 ###

alder = int(input('Hvilket år er du født? ')) # ta i mot fødselsår
print("Alder etter fødselsdag i 2024:", (2024 - alder)) # regne ut og skrive alder i år til konsoll


### oppgave 2 ###

#antall_elever = int(input('\n\nSkriv inn antall elever: ')) # ta i mot antall elever som skal ha pizza
#antall_pizza = (antall_elever + 4 - 1) // 4 # regne ut antall hele pizzaer (padding og heltallsdivisjon)
#print('Antall pizzaer som må bestilles:', antall_pizza) # skrive ut svar


### oppgave 3 ###

#import numpy as np # importere numpy-pakken
#v_grad = float(input('\n\nSkriv inn gradtallet: ' )) # ta i mot gradtall
#v_rad = v_grad*np.pi/180 # gjøre omregning til radiantall
#print('Gradtallet', v_grad, 'omregnet til radianer er:', v_rad) # skriv ut resultat


### oppgave 4 ###

# oppgave 4a #

#data = { # opprette dictionary
#        "Norge": ["Oslo", 0.634],
#        "England": ["London", 8.982],
#        "Frankrike": ["Paris", 2.161],
#        "Italia": ["Roma", 2.873]
#        }

# oppgave 4b #

#land = input('Velg et land: ') # ta i mot et land som input
#print(data[land][0],'er hovedstaden i', land, 'og det er', data[land][1], 'millioner innbyggere i', data[land][0]) # skrive ut data på valgt land fra dictionary

# oppgave 4c #

#nytt_land = input('Legg til et nytt land: ') # ta i mot et nytt land
#hovedstad = input('Hovedstad: ') # ta i mot hovedstad
#innbyggere = float(input('Innbyggere i millioner: ')) # ta i mot innbyggertall

#data[nytt_land] = [hovedstad, innbyggere] # opprette nytt element i dictionary med mottatte verdier

#print(data) # skrive ut dictionary


### oppgave 5 ####

#import math

#a = input('Verdi for a: ')
#b = input('Verdi for b: ')

#def fun_aogo(a,b): #funksjon for å returnere areal og omkrets av figur, trekant med halvsirkel på toppen
        
#        a = float(a) #spesifisere at input er type float
#        b = float(b)
    
#        areal = ((((a/2)**2)*(math.pi)/2)) + (a*b)/2 #utregning av totalt areal
#        omkrets = ((math.pi)*(a/2)) + (b+(math.sqrt(a**2 + b**2))) #utregning av total omkrets
#        return areal, omkrets #returnerer resultatene i en tuple

#areal, omkrets = (fun_aogo(a,b)) #dele opp tuple i to variabler
#print(f'Areal av definert figur er {areal:.2f} og omkrets er {omkrets:.2f}.') #skrive ut resultat

### oppgave 6 ###

#import numpy as np
#import matplotlib.pyplot as plt

#x = np.linspace(-10, 10, 200) #opprette array med 200 punkter i det gitte intervallet

#y = -x**2 - 5 #definere funksjonen

#plt.plot(x, y, label='f(x) = -x^2 - 5') #plotte funksjonen i arrayet, med hjelpetekst og linjer
#plt.xlabel('x')
#plt.ylabel('f(x)')
#plt.title('Plott for f(x) = -x^2 - 5')
#plt.legend()
#plt.grid(True)
#plt.show()

