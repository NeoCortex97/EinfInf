def fib(n):
	global zaehler
	zaehler += 1
	if n==0 or n==1:
		return 1
	else: 
		return fib(n-1)+fib(n-2)
zaehler=0
n=input("Geben Sie n ein : ")
print(fib(int(n)))
print("Anzahl der Aufrufe der Funktion fib : "+ str(zaehler))
