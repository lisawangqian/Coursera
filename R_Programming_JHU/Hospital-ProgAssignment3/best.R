setwd("/Users/lisa/Desktop/R programming/rprog-data-ProgAssignment3-data")


findbest <- function(data, outc, state) {
	state_data <- data[data[, 7]==state, ]
	outcome_data <- state_data[, outc]
	min_value <- min(outcome_data, na.rm=T)
	min_rownum <- which(outcome_data == min_value)
	hos_name <- state_data[min_rownum, 2]
    sorted_name <- sort(hos_name)
    return (sorted_name[1])
  
}


best <- function(state, outcome) {
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
        best_hos_n <- findbest(dataset, 11, state)
      } 
      else if (outcome == "heart failure") {
        best_hos_n <- findbest(dataset, 17, state)
      } 
      else {
        best_hos_n <- findbest(dataset, 23, state)
      }
      
	  return (best_hos_n)
      
    }
}