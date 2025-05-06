library(dplyr)

tests <- read.table("tests.tsv", header = TRUE, sep = "\t")

tests$gender <- as.character(tests$gender)
tests$gender <- recode(tests$gender, "0" = "Unanswered", "1" = "Male", "2" = "Female")

# extroversion, a column that represents each test’s result on the extroversion trait
tests$extroversion <- (tests$E1 + tests$E2 + tests$E3) / 15
print(tests[1:3, c("E1","E2","E3","extroversion")])

# neuroticism, a column that represents each test’s result on the neuroticism trait
tests$neuroticism <- (tests$N1 + tests$N2 + tests$N3) / 15
print(tests[1:3, c("N1","N2","N3","neuroticism")])

# agreeableness, a column that represents each test’s result on the agreeableness trait
tests$agreeableness <- (tests$A1 + tests$A2 + tests$A3) / 15
print(tests[1:3, c("A1","A2","A3","agreeableness")])

# conscientiousness, a column that represents each test’s result on the conscientiousness trait
tests$conscientiousness <- (tests$C1 + tests$C2 + tests$C3) / 15
print(tests[1:3, c("C1","C2","C3","conscientiousness")])

# openness, a column that represents each test’s result on the openness trait
tests$openness <- (tests$O1 + tests$O2 + tests$O3) / 15
print(tests[1:3, c("O1","O2","O3","openness")])

write.csv(tests, "analysis.csv", row.names = FALSE)