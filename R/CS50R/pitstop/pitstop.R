
# Prompt for CSV 
file <- readline("Provide CSV file: ")
# file <- "miami.csv"
df <- read.csv(file, header=T)

# print num of pit stops
num_pitstops <- paste0("Num of pit stops: ", nrow(df))
print(num_pitstops)

# print duration of shortest pit stop
print(min(df$time))

# duration of longest pit stop
print(max(df$time))

# total time spent on pit stops, across all racers
print(sum(df$time))

