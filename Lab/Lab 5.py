## Lab 5 Exercises ##
import numpy as np
import pandas as pd

## 1.
worldwide_gross_dict = {"Avengers: Endgame": 27|96274401,
                        "Avatar": 2789679794,
                        "Titanic": 2187463944,
                        "Star Wars: The Force Awakens": 2068223624,
                        "Avengers: Infinity War": 2048359754,
                        "Jurassic World": 1671713208,
                        "The Lion King": 1617824540}

year_dict = {"Avengers: Endgame": 2019,
             "Avatar": 2009,
             "Titanic": 1997,
             "Star Wars: The Force Awakens": 2015,
             "Avengers: Infinity War": 2018,
             "Jurassic World": 2015,
             "The Lion King": 2019}

# (a) Create a Pandas Series using worldwide_gross_dict above and assign it to gross.
gross = pd.Series(worldwide_gross_dict)

# (b) Create a Pandas Series using year_dict above and assign it to year.
year = pd.Series(year_dict)


# (c) Create a Pandas DataFrame using gross and year and assign in to movies.
movies = pd.DataFrame([gross,year],index=['gross','year']).T
# (d) Get films released in 2019.
movies.loc[movies["year"]==2019,"year"]
# (e) Get films released before 2017.
movies.loc[movies["year"]<2017,"year"]
# (f) Get films that have gross over $2 billion worldwide.
movies.loc[movies["gross"]>2000000000,"gross"]



## 2.
np.random.seed(seed=0)
data = np.random.randint(0, 1000, (30, 5))
data

# (a) Create a Pandas DataFrame using data above
#     with column names x1, x2, x3, x4, x5 and assign it to df.
df = pd.DataFrame(data,columns=["x1","x2","x3","x4","x5"])

# (b) Get the column names of df.
df.columns
# (c) Get all the values under the column x5.
df.iloc[:,4]
# (d) Get the first five rows of df using loc attribute.
df.loc[0:4,:]
# (e) Get the first five rows of df using iloc attribute.
df.iloc[0:5,:]
# (f) Get all the rows with the x1 being greater than 500.
df.loc[df["x1"]>500,:]
# (g) Get all the rows with the x1 being greater than or equal to 300 and x2 being less than 500.
# df.query("x1>=300 and x2<500")
df.loc[(df["x1"]>=300 )& (df["x2"]<500),:]

# (h) Get a subset of df that only contains columns x1, x3, and x5.
df.loc[:,["x1","x2","x5"]]