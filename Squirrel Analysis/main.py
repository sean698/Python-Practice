import pandas 

data = pandas.read_csv("Squirrel Analysis/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

red_squirrel = data[data["Primary Fur Color"] == "Cinnamon"]
black_squirrel = data[data["Primary Fur Color"] == "Black"]
gray_squirrel = data[data["Primary Fur Color"] == "Gray"]

squirrel_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [len(gray_squirrel), len(red_squirrel), len(gray_squirrel)]
}

df = pandas.DataFrame(squirrel_dict)
df.to_csv("Squirrel Analysis/squirrel_count.csv")