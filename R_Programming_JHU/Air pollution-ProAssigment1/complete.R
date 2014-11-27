setwd ("/Users/lisa/Desktop/R programming")

complete <- function(directory, id = 1:332) {
  
    directory <- ("./specdata/")
    
    all_files <- list.files(directory)
    paths <- paste(directory, all_files, sep="")
   
    
    
    l <- length (id)
    comp_num <- integer (l)
    j <- 0
    
    for (i in id) {
      dataset <- read.csv(paths[i], header=TRUE, sep=",")
      j <- j+1
      comp_num[j] <- sum (complete.cases(dataset))
      }
      
    dataframe <- data.frame (id = id, nobs = comp_num)
    dataframe
}