##########################################
# Subsetting dataframes
#########################################
chicks <- data.frame(chickwts)

# Filtering df based on condition, displaying all columns
chicks[chicks$feed == "casein", ]

# Filtering df based on condition, displaying a single column as a vector
chicks[chicks$feed == "casein", "feed"]

# The same with NAs
chicks[is.na(chicks$feed), ]

# Reverting the condition using !
chicks[!is.na(chicks$feed), ]

# Reset rownames (indices) after removing records
rownames(chicks) <- NULL

#####################################################################
# Printing with vectorized functions
#####################################################################
feed_options <- unique(chicks$feed)
cat(paste0(1:6, ". ", feed_options, "\n"), sep="")

#######################################################################
# Vectorized Conditionals
#######################################################################
# Replace values based on condition
ifelse(chicks$feed == "casein", "cool", "not cool")


