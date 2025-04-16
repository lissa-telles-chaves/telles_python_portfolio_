import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
df = pd.read_csv("/Users/lissachaves/Documents/GitHub/TELLES_Python_portfolio/TidyData-Project/olympics_08_medalists.csv")
pd.melt(df)
str.split(df)
# Replace empty strings with NaN
df.replace('', np.nan, inplace=True)
# Drop rows with NaN values
df.dropna(inplace=True)
