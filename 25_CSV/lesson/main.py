import csv
import pandas

def main():
    temperatures = extract_temperatures_pandas()
    print(temperatures)
    get_max_row()
    test_stuff()
    
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
    print(data["temp"].max())
    return data["temp"]

def get_max_row():
    data = pandas.read_csv("25_CSV\lesson\weather_data.csv")
    print(
        data[data["temp"] == data["temp"].max()]
    )

def test_stuff():
    data_dict = {
        "Pé legal": ["Pessoa 1", "Pessoa 2"],
        "Cruzas?": ["Sim", "Não"]
    }

    d = pandas.DataFrame(data_dict)
    d.to_csv("25_CSV\lesson\\to_csv.csv")
    # print(d)

main()