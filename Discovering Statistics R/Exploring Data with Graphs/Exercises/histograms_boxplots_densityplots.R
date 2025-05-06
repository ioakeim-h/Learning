# Page 142 to 149
url <- "https://studysites.sagepub.com/dsur/study/DSUR%20Data%20Files/Chapter%204/DownloadFestival.dat"
destfile <- "DownloadFestival.dat"
download.file(url, destfile)

path <- "C:\\Users\\ihadjimpalasis\\Desktop\\Learning\\LearningR\\Discovering Statistics\\Exploring Data with Graphs//Data"
festivalData <- read.table(file.path(path, "DownloadFestival.dat"), header = TRUE, sep = "\t")

####################################################################
# Histograms
####################################################################

hist <- ggplot(festivalData, aes(day1)) + 
  # Play around with binwidth to get an idea of the data distribution (smaller binwidth = higher detail)
  geom_histogram(binwidth = 0.4) + 
  labs(x="Hygiene on Day 1 of Festival", y="Frequency")
hist

####################################################################
# Box plots
####################################################################

boxPlot <- ggplot(festivalData, aes(x=gender, y=day1)) +
  geom_boxplot() +
  labs(x="Gender", y="Hygiene on Day 1 of Festival")
boxPlot

# The outlier was a typo. 
# Replace it with the correct value obtained from the raw data 
festivalData[festivalData$day1 > 15, "day1"] <- 2.02

# Replot
boxPlot <- ggplot(festivalData, aes(x=gender, y=day1)) +
  geom_boxplot() +
  labs(x="Gender", y="Hygiene on Day 1 of Festival")
boxPlot

####################################################################
# Density plots
####################################################################

densityPlot <- ggplot(festivalData, aes(day1)) +
  geom_density() +
  labs(x="Hygiene on Day 1 of Festival", y="Density Estimate")
densityPlot