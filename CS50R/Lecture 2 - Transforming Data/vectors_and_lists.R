# Vectors in R hold elements of the same dtype
# Even if you try to create a vector with mixed dtypes, R will coerce them to a single type.
myNumericalVector <- c(1,2,3)
myTextualVector <- c("ena","dio","tria")

# A list can contain mixed dtypes
myList <- list(myNumericalVector, myTextualVector)

# Indexing lists
################################
myList[1] # returns the first vector as a list
typeof(myList[1])

myList[[1]] # returns the first vector 
typeof(myList[[1]]) # a vector takes the dtype of its elements

# Name list components for easier indexing
names(myList) <- c("Numbers","Text")
myList$Numbers # same functionality as myList[[1]]

# Select the first value from the first vector of the list
myList[[1]][1] # OR
myList$Numbers[1]
