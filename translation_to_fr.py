import pandas as pd

file = "/Users/leli/Downloads/trainingandtestdata/training.1600000.processed.noemoticon.csv"

df = pd.read_csv(file, sep =  ",", encoding= 'ISO-8859-1')

df.columns = ['target', 'id', 'date', 'flag',  'user', 'text'] #(0 = negative, 2 = neutral, 4 = positive)


eng_tweets = df['text'].tolist()

del df


from googletrans import Translator


fr_tweets = []

for original in eng_tweets[0:5]:
    translator = Translator()

    try:
        r = translator.translate(original, dest='fr')
        fr_tweets.append(r.text)
        #fr_tweets.append(translator.translate(original, dest='fr').text)
    except:
        fr_tweets.append('')
    
    
    





df['translated_text'] = pd.Series(fr_tweets, index = df.index)


translated = "/Users/leli/Downloads/trainingandtestdata/training.1600000.processed.noemoticon_translated.csv"

df.to_csv(translated, sep = ",")
    
