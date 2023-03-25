# creates a dendrogram/heatmap that shows high level
# clustering of mutations.
library(colorspace) 
library(tidyr)
suppressMessages(library(dplyr))
library(stringdist)
library(dendextend)


seq <- read.csv("global_month.csv", sep=",",header=TRUE) 
seq <- na.omit(seq)


seq <- seq[!(seq$Count<5000),]


# add values to sequences so they show up on the heatmap
seq$Count = seq$Count + 15000

# get distance betwen sequences 
dist_mat <- stringdist::stringdistmatrix(seq$sequence, seq$sequence, method = "lv")

# cluster sequences
hc_seq <- hclust(as.dist(dist_mat), method="complete")


dend <- as.dendrogram(hc_seq)

dend <- rotate(dend, 1:nrow(seq))

# Color the branches 
dend <- color_branches(dend, k=20)


# make dendrogram
dend <- hang.dendrogram(dend,hang_height=0.1)

dend <- set(dend, "labels_cex", 0.5)

col_func <- function(n) rev(colorspace::heat_hcl(n, c = c(0, 0), l = c(0, 90),power=c(1,1)))# power = c(1/5, 1.5)))

seq2 <- seq %>% # reformat data
  select(accession,date,Count) %>%
  pivot_wider(names_from = date, values_from = Count) %>%
  mutate(across(everything(), ~replace_na(.x, 0)))

seq2 <- seq2 %>% # remove accession
  select(-accession)
gplots::heatmap.2(as.matrix(seq2), 
                  main = "Total Over Time",
                  srtCol = 90,
                  dendrogram = "row",
                  Rowv = dend,
                  Colv = "NA", # this to make sure the columns are not ordered
                  labRow = "",
                  trace="none", 
                  margins =c(5,5),  
                  key.xlab = "Number of recurences",
                  denscol = "grey",
                  density.info = "none",
                  scale=NULL,
                  col = col_func
)


