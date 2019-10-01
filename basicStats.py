import pandas as pd
import pandas_profiling
import numpy as np

def getPdProfilingStats(csv_file):
    df = pd.read_csv(csv_file)
    df.describe()
    # pandas_profiling.ProfileReport(df)