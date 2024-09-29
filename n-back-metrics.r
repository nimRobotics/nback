# Load required libraries
library(dplyr)

# Read the CSV file
data <- read.csv("n-back_results_test.csv")

# Calculate metrics
metrics <- data %>%
  summarise(
    Total = n(),
    TP = sum(ShouldRespond == 1 & Response == 1),
    TN = sum(ShouldRespond == 0 & Response == 0),
    FP = sum(ShouldRespond == 0 & Response == 1),
    FN = sum(ShouldRespond == 1 & Response == 0),
    P = sum(ShouldRespond == 1),
    N = sum(ShouldRespond == 0)
  ) %>%
  mutate(
    Accuracy = (TP + TN) / Total,
    Sensitivity = TP / P,
    Specificity = TN / N,
    ResponseDelay = mean(data$Response.Time..ms., na.rm = TRUE)
  )

# Print the results
print(metrics)
