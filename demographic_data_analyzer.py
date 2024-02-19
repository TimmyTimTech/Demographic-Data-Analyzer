import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    df.head()
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].nunique()

    # What is the average age of men?
    average_age_men = df[df['sex']=='Male']['age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    Bachelors = df[df['education']=='Bachelors'].value_counts().sum()
    All = df['education'].value_counts().sum()

    Percentage_of_Bachelors = (Bachelors/All)*100
    
    percentage_bachelors = Percentage_of_Bachelors

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    advanced_education = df.loc[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    salary_advanced_education = advanced_education.loc[advanced_education["salary"] == ">50K"]
    
    advanced_education_salary_percentage = round(
    100 * len(salary_advanced_education) / len(df),
    1,
    )
    
    print(advanced_education_salary_percentage,'%')
    
    # What percentage of people without advanced education make more than 50K?
    # Filter the rows where education is Bachelors, Masters, or Doctorate
    low_education_fil = df.loc[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # Filter the rows where salary is >50K
    salary_low_education = low_education_fil.loc[low_education_fil["salary"] == ">50K"]

    low_education_salary_percentage = round(
    100 * len(salary_low_education) / len(df),
    1,
    )

    print(low_education_salary_percentage,'%')
    #Total number of low education people
    low_education = All - advanced_education.value_counts().sum()
    
    
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = advanced_education.value_counts().sum()
    lower_education = low_education

    # percentage with salary >50K
    higher_education_rich = advanced_education_salary_percentage
    lower_education_rich = low_education_salary_percentage

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    
    num_min_workers = df.loc[df['hours-per-week']==min_hours].value_counts().sum()
    
    # Filter the rows where `hours-per-week` is equal to the minimum number of hours
    workers_min_hours = df.loc[df['hours-per-week'] == min_hours]

    # Filter the rows where `salary` is greater than 50K
    salary_min_workers = workers_min_hours.loc[workers_min_hours['salary'] == '>50K']

    # Calculate the percentage
    salary_min_hours = round(100 * len(salary_min_workers) / len(df), 1)

    rich_percentage = salary_min_hours

    # What country has the highest percentage of people that earn >50K?
    # Filter the rows where `salary` is greater than 50K
    rich = df.loc[df["salary"] == ">50K"]

    # Calculate the number of rows for each country in the filtered data
    rich_count = rich["native-country"].value_counts()


    
    highest_earning_country = rich_count.max()
    
    # Calculate the percentage of people from each country who earn more than 50K
    country_percentages = rich["native-country"].value_counts(normalize=True) * 100

    # Find the top 3 countries with the highest percentage
    top_countries = country_percentages.nlargest(1)

    highest_earning_country_percentage = top_countries

    # Identify the most popular occupation for those who earn >50K in India.
    
    # Filter the rows where the salary is greater than 50K and the native-country is India
    high_salary_india = df.loc[(df["salary"] == ">50K") & (df["native-country"] == "India")]

    # Find the most popular occupation
    most_popular_occupation = high_salary_india["occupation"].mode()[0]

    top_IN_occupation = most_popular_occupation

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
print(calculate_demographic_data(print_data=True))