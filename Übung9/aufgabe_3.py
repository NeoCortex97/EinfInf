# Aufgabe 3
#

import random
import time



def merge(links, rechts):
	global vergleiche
	resultat = []
	i,j = 0,0

	while i < len(links) and j < len(rechts):
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


def mergesort(liste):
	if len(liste) < 2:
		return liste
	
	mitte = len(liste) // 2
	links = mergesort(liste[:mitte])
	rechts = mergesort(liste[mitte:])
	return merge(links,rechts)


def bubblesort(liste):
	for i in range(len(liste)):
		sortiert = True
		for j in range(0,len(liste)-i-1):
			if liste[j] > liste[j+1]:
				liste[j], liste[j+1] = liste[j+1], liste[j]
				sortiert = False
		if sortiert:
			break
	return liste

def qsort(liste):  
	global vergleiche
	linke=[]
	rechte=[]
	if len(liste) <= 1:
		return liste

	pivot = 0 

	for i in range(len(liste)):
		if i!= pivot:
			if liste[i] < liste[pivot]:
				linke.append(liste[i])
			else:
				rechte.append(liste[i])

	return qsort(linke)+liste[pivot:pivot+1]+qsort(rechte)


# Implementieren Sie diese Funktion
def radixsort(liste, stelligkeit, tiefe):
	if stelligkeit <= tiefe:
		RADIX = 10
		maxLength = False
		tmp = -1
		while not maxLength:
			maxLength = True
			buckets = [list() for _ in range(RADIX)]
			for i in liste:
				tmp = i / (stelligkeit * 10)
				buckets[int(tmp % RADIX)].append(i)
				if maxLength and tmp > 0:
					maxLength = False
			a = 0
			for b in range(RADIX):
				buck = buckets[b]
				for i in buck:
					liste[a] = i
					a += 1
	return liste







# Nicht veraendern!
if __name__ == '__main__':


	s = 10 # Veraendern Sie diese drei Werte fuer Aufgabenteil b)
	p = 6  #
	t = 6  #

	liste = random.sample(range(10 ** s, 10 ** (s +1)  ), 10 ** p)
	kopie = liste[:]
	kopie2 = liste[:]

	t0 = time.process_time()
	liste = radixsort(liste, 0, t-1)
	liste = bubblesort(liste)
	t1 = time.process_time() - t0
	print(f"Radixsort + Bubblesort: {t1} Sekunden")
	

	t0 = time.process_time()
	kopie = mergesort(kopie)
	t1 = time.process_time() - t0
	print(f"Mergesort: {t1} Sekunden")

	t0 = time.process_time()
	kopie2 = qsort(kopie2)
	t1 = time.process_time() - t0
	print(f"Quicksort: {t1} Sekunden")

# Ihren globalen Testcode koennen Sie hier platzieren:

