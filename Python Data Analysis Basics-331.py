## 1. Reading our MoMA Data Set ##

from csv import reader

# Read the `artworks_clean.csv` file
opened_file = open('artworks_clean.csv')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

# Convert the birthdate values
for row in moma:
    birth_date = row[3]
    if birth_date != "":
        birth_date = int(birth_date)
    row[3] = birth_date
    
# Convert the death date values
for row in moma:
    death_date = row[4]
    if death_date != "":
        death_date = int(death_date)
    row[4] = death_date

# Write your code below

for row in moma:
    date=row[6]
    if date!="":
        date=int(date)
    row[6]=date

## 2. Calculating Artist Ages ##

ages=[]
for row in moma:
    date=row[6]
    birth=row[3]
    if type(birth)==int:
        age=date-birth
    else:
        age=0
    ages.append(age)

    
final_ages=[]
for i in ages:
    if i >20:
        final_age=i
    else:
        final_age="Unknown"
    final_ages.append(final_age)
        

## 3. Converting Ages to Decades ##

# The final_ages variable is available
# from the previous screen

decades=[]
for age in final_ages:
    if age=="Unknown":
        decade=age
    else:
        decade=str(age)
        decade=decade[:-1]
        decade=decade+"0s"
    decades.append(decade)

## 4. Summarizing the Decade Data ##

# The decades variable is available
# from the previous screen
decade_frequency={}
for decade in decades:
    if decade not in decade_frequency:
        decade_frequency[decade]=1
    else:
        decade_frequency[decade]+=1

## 5. Inserting Variables Into Strings ##

artist = "Pablo Picasso"
birth_year = 1881
template="{}'s birth year is {}"
output=template.format(artist,birth_year)
print(output)

## 6. Creating an Artist Frequency Table ##

artist_freq={}
for row in moma:
    artist=row[1]
    if artist not in artist_freq:
        artist_freq[artist]=1
    else:
        artist_freq[artist]+=1
        

## 7. Creating an Artist Summary Function ##

def artist_summary(artist_name):
    temp=artist_freq[artist_name]
    template="There are {1} artworks by {0} in the dataset"
    print(template.format(artist_name,temp))
    
    
artist_summary("Henri Matisse")

## 8. Formatting Numbers Inside Strings ##

pop_millions = [
    ["China", 1379.302771],
    ["India", 1281.935991],
    ["USA",  326.625791],
    ["Indonesia",  260.580739],
    ["Brazil",  207.353391],
]

for row in pop_millions:
    country=row[0]
    pop=row[1]
    print("The population of {} is {:,.2f} million".format(country,pop))

## 9. Challenge: Summarizing Artwork Gender Data ##


gender_freq={}

for row in moma:
    temp=row[5]
    if temp not in gender_freq:
        gender_freq[temp]=1
    else:
        gender_freq[temp]+=1
sorted_gender_freq=sorted(gender_freq.items(), key=lambda x:x[1], reverse=True)
for row in sorted_gender_freq:
    template="There are {n:,} artworks by {g} artists"
    print(template.format(n=row[1],g=row[0]))