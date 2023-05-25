import pandas as pd
import re
import snowballstemmer

df=pd.read_csv("data/nlp.csv",index_col=0)

#sayılar değerlerin kaldırılması

def remove_numeric(value):
    bfr=[item for item in value if not item.isdigit()]

    bfr="".join(bfr)
    return bfr
#emojileri kaldırma

def remove_emoji(value):
    bfr=re.compile("[\U00010000-\U0010ffff]",flags=re.UNICODE)
    bfr=bfr.sub(r'',value)
    return bfr


#tek karakterli harflerin kaldırılması

def remove_single_character(value):
    return re.sub(r'\b\w\b', '', value)

#noktalama işaretlerini kaldırma

def remove_noktalama(value):
    return re.sub(r'[^\w\s]', '', value)


#linklerin kaldırılması

def remove_link(value):
    return re.sub(r'(https?://\S+)|(www\.\S+)', '', value)


#hastagların kaldırılması

def remove_hashtag(value):
    return re.sub(r'#\w+', '', value)

#kullanıcı adını kaldırma

def remove_username(value):
        return re.sub(r'@\w+', '', value)



def stem_word(value):
    stemmer=snowballstemmer.stemmer("turkish")
    value=value.lower()
    value=stemmer.stemWords(value.split())
    stop_words=['acaba','ama','aslında','az','bazı','belki']
    
    value=[item for item in value if not item in stop_words]
    value=' '.join(value)
    return value

def pre_processing(value):
    return [remove_numeric(remove_emoji
                          (remove_single_character
                           (remove_noktalama
                            (remove_link
                             (remove_hashtag
                              (remove_username
                               (stem_word(word)))))))) for word in value.split()]
    


def remove_space(value):
    return [item for item in value if item.strip()]
