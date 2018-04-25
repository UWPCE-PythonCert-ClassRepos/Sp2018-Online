import csv

def readfile(file):
    for line in open(file):
        yield line
        
def printlines(lines):
    music_list = []  # empty list
    for line in lines:
        song = [x.strip() for x in line.split(',')]
        if song[2] == 'Ed Sheeran':
            print (song)
            music_list.append(song)
    return music_list

def run_fav_artist(filename):
    try:
        lines = readfile(filename)
        fav_artist = printlines(lines)
        return fav_artist

    except FileNotFoundError as e:
        print ('error: {}'.format(e))

def high_energy_level(level):
    def energy_check(line):
        if float(line[4]) > level:
            return line[0:5]
    return energy_check

def run_high_energy_tracks(filename):
    # level of 8
    energy_level_8 = high_energy_level(0.8)

    with open(filename) as file:
        reader = csv.reader(file)
        next(reader, None)  # skip the headers
        for line in reader:
            resutl = energy_level_8(line)
            if resutl is not None:
                print (resutl)


if __name__ == "__main__":
    #generator
    print ("Generator Results")
    run_fav_artist('featuresdf.csv')
    #closure
    print("Closure Results")
    run_high_energy_tracks('featuresdf.csv')






