import pandas as pd

def find_favorite(name):
	"""
	find and print all favorite artist's tracks
	"""
	i = 0
	while i < len(music):
		if music['artists'][i] == name:
			yield music['name'][i]
		i += 1

print('-'*10+'Generators'+'-'*10)
music = pd.read_csv('featuresdf.csv')
a = find_favorite('Luis Fonsi')
print(list(a))

def capture_highenergy(number):
	"""
	capture high energy tracks using Closures
	"""
	def capture_function(res):
		if res > number:
			return True
		else:
			return False
	return capture_function

highenergy = capture_highenergy(0.8)

def generator_highenergy(res):
	i = 0
	while i < len(res):
		if highenergy(res['energy'][i]):
			yield res['name'][i]+' by '+res['artists'][i] 
		i += 1

print('-'*10+'Closures'+'-'*10)
b = generator_highenergy(music)
print(list(b))
