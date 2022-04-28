import csv
import pandas


# data = []

# with open("weather_data.csv") as d:
#     d_data = csv.reader(d)
#     temperatures = []
#     for row in d_data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# OR USE PANDAS

data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
data_dict = data.to_dict()
# print(data_dict)


# temps = []
# for ea in data["temp"]:
#     temps.append(ea)  
    # OR USE PANDA:
temp_list = data["temp"].to_list()

temp_avg = (sum(temp_list)) / (len(temp_list))
print(temp_avg)
# OR USE PANDAS:
temp_average = data["temp"].mean()
print(temp_average)

max_temp = data["temp"].max()
print(data.temp.max())

# GET DATA IN COLUMNS
data.condition
data["condition"]
# GET DATA IN ROWS
data[data["day"] == "Monday"]
data[data.day == "Monday"]
# FIND ROW WITH MAX TEMP
data[data.temp == data.temp.max()]

monday = data[data.day == "Monday"]
print(monday.condition)
# FIND MONDAYS TEMP IN FARENHEIT
print(monday.temp * 1.8 + 32)

# CREATE A DATAFRAME FROM SCRATCH
new_dict = {
    "students": ["Jerry", "Larry", "Terry"],
    "scores": [95, 90, 85]
}
new_data = pandas.DataFrame(new_dict)
new_data.to_csv("new_data.csv")
