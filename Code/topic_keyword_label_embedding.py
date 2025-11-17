import json
import numpy as np


LabelEmbedding={}
label_path=""

def compute_label_embedding(embed):
    print("inside label embedding")
    with open(label_path+"Keyword_Keyword_BengaliNews.json", "r") as f:
        key = json.loads(f.read())
        for i in range(0, len(key)):
            label_embedding = 0
            label = key[i]['Keyword'][0]
            for j in range(0, len(key[i]['Keyword'])):
                 label_embedding+= embed([key[i]['Keyword'][j]])
            LabelEmbedding[label] = label_embedding / len(key[i]['Keyword'])
    return LabelEmbedding
