from tabulate import tabulate
data = [["Name", "Place", "Gender"], ["Steve Roggers", "New York", "Male"], ["Tony Stark", "New York", "Male"], ["Natasha Romanova", "Moscow", "Female"]]
print(tabulate(data, headers='firstrow', tablefmt='fancy_grid'))
