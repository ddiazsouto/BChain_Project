import seedphrase_gen as sp
import Username_Generator as ug
import pandas as pd
import random
from os import getenv

#df = pd.DataFrame(columns= ['username','password','mnemonic'])

def json_parser():
    df = pd.DataFrame(columns= ['username','password','mnemonic'])
    df_words = pd.read_json(sp.word_positioner(),orient='columns').sort_values(by='sp_order')
    df_usnpwd = pd.read_json(ug.usn_pwd())
    user_name = df_usnpwd.username[0] + str(random.randint(1000000000, 9999999999))
    if len(df.loc[df.username == user_name]) == 0: 
    
    #connect_string =getenv('DATABASE_URI')
    #sql_engine = sql.create_engine(connect_string)
    #df = pd.read_sql_table('credentials', sql_engine)
    # if len(df.loc[df.username == user_name]) == 0:
    
        seedphrase = '' 
        for w in df_words.sp_words:
            seedphrase = seedphrase + w + '_'
        df_usnpwd['mnemonic'] = seedphrase
        df = df.append(df_usnpwd,ignore_index=True)
        print(len(df))
        # new_user = credentials(username = df_usnpwd.username[0], password = df_usnpwd.password[0], mnemonic = df_usnpwd.mnemonic[0])
    
        return df
    else:
        while len(df.loc[df.username == user_name]) > 0:
            user_name = df_usnpwd.username[0] + str(random.randint(1000000000, 9999999999))
        
        seedphrase = '' 
        for w in df_words.sp_words:
            seedphrase = seedphrase + w + '_'
        df_usnpwd['mnemonic'] = seedphrase
        df = df.append(df_usnpwd, ignore_index=True)
        
        return df.T