import pandas


data = pandas.read_csv("squirrels_cp.csv")

# print(data["Primary Fur Color"])

gray = len(data[data["Primary Fur Color"] == "Gray"])
red = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, red, black]
}

df = pandas.DataFrame(data_dict)
print(df)
df.to_csv("squirrel_count.csv")



color_counts = pandas.DataFrame(data["Primary Fur Color"].value_counts())

# color_counts.to_csv("sq_count.csv")
print(color_counts)