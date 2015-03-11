library(RJSONIO)
#a1 = fromJSON(paste(readLines("datatst.json")),)

system.time(
c <- file("data.json", "r"))
system.time(l <- readLines(c, -1L))
#typelst(l)
system.time(json <- lapply(X=l, fromJSON))
length(json)
# 
# typelst <- 
# function(l){
#   for (i in 1:length(l)){
#     print(i)
#     tst <-  fromJSON(l[i])
#   }
# }

tplst <- function(json){
  test<-c()
  for(i in 1:length(json)){
    if(length(json[[i]]$types)>0){
      if(length(json[[i]]$types)>=3){print(json[[i]]$types)}
     test[i]<-json[[i]]$types}
    else{test[i]=NA}
  }
  return(test)
}

a <- 

