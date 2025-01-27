from flask import Flask, request, render_template
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Initialize Flask app
app = Flask(__name__)

# Load FAISS index
index = faiss.read_index("data/nutrition_index.faiss")
print(f"FAISS index loaded successfully with {index.ntotal} vectors.")

# Load nutrition documents
with open("data/nutrition_documents.txt", "r") as f:
    docs = f.readlines()

# Load Sentence Transformer model
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
print("Sentence Transformer model loaded successfully!")


@app.route("/", methods=["GET", "POST"])
def home():
    results = []  # To store query results
    if request.method == "POST":
        # Get the user query from the form
        query = request.form.get("query", "").strip()

        if query:
            # Generate query embedding
            query_embedding = embedding_model.encode([query])

            # Perform similarity search
            k = 5  # Number of results to retrieve
            distances, indices = index.search(query_embedding, k)

            # Format results for display
            results = [
                {"text": docs[idx].strip(), "distance": distances[0][i]}
                for i, idx in enumerate(indices[0])  # Use indices[0] to access top-k results
            ]
    return render_template("index.html", results=results)  # Corrected template path


if __name__ == "__main__":
    app.run(debug=True)
