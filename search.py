from sentence_transformers import SentenceTransformer
import json
from sklearn.neighbors import NearestNeighbors
import pandas as pd

model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

with open('catecismo.json','r',encoding = 'utf-8') as f:
    parags = list(json.load(f).values())

embeds = pd.read_csv('embeddings.csv')
nbrs = NearestNeighbors(n_neighbors = 3, algorithm = 'ball_tree').fit(embeds.values)

def ask(pergunta):
    if not pergunta:
        return []
    enc = model.encode([pergunta])
    distances,indices = nbrs.kneighbors(enc)
    return [parags[i] for i in indices[0]]