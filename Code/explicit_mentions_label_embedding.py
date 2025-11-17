import json
import numpy as np



LabelEmbedding={}
label_path=""

def compute_label_embedding(embed):
    print("inside label embedding")
    with open(label_path+"Keyword_BengaliNews.json", "r") as f:
        key = json.loads(f.read())
    with open(label_path + "News_Articles_Explicit_Label_Annotated.json", "r") as f:
        data = json.loads(f.read())
        for i in range(0, len(key)):
            count=0
            label_embedding = 0
            label = key[i]['Keyword'][0]
            for l in range(0, len(data)):
               if label in data[l]['Explicit Article Label']:
                 label_embedding+=embed([data[l]['Article Text']])
                 count+=1
            if count > 0:
               LabelEmbedding[label]= label_embedding/count
            else:
               for j in range(0, len(key[i]['Keyword'])):
                    label_embedding+= embed([key[i]['Keyword'][j]])
               LabelEmbedding[label] = label_embedding / len(key[i]['Keyword'])
    return LabelEmbedding

