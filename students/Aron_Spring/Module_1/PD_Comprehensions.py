#Pandas code - same as in notebook
import pandas as pd
music = pd.read_csv("featuresdf.csv")

#gaining familarity with CSV
music.head
music.describe()

#comprehension effort
dance_list = [x for x in music.danceability if x > 0.8]
loud_list = [x for x in music.loudness if x < -5.0]

#filtering using Pandas
dance_list = music.danceability >= 0.8
loud_list = music.loudness <= 0.5

#revised review of data filtered lists
dance_list.head(5)
loud_list.head(5)
music.head(5)

#filter in Pandas for danceability and loudness
music[(music.loudness < -5.0) & (music.danceability > 0.8)].sort_values('danceability')

##
#id	name	artists	danceability	energy	key	loudness	mode	speechiness	acousticness	instrumentalness	liveness	valence	tempo	duration_ms	time_signature
#36	7hDc8b7IXETo14hHIHdnh	Passionfruit	Drake	0.809	0.463	11.0	-11.377	1.0	0.0396	0.256000	0.085000	0.1090	0.364	111.980	298941.0	4.0
#84	3QwBODjSEzelZyVjxPOHd	Otra Vez (feat. J Balvin)	Zion & Lennox	0.832	0.772	10.0	-5.429	1.0	0.1000	0.055900	0.000486	0.4400	0.704	96.016	209453.0	4.0
#14	0VgkVdmE4gld66l8iyGjg	Mask Off	Future	0.833	0.434	2.0	-8.795	1.0	0.4310	0.010200	0.021900	0.1650	0.281	150.062	204600.0	4.0
#38	6EpRaXYhGOB3fj4V2uDkM	Strip That Down	Liam Payne	0.869	0.485	6.0	-5.595	1.0	0.0545	0.246000	0.000000	0.0765	0.527	106.028	204502.0	4.0
#62	00lNx0OcTJrS3MKHcB80H	You Don't Know Me - Radio Edit	Jax Jones	0.876	0.669	11.0	-6.054	0.0	0.1380	0.163000	0.000000	0.1850	0.682	124.007	213947.0	4.0
#94	2fQrGHiQOvpL9UgPvtYy6	Bank Account	21 Savage	0.884	0.346	8.0	-8.228	0.0	0.3510	0.015100	0.000007	0.0871	0.376	75.016	220307.0	4.0
#5	7KXjTSCq5nL1LoYtL7XAw	HUMBLE.	Kendrick Lamar	0.904	0.611	1.0	-6.842	0.0	0.0888	0.000259	0.000020	0.0976	0.400	150.020	177000.0	4.0
#48	4Km5HrUvYTaSUfiSGPJeQ	Bad and Boujee (feat. Lil Uzi Vert)	Migos	0.927	0.665	11.0	-5.313	1.0	0.2440	0.061000	0.000000	0.1230	0.175	127.076	343150.0	4.0
#51	343YBumqHu19cGoGARUTs	Fake Love	Drake	0.927	0.488	9.0	-9.433	0.0	0.4200	0.108000	0.000000	0.1960	0
##

