rm(list=ls())
setwd("/Users/akis/Desktop/CS50R/carpet")

visitors <- read.csv("visitors.csv")

calculate_growth_rate <- function(visitors) {
    # calculate the average yearly increase in visitors that PDX should expect
    visitors_diff <- visitors[visitors$year == max(visitors$year), "visitors"] - visitors[visitors$year == min(visitors$year), "visitors"]
    year_diff <- max(visitors$year) - min(visitors$year)
    return(visitors_diff / year_diff) 
}

repeat {
    year <- as.integer(readline("Year: "))
    if (year >= min(visitors$year)) {
        break
    }
}

predict_visitors <- function(visitors, year) {
    # predict the number of visitors to PDX in a given year
    growth_rate <- calculate_growth_rate(visitors)
    year_baseline <- visitors[visitors$year == max(visitors$year), "year"]
    visitors_baseline <- visitors[visitors$year == max(visitors$year), "visitors"]
    
    total_growth <- growth_rate * (year - year_baseline)
    predicted_visitors <- visitors_baseline + total_growth
    print(predicted_visitors)
}

