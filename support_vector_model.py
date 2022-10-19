import pandas as pd
import numpy as np
import sklearn
import pickle
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_excel(r"C:\Appuzzz\University\Final_project\new-david-dataset.xlsx")
print(df.head())
df2 = df
df2["combined_string"] = df2.Diseases.map(str) + " " + df2.Sym_1 + " " + df2.Sym_2 + " " + df2.Sym_3 + " " + df2.Sym_4 + " " + df2.Sym_5 + " " + df2.Sym_6 + " " + df2.Sym_7 + " " + df2.Sym_8
df3 = df2.drop(['Sym_1','Sym_2','Sym_3','Sym_4','Sym_5','Sym_6','Sym_7','Sym_8',
               'Count','Dept. ','Unnamed: 10','Diseases'],axis = 1)
print(df3.head())

X_train, X_test, y_train, y_test = train_test_split(
    df3.combined_string,
    df3.Directed,
    test_size=0.20, # 20% samples will go to test dataset
    random_state=2022,
    stratify=df3.Directed
)

from sklearn.svm import SVC
svc_tfid_model1 = Pipeline([
     ('vectorizer_tfidf',TfidfVectorizer()),
     ('Support Vector', SVC())
])

#2. fit with X_train and y_train
svc_tfid_model1.fit(X_train, y_train)


#3. get the predictions for X_test
y_pred = svc_tfid_model1.predict(X_test)


#4. print the classfication report
print(classification_report(y_test, y_pred))

with open('support_vector_model_pkl', 'wb') as files:
    pickle.dump(svc_tfid_model1, files)