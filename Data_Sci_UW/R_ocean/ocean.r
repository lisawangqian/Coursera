dataset <- read.csv(file="seaflow_21min.csv", header=TRUE, sep=",")
library(caret)
set.seed(3456)
trainindex <- createDataPartition(dataset$cell_id, p = 0.5, list = FALSE, times=1)
datatrain <- dataset[trainindex,]
datatest <- dataset[-trainindex,]
mean(datatrain$time)

train<-data.frame(datatrain)
datatest<-data.frame(datatest)


library(rpart)
fol <- formula(pop ~ fsc_small + fsc_perp + fsc_big + pe +chl_big + chl_small)
model <- rpart(fol, method="class", data=train)
print(model)


pred <- predict(model, datatest, "class")


com <- pred == datatest$pop

sum(com)/length(datatest$pop)



library(randomForest)
model <- randomForest(fol, data=train)
pred <- predict(model, datatest, "class")

com <- pred == datatest$pop

sum(com)/length(datatest$pop)

library(e1071)
model <- svm(fol, data=train)
pred <- predict(model, datatest, decision.values = FALSE, probability = FALSE, na.action = na.omit)
com <- pred == datatest$pop

sum(com)/length(datatest$pop)


ndataset <- dataset[dataset$file_id != 208,]
train <- ndataset[trainindex,]
datatest <- ndataset[-trainindex,]
train<-data.frame(datatrain)
datatest<-data.frame(datatest)
model <- svm(fol, data=train)
pred <- predict(model, datatest, decision.values = FALSE, probability = FALSE, na.action = na.omit)
com <- pred == datatest$pop

sum(com)/length(datatest$pop)