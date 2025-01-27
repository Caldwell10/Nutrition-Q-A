from sentence_transformers import SentenceTransformer
from text_document import docs
import numpy as np

"""
Embeddings are the numerical representations of the text documents. 
Each embedding is a high-dimensional vector that encodes the semantic meaning of a document
"""

# Load the Sentence Transformer model
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# Confirm model is ready
print("Model loaded successfully!")

# Generate embeddings for the documents
embedding = embedding_model.encode(docs, show_progress_bar=True)

# Save embeddings for reuse
np.save("data/nutrition_embeddings.npy", embedding)
# Load documents
with open("data/nutrition_documents.txt", "w") as file:
    for doc in docs:
        file.write(doc +"\n")

print("Embeddings generated and saved! ")