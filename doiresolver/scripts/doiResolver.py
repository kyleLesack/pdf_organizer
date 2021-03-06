import argparse, urllib2, json
import requests


parser = argparse.ArgumentParser(description='Resolve DOIs from CrossRef')
parser.add_argument('DOI', help='DOI number to be queried')

args = parser.parse_args()
print args.DOI

url = "http://dx.doi.org/" + args.DOI
bibtexHeaders = {'Accept': 'application/x-bibtex'}
jsonHeaders = {'Accept' : 'application/vnd.citationstyles.csl+json'}

req = urllib2.Request(url)

try:
	urllib2.urlopen(req)

except Exception as e:
	print e.code
	print e.read()
else:
	rbibtex = requests.get(url,headers=bibtexHeaders)
	print rbibtex
	print rbibtex.text	
	rjson = requests.get(url,headers=jsonHeaders)
	print rjson
	print rjson.text
	print rjson.headers
	#print r.text
	
	
