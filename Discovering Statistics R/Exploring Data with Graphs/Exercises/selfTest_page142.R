# Self test page 142
library(ggplot2)

# url <- "https://studysites.sagepub.com/dsur/study/DSUR%20Data%20Files/Chapter%204/FacebookNarcissism.dat"
# destfile <- "FacebookNarcissism.dat"
# download.file(url, destfile)

path <- "C:\\Users\\ihadjimpalasis\\Desktop\\Learning\\LearningR\\Discovering Statistics\\Exploring Data with Graphs\\Data"
facebookData <- read.table(file.path(path, "FacebookNarcissism.dat"), header = TRUE, sep = "\t")

scatter <- ggplot(
  facebookData, aes(NPQC_R_Total, Rating)
) + geom_point(aes(colour=Rating_Type), position="jitter") + 
  geom_smooth(aes(colour=Rating_Type), method="lm", se=F) + 
  labs(x="Narsicism (NPQC)", y="Facebook Picture Rating", colour="Rated Attribue")
scatter

