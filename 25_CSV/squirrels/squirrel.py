import pandas as pd

def main():
    data = extract_csv()
    colors = extract_colors(data)
    processed_data = pd.DataFrame.from_dict([colors])
    processed_data.to_csv("25_CSV\\squirrels\\squirrel_amount.csv")
    extract_colors_pd(data)
    # print(colors)

def extract_csv() -> pd.DataFrame:
    return pd.read_csv("25_CSV\squirrels\squirrel_data.csv")

def extract_colors(data: pd.DataFrame) -> dict:
    colors = dict()
    for i in data["Primary Fur Color"].dropna():
        if i not in colors:
            colors[i] = 1
        else:
            try:
                colors[i] += 1
            except KeyError:
                continue
    return colors

def extract_colors_pd(data: pd.DataFrame):
    data.groupby("Primary Fur Color").size().to_csv("25_CSV\\squirrels\\squirrel_amount_pd.csv")

main()