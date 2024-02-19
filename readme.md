The `calculate_demographic_data` function calculates various demographic data from a census dataset. It takes an optional argument `print_data` which is set to `True` by default.

The function first reads the census data from a csv file into a pandas dataframe. It then calculates the following:

- The number of unique races represented in the dataset
- The average age of men in the dataset
- The percentage of people who have a Bachelor's degree
- The percentage of people with advanced education (Bachelor's, Master's, or Doctorate) who earn more than 50K
- The percentage of people without advanced education who earn more than 50K
- The minimum number of hours a person works per week
- The percentage of people who work the minimum number of hours per week and earn more than 50K
- The country with the highest percentage of people who earn more than 50K
- The percentage of people in that country who earn more than 50K
- The most popular occupation for those who earn more than 50K in India.

If the optional argument `print_data` is set to `True`, the function will print the results to the console. Otherwise, it will only return the results as a dictionary.