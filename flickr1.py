import flickr_api 

flickr_api.set_keys(api_key = '0f192ba0d038bbfe5d13b12f18b7109c', api_secret = '88a365e1bc9f57c4')

from flickr_api.api import flickr

# create (define) a function that finds urls within this stuff returned from below api call
def findurl(stuff):
	# the photolist is the part of the stuff that is listed under the heirarchy of photos, photo. In the third level there's a list of stuff that we're calling photolist.
	# photos > photo > photolist > thing > url_o
	photolist = stuff['photos']['photo']

	# for each item in the list of photos print the thing's url_o. The url_o that belongs to each item (thing).

	for thing in photolist:
		print thing['url_o']
		print thing.get('datetimeoriginal')
		print thing.get('ownername')

# now that the function is defined above, we can get some data to give to it. 

#for each page of 100 items between 0 and 24 pages, get this stuff (photos from group + metadata), and then pass it off to the function that will find the URL
for page in range (0,24):
	# turn on the api (flickr_api.api.call_api) and ask for photos (method='flickr.groups.pools.getPhotos') from group (group_id='1156559@N21') and get metadata for each photo and name that stuff "stuff"
	stuff = flickr_api.api.call_api(
		method='flickr.groups.pools.getPhotos',
		group_id = '1156559@N21', 
		extras = 'datetimeoriginal, ownername, url_o', 
		page = page,
		per_page = 100
		)
# now take the stuff retrieved from the api above and put it through the logic defined in the function above.
	findurl(stuff)



	




