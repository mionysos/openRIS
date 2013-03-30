import elemente.py

bezirk_ordinal = 5  #Pankow
bezirk = bezirke[5]


# Synchronisierung der DB mit Inhalten im Web

def hole_neue_drucksachen(bezirk):
	neue_drucksachen = []
	volfdnr_max = hoechste_volfdnr_in_db(bezirk)	

	drucksachenliste_komplett = drucksachenliste_komplett(bezirk)
	#		VOLFDNR, 	Name, 															Initiator, 	Abschl, 	D.-Art
	# 	[	[3621,		"1894/XVIII Muss Jugendarbeit in Neukölln eingestellt werden?","Grüne",		13.07.2011,	"Große Anfrage"], 	
	#		[3620 		...	],...]           #geeignetes Format für Datum finden
	for i in drucksachenliste_komplett:
		if i[0] > volfdnr_max:
			neue_drucksachen.append(i)
	print str(len(neue_drucksachen))+" neue Drucksachen im Web entdeckt"
	return neue_drucksachen

def schreibe_in_drucksachen_zeilen(neue_drucksachen, bezirk)
	import MySQLdb
	conn = MySQLdb.connect (host = mysql_host,user = mysql_user,passwd = mysql_passwd,db = mysql_db,charset = "utf8", use_unicode = True)
	cursor = conn.cursor()

	for i in neue_drucksachen:
		executeCommand = 	"INSERT INTO drucksachen_"+	bezirk[2]	+" "
		executeCommand += 	"(volfdnr,name,initiator,abschl,d_art)" + " VALUES (" + i[0]+"," + i[2]+"," + i[3]+"," + i[4]+"," + i[5]+")"	
		cursor.execute(executeCommand)
		cursor.close ()
	conn.close ()	
	print str(len(neue_drucksachen))+" neue Drucksachen in DB geschrieben ("+

def drucksachenliste_komplett(bezirk):
	link = "http://www.berlin.de/"+bezirk[0]+"/bvv-online/vo040.asp?showall=true"
	# ...
	# parsing nach *Cornelius***
#-->[[volfdnr0,name0,initiator0,abschl0,d_art0],[volfdnr1,name1,initiator1,abschl1,d_art1],[volfdnr2,name2,initiator2,abschl2,d_art2]...]
	return drucksachenliste_komplett
	
	
def hoechste_volfdnr_in_db(bezirk):
