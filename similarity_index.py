import faiss
import numpy as np

"""
Index the generated embeddings using FAISS(Facebook AI Similarity Search
Commonly used to index and query high-dimensional data like embeddings.
Indexing (with FAISS in this case) organizes embeddings in a way that makes similarity search efficient, even for large datasets.
"""

# Load saved embeddings
embeddings = np.load("data/nutrition_embeddings.npy")

# Initialize FAISS index
dimension =embeddings.shape[1] # Number of dimensions in each embedding
index = faiss.IndexFlatL2(dimension) # L2 distance (Euclidean)

# Add embeddings to the index
index.add(embeddings)

# Verify the number of vectors in the index
print(f"Number of vectors in the index: {index.ntotal}")

# Save the FAISSNindex to a file
faiss.write_index(index, "nutrition_index.faiss")
print("FAISS index saved sucessfully")
