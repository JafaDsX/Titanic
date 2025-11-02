
import pandas as pd


def run():
    df = pd.read_csv("../data/Titanic-Dataset.csv")
    print(df)
    
    
if __name__ == '__main__':
    run()