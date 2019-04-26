import urllib.request
import urllib.parse

url = 'https://google.com'


# GET with parameters

data = {}
data['username'] = 'admin'
data['password'] = 'admin'

url_values = urllib.parse.urlencode(data)

req = urllib.request.Request('%s?%s' % (url, url_values))

print('---------Request---------')
print('[%s] %s' % (req.get_method(), req.full_url))

response = urllib.request.urlopen(req)

print('---------Response---------')
print('[%s] %s' % (response.getcode(), response.geturl()))
print('[Info]\n%s' % (response.info()))
print('[Body]\n%s' % (response.read()))

# POST with parameters
token = 'token'
data = {
        'username': 'user',
        'password': 'password'
    }

values = urllib.parse.urlencode(data)

req = urllib.request.Request(url, data=values.encode('utf-8'))
req.add_header('Content-type', 'application/x-www-form-urlencoded')
req.add_header('Cookie', 'token=%s' % (token))


print('---------Request---------')
print('[%s] %s\n%s\n%s' % (req.get_method(), req.full_url, req.data, req.header_items()))

try:
    response = urllib.request.urlopen(req)
except urllib.error.HTTPError as err:
    print('[HTTPError] %s - %s\n%s' % (err.code, err.reason, err.headers))

print('---------Response---------')
print('[%s] %s' % (response.status, response.geturl()))
print('[Info]\n%s' % (response.info()))
print('[Body]\n%s' % (response.read()))
