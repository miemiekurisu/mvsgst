import codecs
import json
import movie
import datetime

def loadfile(file_path):
    sttm = datetime.datetime.now()
    mfile = codecs.open(file_path,'r',encoding='utf-8')
    movies = []
    j=0
    for i in mfile.readlines():
        j+=1
        i = i.replace('\r','')
        i = i.replace('\n','')
        i = i.replace('\t','')
        try:
            movies.append(movie.movie(json.loads(i)))
        except ValueError:
            print 'Find error, No. is: '+ str(j)
            continue
    edtm = datetime.datetime.now()
    print (edtm-sttm).seconds
    return movies

def loadset(mvlist,neededname):
    execstr = "neededsets |= set(i.%s)" % neededname
    neededsets = set([])
    for i in mvlist:
        exec  execstr 
    return list(neededsets)

#mvs = loadfile('data1.json')
#tp=loadset(mvs,'types')
#actors=loadset(mvs,'actors')


