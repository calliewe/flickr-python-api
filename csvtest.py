import flickr_api 

flickr_api.set_keys(api_key = '0f192ba0d038bbfe5d13b12f18b7109c', api_secret = '88a365e1bc9f57c4')

from flickr_api.api import flickr

#group_id = '1156559@N21'
#group = group_id

file = open('42sizes.csv', 'w')

for page in range (0):

	file.write(

		flickr.groups.pools.getPhotos(
		group_id = '1156559@N21', 
		photo_id = photo_id,
#		extras = 'date_taken, owner_name, url_o', 
#		page = page,
#		per_page = 232
		)
#	) 

		flickr.photos.getSizes(
		photo_id = photo_id
		)
	)

file.close()