
#import necessary libraries 
#use the required .py file for label embedding topic_keyword or explicit_mentions
import topic_keyword_label_embedding
import explicit_mentions_label_embedding
import article_embedding
import json
import numpy as np
from scipy import spatial



dataset_path=""
result_path=""


#Load the model here
model = " "

# Load the tokenizer here if needed
tokenizer = " "

#LaBSE implementation
# model = SentenceTransformer('sentence-transformers/LaBSE')

#LASER implementation
# laser = Laser()

# Bangla transformer implementation
# transformer=Bangla_sentence_transformer_small()


#Bloom implementation
# tokenizer = AutoTokenizer.from_pretrained("bigscience/bloomz-1b1")
# model = BloomModel.from_pretrained("bigscience/bloomz-1b1")


#Flan-UL2 implementation
# model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-ul2")
# tokenizer = AutoTokenizer.from_pretrained("google/flan-ul2")

#GPTNeoX implementation
# tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neox-20b")
# model = GPTNeoXModel.from_pretrained("EleutherAI/gpt-neox-20b")


LabelEmbedding= topic_keyword_label_embedding.compute_label_embedding(model)
ArticleEmbedding= article_embedding.compute_article_embedding(model)

for threshold in np.arange(0.0,1.0,0.05):
        final_article_list = []
        print("Threshold running for::",threshold)
        filename = str(threshold) + '_NewsBlog_ProthomAlo_Dataset.json'
        for i in range(0, len(ArticleEmbedding)):
            inferred_label=[]
            final_article = {}
            for label in LabelEmbedding:
                cosine_dist = 1 - spatial.distance.cosine(LabelEmbedding[label], ArticleEmbedding[i]['Article Embedding'])
                if (cosine_dist > threshold):
                    inferred_label.append(label)
            final_article['Article Text'] = ArticleEmbedding[i]['Article Text']
            final_article['Inferred Article Label'] = inferred_label # inferred labels
            final_article['Label'] = ArticleEmbedding[i]['Label']  # ground truth labels added for evaluation
            final_article_list.append(final_article)

        with open(result_path+filename, 'w+', newline='\n') as f:
                    print("writing json::",filename)
                    json.dump(final_article_list, f, indent=4, separators=(',', ':'))

