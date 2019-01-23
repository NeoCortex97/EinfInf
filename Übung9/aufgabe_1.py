# Aufgabe 1
#

def rucksack(schaetze,maxgewicht): 
	akku = 0
	value = 0
	result = list()
	for item in schaetze:
		if item[0] <= maxgewicht - akku:
			result.append(True)
			akku += item[0]
			value += item[1]
		else:
			result.append(False)
	return result

				
			









# Nicht veraendern!
if __name__ == '__main__':

	beispiel1 = [(2,3),(3,4),(5,6)]
	beispiel2 = [(4,10),(3,1),(5,13),(5,5),(7,21)]
	loesung1 = [True, True, False]
	loesung2 = [True, False, True, False, False]
	if rucksack(beispiel1, 5) != loesung1:
		print(f"Ihre Methode funktioniert nicht fuer Beispiel 1 - ist {rucksack(beispiel1, 5)}, soll aber {loesung1} sein.")
	if rucksack(beispiel2, 10) != loesung2:
		print(f"Ihre Methode funktioniert nicht fuer Beispiel 2 - ist {rucksack(beispiel2, 10)}, soll aber {loesung2} sein.")

# Ihren globalen Testcode koennen Sie hier platzieren:
