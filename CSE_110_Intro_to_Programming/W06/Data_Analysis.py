#Author: MReduzino

#Extra Points:
'''
In addition to the core requirements, this program allows users to analyze life expectancy data for
a specific country, showing its minimum, maximum, and average life expectancy values throughout the years.
'''

lowest_life_expectancy_country = ""
lowest_life_expectancy_year = ""
lowest_life_expectancy = 999
highest_life_expectancy = 0
highest_life_expectancy_country = ""
highest_life_expectancy_year = ""

year_of_interest = int(input("Enter the year of interest: "))
year_total = 0
year_count = 0
year_lowest = 999
year_lowest_country = ""
year_highest = 0
year_highest_country = ""

with open(r"BYU\CSE_110_Intro_to_Programming\W06\life-expectancy.csv") as life_expectancy_data:
    next(life_expectancy_data)
    for line in life_expectancy_data:
        line = line.strip()
        line = line.split(",")     
        Entity = line[0]
        Code = line[1]
        Year = int(line[2])
        Life_expectancy = float(line[3])        
        if lowest_life_expectancy > Life_expectancy:
            lowest_life_expectancy = Life_expectancy
            lowest_life_expectancy_year = Year
            lowest_life_expectancy_country = Entity
        if highest_life_expectancy < Life_expectancy:
            highest_life_expectancy = Life_expectancy
            highest_life_expectancy_year = Year
            highest_life_expectancy_country = Entity            
        if Year == year_of_interest:
            year_total += Life_expectancy
            year_count += 1
            year_average = year_total / year_count 
            if Life_expectancy < year_lowest:
                year_lowest = Life_expectancy
                year_lowest_country = Entity
            if Life_expectancy > year_highest:
                year_highest = Life_expectancy
                year_highest_country = Entity

print(f"\nThe overall max life expectancy is: {highest_life_expectancy} from {highest_life_expectancy_country} in {highest_life_expectancy_year}\n")
print(f"The overall min life expectancy is: {lowest_life_expectancy} from {lowest_life_expectancy_country} in {lowest_life_expectancy_year}")
print(f"For the year {year_of_interest}:")
print(f"The average life expectancy across all countries was {year_average}")
print(f"The max life expectancy was in {year_highest_country} with {year_highest}")
print(f"The min life expectancy was in {year_lowest_country} with {year_lowest}")

analyze_country = input("\nWould you like to analyze a specific country? (yes/no): ")

if analyze_country.lower() == "yes":
    country_name = input("\nEnter the name of the country: ")
    country_total = 0
    country_count = 0
    country_min = 999
    country_max = 0
    country_found = False
    
    with open(r"BYU\CSE_110_Intro_to_Programming\W06\life-expectancy.csv") as life_expectancy_data:
        next(life_expectancy_data)
        for line in life_expectancy_data:
            line = line.strip()
            parts = line.split(",")
            entity = parts[0]
            life_expectancy = float(parts[3])
            
            if entity.lower() == country_name.lower():
                country_found = True
                country_total += life_expectancy
                country_count += 1
                
                if life_expectancy < country_min:
                    country_min = life_expectancy
                if life_expectancy > country_max:
                    country_max = life_expectancy
    
    if country_found:
        country_avg = country_total / country_count
        print(f"\nAnalysis for {country_name.capitalize()}:")
        print(f"Minimum life expectancy: {country_min}")
        print(f"Maximum life expectancy: {country_max}")
        print(f"Average life expectancy: {country_avg:.3f}")
    else:
        print(f"\nNo data found for {country_name}")
else:
    print("Program finalized")