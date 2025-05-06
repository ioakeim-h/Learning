rm(list=ls())
setwd("C:\\Users\\ihadjimpalasis\\Desktop\\Learning\\LearningR\\CS50R\\Lecture 2 - Transforming Data\\Exercises\\teahouse")

flavor <- readline("Flavor: ")
caffeine <- readline("Caffeine: ")

valid_flavor <- function(flavor) {
  return(flavor %in% c("Light","Bold"))
}

valid_caffeine <- function(caffeine) {
  return(caffeine %in% c("Yes","No"))
}

recommend_tea <- function(flavor, caffeine) {
  if (caffeine == "Yes") {
    ifelse(flavor == "Light", print("You might like green tea"), print("You might like black tea"))
  } else {
    ifelse(flavor == "Light", print("You might like chamomile tea"), print("You might like rooibos tea"))
  }
}

# Main
if (!valid_flavor(flavor)) {
  print("Enter either 'Light' or 'Bold' for flavor")
} else if (!valid_caffeine(caffeine)) {
  print("Enter either 'Yes' or 'No' for caffeine")
} else {
  recommend_tea(flavor, caffeine)
}




