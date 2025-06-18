df <- read.table(file = "tests.tsv", sep = '\t', header = TRUE)

# Get factor levels
levels(factor(df$gender))

df$gender <- factor(
  df$gender,
  labels = c("Unanswered","male","female", "Other"),
)

df$Extraversion <- (df$E1 + df$E2 + df$E3) / 15
df$Neuroticism <- (df$N1 + df$N2 + df$N3) / 15
df$Agreeableness <- (df$A1 + df$A2 + df$A3) / 15
df$Conscientiousness <- (df$C1 + df$C2 + df$C3) / 15
df$Openness <- (df$O1 + df$O2 + df$O3) / 15

# df$Extraversion <- round(df$Extraversion, 2)
# df$Neuroticism <- round(df$Neuroticism, 2)
# df$Agreeableness <- round(df$Agreeableness, 2)
# df$Conscientiousness <- round(df$Conscientiousness, 2)
# df$Openness <- round(df$Openness, 2)

columns <- c("Extraversion","Neuroticism","Agreeableness","Conscientiousness","Openness")
for (col in columns) {
  df[col] <- round(df[col], 2)
}
