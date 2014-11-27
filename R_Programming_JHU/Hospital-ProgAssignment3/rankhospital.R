setwd("/Users/lisa/Desktop/R programming/rprog-data-ProgAssignment3-data")

rank <- function(data, outc, state, num) {
  state_data <- data[data[, 7]==state, ]
  outcome_data <- state_data[, outc]
  len <- dim(state_data[!is.na(outcome_data), ])[1]
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
    ordered_name <- state_data[, 2][order(outcome_data, state_data[, 2])]
    rank_name <- ordered_name[num]
  }
  
  return (rank_name)
  
}




rankhospital <- function(state, outcome, num = "best") {
  dataset <- read.csv("outcome-of-care-measures.csv", colClasses="character")
  check_state <- match(state,dataset$State,nomatch=0)
  check_outcome <- match(outcome, c("heart attack", "heart failure", "pneumonia"), nomatch=0)
  
  if (!check_state) {
    stop("invalid state")
  }
  else if (!check_outcome) {
    stop("invalid outcome")
  }
  else {
    dataset[, 11] <- as.numeric(dataset[, 11]) # heart attack mortality
    dataset[, 17] <- as.numeric(dataset[, 17]) # heart failure morality
    dataset[, 23] <- as.numeric(dataset[, 23]) # pneumonia morality
    
    if (outcome == "heart attack") {
      rank_result <- rank(dataset, 11, state, num)
    } 
    else if (outcome == "heart failure") {
      rank_result <- rank(dataset, 17, state, num)
    } 
    else {
      rank_result <- rank(dataset, 23, state, num)
    }
    
    return (rank_result)
    
  }
}