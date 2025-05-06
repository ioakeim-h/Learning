books <- read.csv("books.csv")
authors <- read.csv("authors.csv")
answers <- read.delim("answers.txt", header=F, col.names="Answers")

# The writer's request:
# Looking for Mia Morgan's book
miaMorgan_book <- books[books$author == "Mia Morgan", "title"]

# grepl() returns a logical vector (TRUE or FALSE) corresponding to whether 
# "Writer" is found in each element of the Answers column.
writer_value <- answers[grepl("Writer", answers$Answers) , "Answers"]
answers[answers$Answers == writer_value, "Answers"] <- paste(writer_value, miaMorgan_book)

# The musician's request:
# Per the request, title should relate to music history 
music_book <- books[books$year == 1613, "title"][2]
musician_value <- answers[grepl("Musician", answers$Answers) , "Answers"]
answers[answers$Answers == musician_value, "Answers"] <- paste(musician_value, music_book)

# The traveler's request:
# Book published in 1775 with two possible authors
# Only one book published in 1775 though
travelers_book <- books[books$year == 1775, "title"]
travelers_value <- answers[grepl("Traveler", answers$Answers) , "Answers"]
answers[answers$Answers == travelers_value, "Answers"] <- paste(travelers_value, travelers_book)

# The painter's request:
# Topic: art 
# Published in 1990 or 1992
painters_book <- books[(books$year == 1990 | books$year == 1992), "title"][1]
painters_value <- answers[grepl("Painter", answers$Answers), "Answers"]
answers[answers$Answers == painters_value, "Answers"] <- paste(painters_value, painters_book)

# The scientist's request:
# Quantum Mechanics in title
scientists_book <- books[grepl("Quantum Mechanics", books$title), "title"]
scientists_value <- answers[grepl("Scientist", answers$Answers), "Answers"]
answers[answers$Answers == scientists_value, "Answers"] <- paste(scientists_value, scientists_book)


# The teacher's request:
# Topic education
# Published in the 1700s
# Author town is Zenthia
zenthia_authors <- authors[grepl("Zenthia", authors$hometown), "author"]
zenthia_authors_books <- books$author %in% zenthia_authors
books_in_1700s <- books$year > 1700 & books$year < 1800

teachers_book <- books[zenthia_authors_books & books_in_1700s, "title"]
teachers_value <- answers[grepl("Teacher", answers$Answers), "Answers"] 
answers[answers$Answers == teachers_value, "Answers"] <- paste(teachers_value, teachers_book)

# Export answers updated
write.table(answers, file="answers.txt", row.names=F, col.names=F)
