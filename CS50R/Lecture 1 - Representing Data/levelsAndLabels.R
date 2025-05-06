
url = "https://github.com/fivethirtyeight/data/raw/master/non-voters/nonvoters_data.csv"
voters = read.csv(url, sep=",")
View(voters)

# Convert a vector into a factor -> gives levels to categorical data
factor(voters$Q21)

# Give factored categories a name
factor(
  voters$Q21,
  # Based on levels 1, 2, 3 when -1 is excluded, creating NA
  labels = c("Yes","No","Unsure/Undecided"),
  exclude = c(-1)
)