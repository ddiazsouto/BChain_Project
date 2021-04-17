import random
import BChain_WordList as bwords
import pandas as pd

def mnemonic_generator():
    seedphrase_words = []

    while len(seedphrase_words) < 12:
        seedphrase_words.append(bwords.wordlist[random.randint(0,len(bwords.wordlist)-1)])
    series = pd.Series(seedphrase_words,  name="sp_words").reset_index().drop(columns='index')
    return series.to_json()