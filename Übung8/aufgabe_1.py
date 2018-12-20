# Aufgabe 1
#

def bisection2(L,e): # Diese Zeile duerfen Sie nicht veraendern
	def bisection_hilfe(L, e, links, rechts):
		if links >= rechts:
			# print("Links({}) >= rechts({})".format(links, rechts))
			return links if links == rechts and L[links] == e else -1
		mitte = (links + rechts) // 2
		if L[mitte] == e:
			# print("Mitte({}) = e({}) | {} {} {}".format(L[mitte], e, links, mitte, rechts))
			return mitte
		elif L[mitte] > e:
			# print("Mitte({}) > e({}) | {} {} {}".format(L[mitte], e, links, mitte, rechts))
			return bisection_hilfe(L,e,links,mitte-1)
		else:
			# print("mitte({}) < e({}) | {} {} {}".format(L[mitte], e, links, mitte, rechts))
			return bisection_hilfe(L,e,mitte+1,rechts)
	if len(L) == 0:
		# print("array leer")
		return -1
	else:
		# print("suche . . .")
		return bisection_hilfe(L,e,0,len(L)-1)










# Nicht veraendern!
if __name__ == '__main__':
# Ihren globalen Testcode koennen Sie hier platzieren:
	array = [1, 2, 3, 4, 5, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]
	for e in array:
		print(str(bisection2(array, e)))
