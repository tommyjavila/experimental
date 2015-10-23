
import MySQLdb
import urllib2
import json

# goal: get bitcoin data and store in a database

def printResults(data):
    # Use the json module to load the string data into a dictionary
    theJSON = json.loads(data)

    print theJSON['time']['updated']
    print theJSON['bpi']['USD']['rate']
    print theJSON['bpi']['EUR']['rate']
    print theJSON['time']['updated']


# define the database
db = MySQLdb.connect(host="localhost", user="root", passwd="FIXME", db="bitcoin_data")


# create a cursor for the select
cur = db.cursor()

urlData = "https://api.coindesk.com/v1/bpi/currentprice.json"

print "==================================================="

webUrl = urllib2.urlopen(urlData)
if (webUrl.getcode() == 200):
    data = webUrl.read()
    theJSON = json.loads(data)
    printResults (data)
else:
    print "Error retrieving data from api.coindesk.com"

print "==================================================="


# store the data
cur.execute("""INSERT INTO rates (usd_rate, eur_rate) VALUES (%s, %s)""",  (theJSON['bpi']['USD']['rate'], theJSON['bpi']['EUR']['rate']))

# close the cursor
cur.close()

# close the connection
db.close()
