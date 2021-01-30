import csv
from bs4 import BeautifulSoup


renewable_projects = {}

data_file = csv.reader(open("Resources/Renewable_Energy_Permits.csv"), delimiter=",")
for row in data_file:
    try:
        county = row[22]

        if county != '' and county.upper() != 'COUNTY':
            if county in renewable_projects.keys():
                renewable_projects[county] = renewable_projects[county] + 1
            else:
                renewable_projects[county] = 1

    except:
        pass

svg = open("Resources/VA_county_map.svg", 'r').read()

soup = BeautifulSoup(svg, features='lxml-xml')

colors = ['#edf8fb','#b2e2e2','#66c2a4','#2ca25f','#006d2c', '#fff']

paths = soup.find_all("path", attrs={'id': True})

for path in paths:
    if path['id'] in renewable_projects.keys():
        # pass
        try:
            number_of_projects = renewable_projects[path['id']]
        except:
            continue

        if number_of_projects > 4:
            color_class = 4
        elif number_of_projects == 4:
            color_class = 3
        elif number_of_projects == 3:
            color_class = 2
        elif number_of_projects == 2:
            color_class = 1
        elif number_of_projects == 1:
            color_class = 0

        color = colors[color_class]
        print(path)
        path['fill'] = color
        print(path)
        print("")







with open('Resources/VA_county_map_new.svg', 'w') as file:
    file.write(str(soup))
