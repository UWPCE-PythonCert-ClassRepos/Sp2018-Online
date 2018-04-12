import pandas as pd

music = pd.read_csv("featuresdf.csv")


# Using iterrows() as I think it is more DB like and maybe clearer?

result = [(row['name'],
           row['artists'],
           row['danceability'],
           row['loudness']) for index,row in music.iterrows() if row['danceability'] > 0.8 and row['loudness'] <-5.0]

# found how to do a keyless sort on the 3rd column (danceability).  i.e. no key val pairs in the result
# just tuples, with 4 elements for each row
# e.g. ("You Don't Know Me - Radio Edit", 'Jax Jones', 0.8759999999999999,  -6.053999999999999)
print(sorted(result,key=lambda column : column[2], reverse=True))



