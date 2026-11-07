from sentence_transformers import SentenceTransformer, util
# faiss: Facebook's library for fast vector similarity search
import faiss
# numpy: handles the arrays of numbers (vectors)
import numpy as np
# ══ SECTION 2: LOAD THE EMBEDDING MODEL ════════════════════════════════
# Load a small, fast, free model — downloads once (~90MB), then cached
# all-MiniLM-L6-v2 produces 384-dimensional vectors for any sentence
model = SentenceTransformer('all-MiniLM-L6-v2')
print("✅ Model loaded!")
# ══ SECTION 3: CREATE YOUR FIRST EMBEDDINGS ════════════════════════════
# These are the sentences we want to embed (convert to vectors)
sentences = [
    "I love cats and dogs",         # index 0
    "Pets are wonderful companions",  # index 1 — similar to 0
    "Python is great for coding",     # index 2
    "I enjoy programming in Python",  # index 3 — similar to 2
    "The sky is blue today",          # index 4 — unrelated to both
]
# .encode() converts each sentence into a numpy array of 384 numbers
# This is the "meaning" of each sentence captured as coordinates
embeddings = model.encode(sentences)
# Print the shape: (5 sentences, 384 numbers each)
print(f"\n📐 Embedding shape: {embeddings.shape}")
print(f"   Each sentence = {embeddings.shape[1]} numbers (dimensions)\n")
# ══ SECTION 4: COSINE SIMILARITY ═══════════════════════════════════════
# Cosine similarity: measures how "close" two vectors are
# Returns a value between 0 (totally different) and 1 (identical meaning)
# Compare sentence 0 ("I love cats") with sentence 1 ("Pets are wonderful")
sim_close = util.cos_sim(embeddings[0], embeddings[1])
print(f"🟢 'cats/dogs' vs 'pets': similarity = {sim_close.item():.3f}")
# Compare sentence 0 ("I love cats") with sentence 4 ("sky is blue")
sim_far = util.cos_sim(embeddings[0], embeddings[4])
print(f"🔴 'cats/dogs' vs 'sky is blue': similarity = {sim_far.item():.3f}")
# The first score should be MUCH higher — that's semantic similarity!
# ══ SECTION 5: BUILD A FAISS VECTOR SEARCH INDEX ════════════════════════
# Our "document database" — imagine these are chunks from a big PDF
documents = [
    "Employees are entitled to 18 days of annual leave per year",
    "The company provides health insurance to all full-time staff",
    "Python was created by Guido van Rossum in 1991",
    "Machine learning is a subset of artificial intelligence",
    "Hyderabad is famous for its biryani and pearls",
    "You can take vacation days after completing 6 months of service",
    "Large language models are trained on billions of text tokens",
    "The office is located in the HITEC City area of Hyderabad",
    "GenAI engineers are in high demand across the tech industry",
    "Time off requests must be submitted 2 weeks in advance",
]
# Convert all documents to embedding vectors
# convert_to_numpy=True ensures we get numpy arrays (FAISS needs this)
doc_embeddings = model.encode(documents, convert_to_numpy=True)

# Get the number of dimensions (384 for this model)
dimension = doc_embeddings.shape[1]

# Create a FAISS index using L2 (Euclidean) distance
# IndexFlatL2 = simple but accurate — good for small datasets
index = faiss.IndexFlatL2(dimension)

# Add all document vectors to the FAISS index
# FAISS stores them in a way that allows super-fast search
index.add(doc_embeddings)

print(f"\n✅ FAISS index built with {index.ntotal} documents\n")

# ══ SECTION 6: SEMANTIC SEARCH ══════════════════════════════════════════

# The user's question — notice we use different words than the documents!
# "time off" is NOT in the documents, but "annual leave" and "vacation days" are
query = "How many days of time off do I get?"

# Convert the query to an embedding vector (same model = same space)
query_embedding = model.encode([query], convert_to_numpy=True)

# Search FAISS for the k=3 most similar documents
# Returns: distances (how far) and indices (which documents)
k = 3   # number of results to return
distances, indices = index.search(query_embedding, k)

# Print the search results
print(f"🔍 Query: '{query}'\n")
print("📋 Top 3 most semantically similar documents:\n")

# Loop through the results and print each one with its distance score
for rank, (idx, dist) in enumerate(zip(indices[0], distances[0]), 1):
    # Lower distance = more similar (opposite of cosine similarity)
    print(f"  {rank}. [{dist:.3f}] {documents[idx]}")

# ✨ Notice: "annual leave" and "vacation days" are found even though
# the query said "time off" — that's the magic of semantic search!
print("\n✨ Found relevant docs using MEANING, not just keywords!")