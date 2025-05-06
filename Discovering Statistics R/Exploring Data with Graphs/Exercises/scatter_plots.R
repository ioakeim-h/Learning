# Page 136
library(ggplot2)
library(MASS)

url <- "https://studysites.sagepub.com/dsur/study/DSUR%20Data%20Files/Chapter%204/Exam%20Anxiety.dat"
destfile <- "Anxiety.dat"
download.file(url, destfile)

path <- "C:\\Users\\ihadjimpalasis\\Desktop\\Learning\\LearningR\\Discovering Statistics\\Exploring Data with Graphs//Data"
examData <- read.table(file.path(path, "Anxiety.dat"), header = TRUE, sep = "\t")

# Fit a linear model (a straight line) to the data
# Results: Performance and anxiety have an inverse relationship.
simple_scatter <- ggplot(
  examData, aes(Anxiety, Exam)
  # geom_smooth: "lm" for linear model, alpha for transparency of 95% CI, fill for colouring the shade (CI)
) + geom_point() + geom_smooth(method="lm", alpha=0.1, fill="blue") + labs(x="Exam Anxiety", y="Exam Performance %")
simple_scatter

# Explore performance vs anxiety relationship based on Gender
# Results: The relationship was slightly stronger in males (steeper line)
# indicating that men's exam performance was more adversely affected by anxiety than women's exam anxiety
grouped_scatter <- ggplot(
  examData, aes(Anxiety, Exam, colour=Gender)
) + geom_point() + geom_smooth(method="lm", alpha=0.1, aes(fill=Gender)) 
grouped_scatter