
# code for getting boxplot
# each segment had a column so I just changed which column was
# being called when I ran the data.

library(tidyr)
suppressMessages(library(dplyr))
library(stringdist)

seq <- read.csv("base2.csv",sep=",",header=TRUE);
seq2 <- read.csv("global_month.csv", sep=",",header=TRUE) 

seq2 <- na.omit(seq2)
seq2$dist = stringdist(seq2$HR1,seq$HR1[1],method="lv")
#seq2 <- seq2[!(seq2$dist > 50),] #RBD had a lot of outliers 
#seq2 <- seq2[!(seq2$dist > 100),]#NTD had a lot of outliers


boxplot(dist~date,data=seq2,main="HR1 Distance from Reference", xlab="date", ylab="distance")


