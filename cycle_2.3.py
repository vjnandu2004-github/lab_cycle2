import json

#create a list having each line of file as element

file = open("iris.json", "r")
txt_file = file.read()
print(txt_file)

def calculate_total_area(flower):
    sepal_area = flower.get("sepalLength") * flower.get("sepalWidth")
    petal_area = flower.get("petalLength") * flower.get("petalWidth")
    return sepal_area + petal_area

# convert into a list of dictionary objects

list_of_dictionary = json.loads(txt_file)

# show the details of the flower species naming setosta

for i in list_of_dictionary:
    if i.get("species") == "setosa":
        print(i)

petal_lst = []
sepal_lst = []
for j in list_of_dictionary:
    sepal_length = j.get('sepalLength')
    sepal_width = j.get('sepalWidth')
    petal_length = j.get('petalLength')
    petal_width = j.get('petalWidth')

    # Check for None values before performing calculations
    if all(v is not None for v in [sepal_length, sepal_width, petal_length, petal_width]):
        petal_area = round(petal_length * petal_width, 2)
        petal_lst.append(petal_area)
        sepal_area = round(sepal_length * sepal_width, 2)
        sepal_lst.append(sepal_area)
    else:
        print("Missing values for some attributes in the data.")

# Print the minimum petal area and max sepal area in each species

print("MAXIMUM SEPAL AREA:", max(sepal_lst))
print("MINIMUM PETAL AREA:", min(petal_lst))

#Sort the list of dictionaries according to the total area for sepal and petal.

sorted_list = sorted(list_of_dictionary, key=calculate_total_area, reverse=True)
print("Sorted List based on Total Area:")
for item in sorted_list:
    print(item)
