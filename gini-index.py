import pandas as pd
import numpy as np
import streamlit as st
from pandas_profiling import ProfileReport

st.title("Sample project: GINI Index across the countries from 1978-2007.")
st.markdown("**In economics, the Gini coefficient, also the Gini index and the Gini ratio, is a measure of statistical dispersion intended to represent the income inequality or the wealth inequality within a nation or a social group. The Gini coefficient was developed by the statistician and sociologist Corrado Gini. The Gini coefficient measures the inequality among values of a frequency distribution (for example, levels of income). A Gini coefficient of zero expresses perfect equality, where all values are the same (for example, where everyone has the same income). A Gini coefficient of one (or 100%) expresses maximal inequality among values (e.g., for a large number of people where only one person has all the income or consumption and all others have none, the Gini coefficient will be nearly one).**")

df = pd.read_csv("data\gini.csv")
df.dropna(axis = 0, inplace = True)

options_one = list(df['Country'])
i1 = st.selectbox('Select a country.', options_one, 1)
filtered_df = df[df['Country']==i1]

st.table(filtered_df)

import matplotlib.pyplot as plt

plt.scatter(filtered_df.columns[1], filtered_df.columns[2])
plt.title('Scatter plot for data visualization')
plt.xlabel('Year Collected')
plt.ylabel('GINI Index score')
plt.show()


st.header("You can find data set from the link in reference. Recommend to visit for more social economic indicators and data.")
st.markdown(
"**Reference - [Gapminder](https://www.gapminder.org/data/)**")
