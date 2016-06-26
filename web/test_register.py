import urllib
import json

coord_in = (46.616162, 14.313515)
coord_out = (46.711313, 14.265178)

URL_IN = 'http://wth.ivoras.net:8000/api/beacon/register'
URL_OUT = 'http://wth.ivoras.net:8000/api/beacon/unregister'

u1 = urllib.urlopen(URL_IN, 'beacon_name=BUS-1070&profile_id=1&lat=%0.6f&lng=%0.6f' % coord_in)
resp = u1.read()
print resp
rdata = json.loads(resp)

u2 = urllib.urlopen(URL_OUT, 'id=%d&lat=%0.6f&lng=%0.6f' % (rdata['id'], coord_out[0], coord_out[1]))
print u2.read()

