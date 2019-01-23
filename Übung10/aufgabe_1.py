class Mensch(object):
	
	def __init__(self, name, weiblich):
		self.name = name
		self.weiblich = weiblich

	def get_name(self):
		return self.name	

	def get_weiblich(self):
		return self.weiblich

	def set_name(self, neuername):
		self.name = neuername
	



	

# Nicht veraendern!
if __name__ == '__main__':


# Loesen Sie Aufgabenteil g) hier:
	
	

# Diesen Teil duerfen Sie nicht veraendern

	if not (Laureline.get_name() == "Laureline" and Canine.get_name() == "Canine"):
		print("Fehler: Gallierinnen falsch benannt")

	if not (Praefix.get_name() == "Praefix"  and Postfix.get_name() == "Postfix" ):
		print("Fehler: Gallier falsch benannt")

	if not (Salta.get_name() == "Salta" and Ushuaia.get_name() == "Ushuaia"):
		print("Fehler: Roemerinnen falsch benannt")

	if not (Primus.get_name() == "Primus" and Quintus.get_name() == "Quintus"):
		print("Fehler: Roemer falsch benannt")

	if not (Roemer.imperator == Salta):
		print("Fehler: Imperator falsch")
	
	Primus.werde_imperator()

	if not Roemer.imperator == Primus:
		print("Fehler: Thronfolge kaputt")


	Laureline.set_name("Geraldine")
	Canine.set_name("Paul")
	Praefix.set_name("Unix")
	Infix.set_name("Append")
	Mendoza.set_name("Catamarca")
	Ushuaia.set_name("Viedm")
	Primus.set_name("Airbus")
	Secundus.set_name("Autob")

	if not (Laureline.get_name() == "Geraldine" and Canine.get_name() == "Pauline" and Praefix.get_name() == "Unix" and Infix.get_name() == "Appendix" and Mendoza.get_name() == "Catamarca" and Ushuaia.get_name() == "Viedma" and Primus.get_name() == "Airbus"  and Secundus.get_name() == "Autobus" ):
		print("Fehler: Namensaenderung funktioniert nicht korrekt")


	Laureline.set_name("Laureline")
	Canine.set_name("Canine")
	Praefix.set_name("Praefix")
	Infix.set_name("Infix")
	Mendoza.set_name("Mendoza")
	Ushuaia.set_name("Ushuaia")
	Primus.set_name("Primus")
	Secundus.set_name("Secundus")
	
	if not (Oelixdorf.get_barde() == Praefix and Oelixdorf.get_druide() == Laureline and Oelixdorf.get_bewohner() == {Apfelsine, Praefix, Laureline} ):
		print("Fehler: Dorf falsch erstellt")

	if not (Bekdorf.get_barde() == Canine and Bekdorf.get_druide() == Infix and Bekdorf.get_bewohner() == {Laureline, Postfix, Infix, Canine} ):
		print("Fehler: Dorf falsch erstellt")

	if not (Hispana.get_zenturio() == Salta and Hispana.soldaten == {Quintus, Quartus, Tertius} ):
		print("Fehler: Legion falsch")


	Hispana.rekrutiere(Secundus)
	Hispana.rekrutiere(Ushuaia)	
	Hispana.pensioniere(Tertius)
	Hispana.pensioniere(Tertius)
	Hispana.rekrutiere(Salta)
	
	if not (Hispana.soldaten == {Secundus, Quartus, Quintus}):
		print("Fehler: Legion arbeitet falsch")


	wettkampf(Oelixdorf, Hispana)

	if not ((Secundus.wie_oft_verloren() == 1) and (Salta.wie_oft_verloren() == 1) and (Laureline.get_wildschweine() == 1) and (Canine.get_wildschweine() == 0)):
		print("Fehler: Wettkampf funktioniert nicht")
	
	Bekdorf.set_barde(Laureline)
	Hispana.rekrutiere(Primus)
	wettkampf(Bekdorf, Hispana)
	if not (Secundus.wie_oft_verloren() == 2 and Primus.wie_oft_verloren() == 1 and Laureline.get_wildschweine() == 1 and Canine.get_wildschweine() == 1):
		print("Fehler: Wettkampf funktioniert nicht richtig")


# Ihre Ausgabe soll in etwa folgendes Format haben:
# Gallier Apfelsine misst sich mit Roemer Quintus.
# Gallier Praefix misst sich mit Roemer Quartus.
# Gallier Apfelsine misst sich mit Roemer Secundus.
# Gallier Praefix misst sich mit Zenturio Salta.
# Gallier Laureline misst sich mit Roemer Primus.
# Gallier Postfix misst sich mit Roemer Secundus.
# Gallier Canine misst sich mit Roemer Quartus.
# Gallier Laureline misst sich mit Roemer Quintus.
# Gallier Postfix misst sich mit Zenturio Salta.




	

			

			
