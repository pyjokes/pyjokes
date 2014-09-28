import json
import urllib2
from random import choice

def get_chuck_nerd_jokes():
	url = 'http://api.icndb.com/jokes/random?limitTo=[nerdy]'
	response = urllib2.urlopen(url)
	data = json.load(response)  
	d = data['value'] 
	return d['joke']

def main():
	print get_chuck_nerd_jokes()

if __name__ == '__main__':
    main()
