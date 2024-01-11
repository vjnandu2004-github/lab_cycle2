import json

file = open("iris.json", "r")
txt_file = file.read()
print(txt_file)

def calculate_total_area(flower):
    sepal_area = flower.get("sepal_length") * flower.get("sepal_width")
    petal_area = flower.get("petal_length") * flower.get("petal_width")
    return sepal_area + petal_area

list_of_dictionary = json.loads(txt_file)

for i in list_of_dictionary:
    if i.get("species") == "setosa":
        print(i)

petal_lst = []
sepal_lst = []
for j in list_of_dictionary:
    sepal_length = j.get('sepalLength')  # Update with the correct attribute name
    sepal_width = j.get('sepalWidth')    # Update with the correct attribute name

    petal_length = j.get('petalLength')  # Update with the correct attribute name
    petal_width = j.get('petalWidth')    # Update with the correct attribute name

    petal_area = round(petal_length * petal_width, 2)
    petal_lst.append(petal_area)
    sepal_area = round(sepal_length * sepal_width, 2)
    sepal_lst.append(sepal_area)

print("MAXIMUM SEPAL AREA:", max(sepal_lst))
print("MINIMUM PETAL AREA:", min(petal_lst))

# Corrected the key parameter in the sorted function
sorted_list = sorted(list_of_dictionary, key=calculate_total_area, reverse=True)
