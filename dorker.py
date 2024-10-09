from googlesearch import search
import sys

from pyfiglet import Figlet

class couleur:
		  	OK = '\033[91m' #GREEN
		  	
		  		

figlet = Figlet(font='slant')
result = figlet.renderText("jhonson")
dak= figlet.renderText("jon")
print(couleur.OK+result)
print(couleur.OK+dak)
try :
	a = sys.argv[1]
	query = a
	for dork in search(query, tld="co.in", num=100, stop=1000, pause=2):
		  		if '=' in dork :
		  			class couleur:
		  				OK = '\033[92m' #GREE
		  				print(couleur.OK+dork)


except :
	class couleur:
		OK = '\033[92m' #GREEN
	
	print(couleur.OK+'python dorker.py target')
