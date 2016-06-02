# this file will download all photos from the 42 below flickr group 
# and assign them a random string of numbers as a filename. 
 


# get these libraries to use in python
import flickr_api 	#flickr API 
import requests 	# download things from the internet
import uuid 		# universal unique identifier 
import shutil


#set the flickr API key and secret so the flickr API will accept your query.
flickr_api.set_keys(api_key = '0f192ba0d038bbfe5d13b12f18b7109c', api_secret = '88a365e1bc9f57c4')

# import the flickr file from the flickr api
from flickr_api.api import flickr

# create (define) a function that finds urls within this stuff returned from below api call
def saveurl(stuff):
	# the photolist is the part of the stuff that is listed under the heirarchy of photos, photo. In the third level there's a list of stuff that we're calling photolist.
	# photos > photo > photolist > thing > url_o
	photolist = stuff['photos']['photo']

#def namefile(meta):
#	meta = stuff['photos']['photo']['extras']['date_taken'+'owner_name'+'url_o'+'.jpg']

#	for extras in filename:
#		 extras = meta

	for item in photolist:
		print item['url_o']
#		print item.get('date_taken')
#		print item.get('owner_name')
#		r = requests.get(item['url_o'])
#		filename = ['url_o'].split('/')[-1] 
#		filename = str(uuid.uuid4()) + ".jpg"

#		with open (filename, 'wb') as f:
#			for chunk in r.iter_content():
#				f.write(chunk)


# raw_input(item['url_o']) + '.jpg'

	# for each item in the list of photos 
	# print the item's url_o. The url_o that belongs to each item (thing).
	# then go get that item from the internet and name that object 'r'
	# create a file name with a random string for use in the next step
	# open a file with the random filename from above (make sure it is writable) and assign it the variable f.
	# for each bit of data that comes out when you send the request (r), put it in the file f and do that until it's done. 


#			for chunk in r.iter_content():
#				f.write(i)

# 		findurl = thing['url_o']


#def savephoto(findurl):
#	r = requests.get(findurl)
#	filename = str(uuid.uuid4())
#	if r.status_code == 200:
#		with open(filename, 'wb') as f:
#			for chunk in r.iter_content():
#				f.write(chunk)

# now that the function is defined above, we can get some data to give to it. 

#for each page of 100 items between 0 and 24 pages, get this stuff (photos from group + metadata), and then pass it off to the function that will find the URL
for page in range (0,24):
	# turn on the api (flickr_api.api.call_api) and ask for photos (method='flickr.groups.pools.getPhotos') from group (group_id='1156559@N21') and get metadata for each photo and name that stuff "stuff"
	stuff = flickr_api.api.call_api(
		method='flickr.groups.pools.getPhotos',
		group_id = '1156559@N21', 
		extras = 'date_taken, owner_name, url_o', 
		page = page,
		per_page = 100
		)
# now take the stuff retrieved from the api above and put it through the logic defined in the function above.
	
	saveurl(stuff)

#for thing in photolist:

#	savephoto(findurl)



