import pandas as pd

def SRS(filepath):
    df = pd.read_csv(filepath, dtype={'AudioMothID' : str, 'StartDateTime' : str, 'Artist' : str})
    df.drop(df[df.AudioMothID == "NA"].index, inplace=True)
    df.drop(df[df.Error == "File is empty"].index, inplace=True)
    df.drop(df[df.Duration == "NA"].index, inplace=True)
    df.drop(df[df.Duration < 60.00025].index, inplace=True)
    df.drop(df[df.AudioMothCode.isin(["AM-21", "AM-19", "AM-8", "AM-28", "AM-18"])].index, inplace=True)
    df['StartDateTime'] = pd.to_datetime(df["StartDateTime"], format="%d.%m.%Y %H:%M")
    df['Hour'] = df['StartDateTime'].dt.hour.tolist()
    df = df.groupby(['AudioMothCode', 'Hour']).sample(1, random_state=1).reset_index()
    if(df.empty):
        return False
    else:
        df.to_csv('SRS.csv')
        return True

print(SRS('Peru_2019_AudioMoth_Data_Full.csv'))