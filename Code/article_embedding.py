import json


ArticleEmbedding=[]
dataset_path=""

def compute_article_embedding(embed):
    with open(dataset_path+"NewsBlog_ProthomAlo_Dataset.json", "r") as f:
        data = json.loads(f.read())
        for l in range(0,len(data)):
            article=dict()
            print("Article number:",l)
            article['Article Text'] = data[l]['Article Text']
            article['Article Embedding']=embed([data[l]['Article Text']])
            article['Label'] = data[l]['Concept']
            ArticleEmbedding.append(article)
    return ArticleEmbedding
