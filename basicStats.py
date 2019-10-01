import pandas as pd
import pandas_profiling
import numpy as np

def getPdPLottStats(csv_file):
    df = pd.read_csv(csv_file)

    # remove the draw date column to only have the numbers
    df = df.drop(columns = '#Draw Date')
    df.describe()

    profile = df.profile_report(title='Pandas Profiling Lotto History Report')
    profile.to_file(output_file="PDP_LottoStats.html")