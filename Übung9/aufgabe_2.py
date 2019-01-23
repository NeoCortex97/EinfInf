 	# Aufgabe 2
#
import math
import sys
import random
import time

# Sortiert Liste liste mittels Insertionsort
def inssort(liste):
	global vergleiche
	trenner = 0
	while trenner != len(liste):
		for i in range(trenner+1,len(liste)):
			vergleiche += 1
			if liste[i] < liste[trenner]:
				liste[trenner], liste[i] = liste[i], liste[trenner]
		trenner += 1
	return liste


# mische aufsteigend sortierte Listen links und rechts zu einer aufsteigend sortierten Liste
def merge(links, rechts):
	global vergleiche
	resultat = []
	i,j = 0,0

	while i < len(links) and j < len(rechts):
		vergleiche += 1
		if links[i] < rechts[j]:
			resultat.append(links[i])
			i += 1
		else:
			resultat.append(rechts[j])
			j += 1

	while i < len(links):
		resultat.append(links[i])
		i+= 1

	while j < len(rechts):
		resultat.append(rechts[j])
		j += 1

	return resultat

# Sortiert Liste liste mittels Mergesort
def mergesort(liste):
	if len(liste) < 2:
		return liste
	
	mitte = len(liste) // 2
	links = mergesort(liste[:mitte])
	rechts = mergesort(liste[mitte:])
	return merge(links,rechts)

# Sortiere Liste liste mittels Quicksort
def qsort(liste):  
	global vergleiche
	linke=[]
	rechte=[]
	if len(liste) <= 1:
		return liste

	pivot = 0 

	for i in range(len(liste)):
		if i!= pivot:
			vergleiche += 1
			if liste[i] < liste[pivot]:
				linke.append(liste[i])
			else:
				rechte.append(liste[i])

	return qsort(linke)+liste[pivot:pivot+1]+qsort(rechte)



def qsort_ma3(liste):  
	global vergleiche
	


def qsort_cutoff(liste):  
	global vergleiche



def qsort_intro(liste):  
	global vergleiche
	


def qsort_cutoff_ma3(liste):  
	global vergleiche



def qsort_random(liste):  
	global vergleiche



	
def teste(liste, funktion): # Nicht veraendern!
	global vergleiche
	L = liste[0][:]
	vergleiche = 0
	t0 = time.process_time()
	L1 = funktion[0](L)
	t1 = time.process_time() - t0
	L2 = sorted(L1)
	if L2 != L1:
		print(f"Funktion {funktion[1]} sortiert nicht richtig")
	
	print(f"{funktion[1]}:  Zeit: {str(t1)[:5]} Sekunden, Vergleiche: {vergleiche} ")


# Nicht veraendern!
if __name__ == '__main__':
	sys.setrecursionlimit(20000)
	n = 5000  # Diesen Wert können Sie zum Testen veraendern

	listen = [ ([i for i in range(n)], "Aufsteigende Liste" ), ([ n-i for i in range(n) ],"Absteigende Liste" ),] + [  (random.sample(range(n),n), str(i)+"-te zufaellige Liste")   for i in range(5)  ]
	funktionen = [(inssort, "Insertionsort"+" "*11), (mergesort, "Mergesort"+" "*15), (qsort,"Quicksort" + " "*15), (qsort_intro,"Introsort" + " " *15), (qsort_cutoff,"Quicksort mit Cutoff"+ " "*4), (qsort_ma3,"Quicksort mit Ma3"+" "*7 ), (qsort_cutoff_ma3, "Quicksort mit Cutoff/Ma3"), (qsort_random, "Quicksort mit zuf. Pivot")]
	for liste in listen:
		print(f"Teste nun diese Liste: {liste[1]}")
		for funktion in funktionen:	
			teste(liste, funktion) 
		print("\n")
		
		
# Ihren globalen Testcode koennen Sie hier platzieren:



