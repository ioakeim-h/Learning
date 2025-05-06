library(glue)

data_list <- list(
happiness_2020 <- read.csv("2020.csv"),
happiness_2021 <- read.csv("2021.csv"),
happiness_2022 <- read.csv("2022.csv"),
happiness_2023 <- read.csv("2023.csv"),
happiness_2024 <- read.csv("2024.csv")
)

country <- readline("Country: ")
year <- 2020

for (data in data_list) {
  # Except character col from calculations
  data$total_happiness <- apply(data[, 2:8], MARGIN=1, FUN=sum)
  score <- round(data[data$country == country, "total_happiness"], 2)
  
  print(glue("{country} ({year}): {score}"))
  year <- year + 1
}


