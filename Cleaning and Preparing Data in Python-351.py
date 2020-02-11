## 1. Introducing Data Cleaning ##

# Read the text on the left, and then scroll to the bottom
# to find the instructions for the coding exercise

# Write your answer to the instructions below -- the list of
# lists is stored using the variable name `moma`
num_rows=len(moma)
print(num_rows)

## 2. Reading our MoMA Data Set ##

# import the reader function from the csv module
from csv import reader

# use the python built-in function open()
# to open the children.csv file
opened_file = open('artworks.csv')

# use csv.reader() to parse the data from
# the opened file
read_file = reader(opened_file)

# use list() to convert the read file
# into a list of lists format
children = list(read_file)

# remove the first row of the data, which
# contains the column names


# Write your code here
moma=children[1:]

## 3. Replacing Substrings with the replace Method ##

age1 = "I am thirty-one years old"
age2=age1.replace("one","two")

## 4. Cleaning the Nationality and Gender Columns ##

# Variables you create in previous screens
# are available to you, so you don't need
# to read the CSV again
for column in moma:
    temp=column[2]
    temp=temp.replace("(","")
    temp=temp.replace(")","")
    column[2]=temp
    temp2=column[5]
    temp2=temp2.replace("(","")
    temp2=temp2.replace(")","")
    column[5]=temp2

## 5. String Capitalization ##

for data in moma:
    gender=data[5]
    gender=gender.title()
    if not gender:
        gender="Gender Unknown/Other"
    data[5]=gender
    nationality=data[2]
    nationality=nationality.title()
    if not nationality:
        nationality="Nationality Unknown"
    data[2]=nationality
    


## 6. Errors During Data Cleaning ##

def clean_and_convert(date):
    # check that we don't have an empty string
    if date != "":
        # move the rest of the function inside
        # the if statement
        date = date.replace("(", "")
        date = date.replace(")", "")
        date = int(date)
    return date

for data in moma:
    begin_date=clean_and_convert(data[3])
    end_date=clean_and_convert(data[4])
    data[3]=begin_date
    data[4]=end_date

## 7. Parsing Numbers from Complex Strings, Part One ##

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    for i in bad_chars:
        string=string.replace(i,"")
    return string

stripped_test_data=[]
for data in test_data:
    temp=strip_characters(data)
    stripped_test_data.append(temp)

## 8. Parsing Numbers from Complex Strings, Part Two ##

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,"")
    return string

stripped_test_data = ['1912', '1929', '1913-1923',
                      '1951', '1994', '1934',
                      '1915', '1995', '1912',
                      '1988', '2002', '1957-1959',
                      '1955', '1970', '1990-1999']
def process_date(string):
    sum_year=0
    if '-' in string:
        year=string.split('-')
        for i in year:
            temp=int(i)
            sum_year+=temp
        avg_year=round(sum_year/2)
        return avg_year
    else:
        return int(string)
    
processed_test_data=[]
for year in stripped_test_data:
    processed_test_data.append(process_date(year))
    
    
for data in moma:
    date_one=data[6]
    date_one=strip_characters(date_one)
    date_two=process_date(date_one)
    data[6]=date_two