happiness_datasets <- list(
    happiness_2020 <- read.csv("2020.csv"),
    happiness_2021 <- read.csv("2021.csv"),
    happiness_2022 <- read.csv("2022.csv"),
    happiness_2023 <- read.csv("2023.csv"),
    happiness_2024 <- read.csv("2024.csv")
)

for (i in seq_along(happiness_datasets)) {
    # Skip character col
    happiness_datasets[[i]]$total_happiness <- apply(happiness_datasets[[i]][, 2:8], MARGIN=1, FUN=sum)
}

happiness_2020 <- happiness_datasets$happiness_2020
happiness_2021 <- happiness_datasets$happiness_2021
happiness_2022 <- happiness_datasets$happiness_2022
happiness_2023 <- happiness_datasets$happiness_2023
happiness_2024 <- happiness_datasets$happiness_2024

country <-