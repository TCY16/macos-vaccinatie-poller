import os

year = "1990"
path = "~/" # Path to the location of the greensquare.png

query = "curl https://user-api.coronatest.nl/vaccinatie/programma/bepaalbaar/"+ year +"/NEE/NEE"

response = os.popen(query).read()

print("watching...")
while(True):
	if "true" in response:
		print("JE MAG EEN VACCINATIE!")
		os.system("open "+ path +"greensquare.png")
		break
