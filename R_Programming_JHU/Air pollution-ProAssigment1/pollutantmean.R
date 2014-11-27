setwd ("/Users/lisa/Desktop/R programming")

pollutantmean <- function(directory, pollutant, id = 1:332) {
  
 
     directory <- ("./specdata/")
  
     all_files <- list.files(directory)
     paths <- paste(directory, all_files, sep="")
  
     
     
     means <- vector()
     
     
     for (i in id) {
        dataset <- read.csv(paths[i], header=TRUE, sep=",")
        removedNA <- dataset[!is.na(dataset[, pollutant]), pollutant]
        means <- c(means, removedNA)
     }
  
     result <- mean(means)
  
     round (result, 3)
}



