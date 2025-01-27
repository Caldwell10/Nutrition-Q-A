import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from text_document import docs
# Load FAISS index
index = faiss.read_index("data/nutrition_index.faiss")
print(f"FAISS index loaded successfully with {index.ntotal} vectors.")

# Load Sentence Transformer model
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
print("Sentence Transformer model loaded successfully!")

# Loop to handle multiple queries
while True:
    # User inputs a query
    query = input("\nEnter your query(or type 'exit' to quit): ").strip()

    # Exit condition
    if query.lower() == 'exit':
        print("Exiting. Thank you for using the system!")
        break

    # Check for empty input
    if not query:
        print("Query cannot be empty. Please try again.")
        continue

    # Generate embedding for the query
    query_embedding= embedding_model.encode([query])



    # Perform similarity search
    k=5 # Number of results to retrieve
    distance, indices = index.search(query_embedding, k)

    # Display the top results
    print("\n================ Top Results ================\n")
    for i, idx in enumerate(indices[0]):
        print(f"{i+1}: {docs[idx].strip()}(Distance: {distance[0][i]})")

