library(rjson)
#a1 = fromJSON(paste(readLines("datatst.json")),)

c <- file("data.json", "r")
l <- readLines(c, -1L)
json <- lapply(X=l, fromJSON)
length(json)
