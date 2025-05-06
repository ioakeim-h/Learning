url <- "https://studysites.sagepub.com/dsur/study/DSUR%20Data%20Files/Chapter%204/ChickFlick.dat"
destfile <- "ChickFlick.dat"
download.file(url, destfile)

path <- "C:\\Users\\ihadjimpalasis\\Desktop\\Learning\\LearningR\\Discovering Statistics\\Exploring Data with Graphs//Data"
chickFlick <- read.table(file.path(path, "ChickFlick.dat"), header = TRUE, sep = "\t")

