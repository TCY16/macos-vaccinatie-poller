import os
import time

year = "1990"
path = "~/" # Path to the location of the greensquare.png

query = "curl https://user-api.coronatest.nl/vaccinatie/programma/bepaalbaar/"+ year +"/NEE/NEE"

print("watching...")
while(True):
	response = os.popen(query).read()

	if "true" in response:
		print("JE MAG EEN VACCINATIE!")
		os.system("open "+ path +"greensquare.png")
		break

	time.sleep(30)
