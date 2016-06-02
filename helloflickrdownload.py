import flickr_api 
import urllib2 

flickr_api.set_keys(api_key = '0f192ba0d038bbfe5d13b12f18b7109c', api_secret = '88a365e1bc9f57c4')

from flickr_api.api import flickr

group_id = '1156559@N21'
group = group_id

##file = open('flickr42.csv', 'w')

url = URL

file_name = url.split('/')[-1]
u = urllib2.urlopen(url)
f = open(file_name, 'wb')

for page in range (0):

##	file.write(

		flickr.groups.pools.getPhotos(
		group_id = '1156559@N21', 
		photo_id = photo_id,
#		extras = 'date_taken, owner_name, url_o', 
#		page = page,
#		per_page = 232
#		)
#	) 

		for photo_id in group_id 

	flickr.photos.getSizes(
		photo_id = photo_id
		)

f.close()


#file.close()





#flickr = flickr_api

#print flickr_api.Person.findByUser Name('callums73')

#print flickr.photos_search(tags = "e-waste")

#flickr.groups.pools.getPhotos