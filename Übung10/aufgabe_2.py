# Aufgabe 2
#
import random








# Nicht veraendern!
if __name__ == '__main__':
	# Sortiert Liste liste mittels Mergesort
	def mergesort(liste):
		if len(liste) < 2:
			return liste
	
		mitte = len(liste) // 2
		links = mergesort(liste[:mitte])
		rechts = mergesort(liste[mitte:])
		return merge(links,rechts)

	# mische aufsteigend sortierte Listen links und rechts zu einer aufsteigend sortierten Liste
	def merge(links, rechts):
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



	n = 10
	m = 20
	r = 100
	
	# Ergebniskontrolle fuer Vergleiche
	# Erzeugt n Listen zufaelliger Laenge (von 0 bis m-1) mit zufaelligen Eintraegen (von 0 bis r-1). 


	Listen = [ Intliste([random.choice(range(r)) for j in range(random.choice(range(m)))]) for i in range(n) ]
	for liste in Listen:
		print(liste)

	Sortiert = mergesort(Listen)
	
	for liste in Sortiert:
		print(liste)

# Ihren globalen Testcode koennen Sie hier platzieren:


