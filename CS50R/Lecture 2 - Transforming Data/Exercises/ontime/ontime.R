library(glue)

setwd("C:\\Users\\ihadjimpalasis\\Desktop\\Learning\\LearningR\\CS50R\\Lecture 2 - Transforming Data\\Exercises\\ontime")

# service: a mode of transportation
# reliability: how often a service is on time

bus <- read.csv("bus.csv")
rail <- read.csv("rail.csv")

# reliability = numerator / denominator
bus$reliability <- bus$numerator / bus$denominator
rail$reliability <- rail$numerator / rail$denominator

bus_routes <- unique(bus$route)
rail_routes <- unique(rail$route)
route <- readline("Route: ")

invalid_route <- FALSE

if (route %in% bus_routes) {
  reliability_on_peak <- round(mean(bus[(bus$route == route) & (bus$peak == "PEAK"), "reliability"] * 100), 0)
  reliability_off_peak <- round(mean(bus[(bus$route == route) & (bus$peak == "OFF_PEAK"), "reliability"] * 100), 0)
} else if (route %in% rail_routes) {
  reliability_on_peak <- round(mean(rail[(rail$route == route) & (rail$peak == "PEAK"), "reliability"] * 100), 0)
  reliability_off_peak <- round(mean(rail[(rail$route == route) & (rail$peak == "OFF_PEAK"), "reliability"] * 100), 0)
} else {
  invalid_route <- TRUE
}

if (invalid_route) {
  print("Enter a valid route.")
} else {
  print(glue("On time {reliability_on_peak}% of the time during peak hours."))
  print(glue("On time {reliability_off_peak}% of the time during off-peak hours."))
}


