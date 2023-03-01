cities_list = ["Almaty", "Shymkent", "Astana", "Aqtau", "Atyrau", "Aqtobe"]

with open("cities.txt", "w") as fo:
    for city in cities_list:
        fo.write(city + "\n")


with open("cities.txt", "r") as fo:
    lines = fo.readlines()
    print(lines)