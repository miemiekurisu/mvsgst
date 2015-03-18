import json
import codecs

def getdbdata(imdbid):
    APIURL =  'https://api.douban.com'
    imdbid = 'tt2397535'
    url = APIURL + '/v2/movie/imdb/%s' % imdbid
    req = urllib2.Request(url)
    reqdata = urllib2.urlopen(req)
    print reqdata.read().decode('utf-8')

def loadfile(vcfile):
    mfile = codecs.open(vcfile,'r',encoding='utf-8')
    movies = json.loads(
