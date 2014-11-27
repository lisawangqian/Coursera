setwd("/Users/lisa/Desktop/R programming/rprog-data-ProgAssignment3-data")

rank <- function(data, outc, num) {
  
  outcome_data <- data[, outc]
  len <- dim(data[!is.na(outcome_data), ])[1]
  if (num == "worst") {
    num <- len
  } 
  else if (num == "best") {
    num <-1
  }
  if (num > len) {
    rank_name <- NA
  } 
  else {
    ordered_name <- data[, 2][order(outcome_data, data[, 2])]
    rank_name <- ordered_name[num]
  }
  
  return (rank_name)
  
}




rankall <- function(outcome, num = "best") {
  dataset <- read.csv("outcome-of-care-measures.csv", colClasses="character")
  
  check_outcome <- match(outcome, c("heart attack", "heart failure", "pneumonia"), nomatch=0)
  
  if (!check_outcome) {
    stop("invalid outcome")
  }
  else {
    dataset[, 11] <- as.numeric(dataset[, 11]) # heart attack mortality
    dataset[, 17] <- as.numeric(dataset[, 17]) # heart failure morality
    dataset[, 23] <- as.numeric(dataset[, 23]) # pneumonia morality
    state_data <-sort(unique(dataset$State))
    st_len <- length(state_data)
    hos_arr <- rep("", st_len)
    for (i in 1:st_len) {
      state_sub <- dataset[dataset[, 7]==state_data[i], ]
      if (outcome == "heart attack") {
      hos_arr[i] <- rank(state_sub, 11, num)
      } 
      else if (outcome == "heart failure") {
      hos_arr[i] <- rank(state_sub, 17, num)
      } 
      else {
      hos_arr[i] <- rank(state_sub, 23, num)
      }
    }
    
    rank_result <- data.frame(hospital=hos_arr, state=state_data)
    
    return (rank_result)
    
  }
}