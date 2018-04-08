import pandas as pd

# pandas options
pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

def run_analysis():
    try:
        df_music = pd.read_csv('featuresdf.csv')

        print ('data types')
        print (df_music.dtypes)
        print('frist five rows')
        print(df_music.head(5))
        print('\n')

    except FileNotFoundError as e:
        print ('error: {}'.format(e))

    #Question how would I select column name only after running my filter? The only way I found is commmented out below.
    df_danceability = df_music[(df_music['danceability'] > 0.8) & (df_music['loudness'] < -5.0)].sort_values(by=['danceability'],ascending=False)

    # df_danceability = df_danceability[['name']]

    print (df_danceability.head(5))

if __name__ == "__main__":
    run_analysis()





