#code to transform data to a binary encoded data file

hs <- read_xlsx("/location/file_name.xlsx")

cc <- str_split(hs$ocms, ",")

unique_ocms2 <- unique(unlist(cc))

binary_matrix2 <- matrix(0, nrow = nrow(hs), ncol = length(unique_ocms2))

colnames(binary_matrix2) <- unique_ocms2

for (i in 1:nrow(hs)) {

  ocm_values <- unlist(cc[i])

  binary_matrix2[i, ocm_values] <- 1
}

hs_combined <- cbind(hs, binary_matrix2)

write.csv(hs_combined, "/location/new_file_name.xlsx", row.names = FALSE)
