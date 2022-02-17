import pickle
import pandas as pd
import scipy.sparse
import re

tokenizer1 = open("./tfidf.pkl","rb")
tokenizer1 = pickle.load(tokenizer1)
model = open("./MNBModel.pkl", "rb")
model = pickle.load(model)
    
def priorityEncoder(priority):
    if priority == 'P1 - Urgent':
        return [1,0,0]
    elif priority == 'P2 - High':
        return [0,1,0]
    elif priority == 'P3 - Medium':
        return [0,0,1]
    else :
        return [0,0,0]
    
def Test_project(desc, app, prio):
    desc = re.sub('<[^<]+?>', '', desc)
    desc = re.sub(r'https?:\/\/.*[\r\n]*', '', desc, flags=re.MULTILINE)
    desc= re.sub("\n+\r", "", desc)
    desc = pd.Series(desc)
    desc = tokenizer1.transform(desc)
    prio = priorityEncoder(prio)
    pred = model.predict(desc)[0]
    prob = model.predict_proba(desc)[0]
    if pred =='Valid':
        prob = prob[1]
    else:
        prob = prob[0]
    prob = round(prob*100, 2)
    return pred, prob