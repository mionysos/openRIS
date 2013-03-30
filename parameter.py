# Parameter
#-----------


mysql_host = 			"localhost"
mysql_user = 			"XXX"
mysql_passwd = 			"YYY"
mysql_db = 			"ZZZ"



bezirke = [
		# URL-Bestandteil			Bezirk in Schoenform		Kuerzel
		["ba-treptow-koepenick",		"Treptow-Köpenick",		"tk"],
		["ba-tempelhof-schoeneberg",		"Tempelhof-Schöneberg",		"ts"],
		["ba-steglitz-zehlendorf",		"Steglitz-Zehlendorf",		"sz"],
		["ba-spandau",				"Spandau",			"sp"],
		["ba-reinickendorf",			"Reinickendorf",		"re"],
		["ba-pankow",				"Pankow",			"pa"],
		["ba-neukoelln",			"Neukölln",			"nk"],
		["ba-mitte",				"Mitte",			"mi"],
		["ba-marzahn-hellersdorf",		"Marzahn-Hellersdorf",		"mh"],
		["ba-lichtenberg",			"Lichtenberg",			"li"],
		["ba-friedrichshain-kreuzberg",		"Friedrichshain-Kreuzberg",	"fk"],
		["ba-charlottenburg-wilmersdorf",	"Charlottenburg-Wilmersdorf",	"cw"]		]
		


scripe_in_url = [
		"vo020.asp",
		"vo040.asp?showall=true", 	# Drucksachenliste: VOLFDNR, Name, Initiator, Abschl, D.-Art
		"pa021.asp", 			# aktuelle BV: Name, Art der Mitarbeit, Herkunft, seit
		"kp020.asp",
		"au010.asp", 			# Ausschuesse: Name, Mitglieder, Letzte Sitzung, Naechste Sitzung 
		"au020.asp",
		"fr010.asp", 			# Fraktionen: Name, Mitglieder, Letzte Sitzng, Naechste Sitzung
		"fr020.asp",
		"to010.asp",			# Tagesordnung eines to010.asp?SILFDNR=1058&options=4
		"ka040.asp?showall=true", 	# Kleine Anfragen: Nummer, Betreff, Eingang, Antwort   #XML-Abfrage ergab Fehler
		"si010.asp", 			# Sitzungskalender
		"si018.asp"] 			# Sitzung Suchen

