'''required:
What is the year and country that has the lowest life expectancy in the dataset?

What is the year and country that has the highest life expectancy in the dataset?

Allow the user to type in a year, then, find the average life expectancy for that year. Then find the country with the minimum and the one with the maximum life expectancies for that year.
'''

lowest_life_expectancy_country = ""
lowest_life_expectancy_year = ""
lowest_life_expectancy = 999
highest_life_expectancy = 0
highest_life_expectancy_country = ""
highest_life_expectancy_year = ""

with open(r"BYU\CSE_110_Intro_to_Programming\W06\life-expectancy.csv") as life_expectancy_data:
    for line in life_expectancy_data:
        line = line.strip()
        line = line.split(",")     
        Entity = line[0]
        Code = line[1]
        Year = line[2]
        Life_expectancy = float(line[3])
        if lowest_life_expectancy > Life_expectancy:
            lowest_life_expectancy = Life_expectancy
            lowest_life_expectancy_year = Year
            lowest_life_expectancy_country = Entity
        if highest_life_expectancy < Life_expectancy:
            highest_life_expectancy = Life_expectancy
            highest_life_expectancy_year = Year
            highest_life_expectancy_country = Entity

print(f"\nThe overall max life expectancy is: {highest_life_expectancy}")
print(f"The overall min life expectancy is: {lowest_life_expectancy}")