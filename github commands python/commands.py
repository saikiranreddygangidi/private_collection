import numpy as np
import pandas as pd 
import nltk
import re
import data
df = pd.read_excel ('select.xlsx')
#print (df[["name","Description"]])
lst_stopwords = data.data
def utils_preprocess_text(text, flg_stemm=False, flg_lemm=True, lst_stopwords=None):
    ## clean (convert to lowercase and remove punctuations and   characters and then strip)
    text = re.sub(r'[^\w\s]', '', str(text).lower().strip())
            
    ## Tokenize (convert from string to list)
    lst_text = text.split()
    ## remove Stopwords
    if lst_stopwords is not None:
        lst_text = [word for word in lst_text if word not in 
                    lst_stopwords]
                
    ## Stemming (remove -ing, -ly, ...)
    if flg_stemm == True:
        ps = nltk.stem.porter.PorterStemmer()
        lst_text = [ps.stem(word) for word in lst_text]
                
    ## Lemmatisation (convert the word into root word)
    if flg_lemm == True:
        lem = nltk.stem.wordnet.WordNetLemmatizer()
        lst_text = [lem.lemmatize(word) for word in lst_text]
            
    ## back to string from list
    text = " ".join(lst_text)
    return text
df["text_clean"] = df["Description"].apply(lambda x: utils_preprocess_text(x, flg_stemm=False, flg_lemm=True, lst_stopwords=lst_stopwords))



from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
vect = CountVectorizer()
vect.fit(df["text_clean"])
simple_train_dtm = vect.transform(df["text_clean"])
simple_train_dtm=pd.DataFrame(simple_train_dtm.toarray(), columns=vect.get_feature_names())

#print(simple_train_dtm.shape)

X=simple_train_dtm
Y=list(df["name"].index)

#print(list(Y))


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state=1)



a=[" presence of a common field"]
b=vect.transform(a)


from sklearn.tree import DecisionTreeRegressor
model = DecisionTreeRegressor()
model.fit(X, Y)


y_pred_class = model.predict(X_test)

from sklearn import metrics

print(metrics.r2_score( y_test , y_pred_class))

#print(metrics.confusion_matrix( y_test , y_pred_class.round()))
#print(metrics.classification_report( y_test , y_pred_class))
#y_pred_prob = model.predict_proba(simple_train_dtm[:20])[:, 1]
#print(metrics.roc_auc_score(Y[:30], y_pred_prob))
while(True):
    a=[utils_preprocess_text(input("enter file name") , flg_stemm=False, flg_lemm=True, lst_stopwords=lst_stopwords)]
    b=vect.transform(a)


    print(df.iloc[int(model.predict(b))]["name"])
