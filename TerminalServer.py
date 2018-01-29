from Analyze import analyze

with open("2016.html", 'w') as f:
	f.write(analyze(2016))

with open("2017.html", 'w') as f:
	f.write(analyze(2017))