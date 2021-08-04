import csv

filename1 = "data/fav_fruits.csv"
filename2 = "data/fav_veggies.csv"

# retrieves data from lcoal csv store
# str, str -> list(str), list(str)
def get_data(fruit_file, veggie_file):
    fruits = []
    veggies = []

    # get csv values for fruit
    with open(fruit_file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fruits = next(csvreader)

    # get csv values for veggie
    with open(veggie_file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        veggies = next(csvreader)

    return fruits, veggies
