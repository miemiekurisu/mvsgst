import codecs
import json
import movie

def loadfile(file_path):
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
    return movies

mvs = loadfile('data1.json')
tp=set([])
for i in mvs:
    tp |= set(i.types)
actors=set([])
for i in mvs:
    actors |= set(i.actors)


