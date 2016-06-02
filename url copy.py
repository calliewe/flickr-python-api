import requests

url = 'https://farm3.staticflickr.com/2578/3930414289_f60fab010d_o.jpg'
response = requests.get(url)

f = open("/Users/calliewe/Desktop/sample.jpg", 'wb')
f.write(response.content)
f.close()

