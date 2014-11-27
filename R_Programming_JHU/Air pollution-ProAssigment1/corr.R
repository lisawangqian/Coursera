setwd ("/Users/lisa/Desktop/R programming")

corr <- function(directory, threshold = 0) {
     directory <- ("./specdata/")
  
     all_files <- list.files(directory)
     paths <- paste(directory, all_files, sep="")
     
     com_list <- complete("specdata", 1:332)
     com_ids <- com_list$id [com_list$nobs > threshold]
     
     ids_l <- length (com_ids)
     
     num_vec <- numeric (ids_l)
     
     j <- 0
     
     for (i in com_ids) {
       dataset <- read.csv(paths[i], header=TRUE, sep=",")
       j <- j+1
       num_vec[j] <- cor(dataset$sulfate, dataset$nitrate, use = "na.or.complete")
      }
     
     num_vec
     
}