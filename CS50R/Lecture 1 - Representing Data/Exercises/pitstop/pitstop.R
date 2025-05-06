rm(list = ls())

file_to_analyze = readline(prompt = "Enter name of CSV file to analyze: ")
df = read.csv(file_to_analyze)

print(paste("Total number of pit stops:", nrow(df)))
print(paste("Duration of shortest pit stop:", min(df$time)))
print(paste("Duration of longest pit stop:", max(df$time)))
print(paste("Total time spent on pit stops across races:", sum(df$time)))

