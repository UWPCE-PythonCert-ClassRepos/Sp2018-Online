import pandas as pd

music = pd.read_csv("featuresdf.csv")
music.head()
music.describe()
a = [[x, y, z] for x in music.danceability for y in music.loudness for z in music.artists if((x > 0.8) and (y < -0.5))]
#Below code can be uncommented and used to print all the elements of a
#for i in a:
    #print(i[2])

print(len(a))
#sorted the list in reverse/descending order
a.sort(key=lambda a: (a[0]), reverse=True)
#Print the first and last elements in the sorted list
print("The first track info in sorted is {} and last track info in sorted is: {}".format(a[0], a[(len(a)-1)]))


