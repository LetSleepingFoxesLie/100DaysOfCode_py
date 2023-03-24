import csv
import pandas

def main():
    temperatures = extract_temperatures_pandas()
    print(temperatures)
    
# 
def extract_temperatures_csv():
    temperatures = list()
    with open("25_CSV\lesson\weather_data.csv", "r") as f:
        data = csv.reader(f)
        for row in data:
            if row[1] == "temp":
                continue
            temperatures.append(int(row[1]))
    return temperatures

def extract_temperatures_pandas():
    data = pandas.read_csv("25_CSV\lesson\weather_data.csv")
    return data["temp"]

main()