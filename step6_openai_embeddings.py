"""
Step 6: Advanced - Using OpenAI's Embedding Model

This script demonstrates:
- Installing and using OpenAI and tiktoken libraries
- Counting tokens with tiktoken
- Creating collections with OpenAI embedding functions
- Querying with OpenAI embeddings

PREREQUISITES:
1. Install libraries: pip install openai tiktoken
2. Set your OpenAI API key as an environment variable:
   - Windows: set OPENAI_API_KEY=your-api-key-here
   - Mac/Linux: export OPENAI_API_KEY=your-api-key-here
   - Or set it in this script (not recommended for production)
"""

import os
import sys

print("="*60)
print("STEP 6: Using OpenAI's Embedding Model")
print("="*60)

# ============================================================
# 1. Check for Required Libraries
# ============================================================
print("\n1. Checking required libraries...")
print("-"*60)

try:
    import tiktoken
    print("[OK] tiktoken is installed")
except ImportError:
    print("[ERROR] tiktoken is NOT installed")
    print("\nPlease install it with:")
    print("  pip install tiktoken")
    sys.exit(1)

try:
    import openai
    print("[OK] openai is installed")
except ImportError:
    print("[ERROR] openai is NOT installed")
    print("\nPlease install it with:")
    print("  pip install openai")
    sys.exit(1)

# ============================================================
# 2. Check for OpenAI API Key
# ============================================================
print("\n2. Checking for OpenAI API key...")
print("-"*60)

# ChromaDB looks for CHROMA_OPENAI_API_KEY or OPENAI_API_KEY
api_key = os.environ.get('OPENAI_API_KEY') or os.environ.get('CHROMA_OPENAI_API_KEY')

if not api_key:
    print("[ERROR] OPENAI_API_KEY environment variable is NOT set")
    print("\nTo set your API key:")
    print("  Windows (Command Prompt): set OPENAI_API_KEY=your-key-here")
    print("  Windows (PowerShell):     $env:OPENAI_API_KEY='your-key-here'")
    print("  Mac/Linux/Git Bash:       export OPENAI_API_KEY=your-key-here")
    print("\nOr uncomment and edit this line in the script:")
    print("  # os.environ['OPENAI_API_KEY'] = 'your-key-here'")
    print("\n[WARNING] Get your API key from: https://platform.openai.com/api-keys")
    sys.exit(1)
else:
    # ChromaDB specifically needs CHROMA_OPENAI_API_KEY
    os.environ['CHROMA_OPENAI_API_KEY'] = api_key
    print(f"[OK] API key found (starts with: {api_key[:8]}...)")
    print("[OK] Set CHROMA_OPENAI_API_KEY for ChromaDB")

# ============================================================
# 3. Understanding Tokens with tiktoken
# ============================================================
print("\n3. Counting tokens with tiktoken...")
print("-"*60)

# text-embedding-3-small uses the cl100k_base encoding
encoding = tiktoken.get_encoding("cl100k_base")

sample_texts = [
    "This is a sample sentence.",
    "For domestic flights, employees must book economy class tickets.",
    "Employees can book hotels up to a maximum of $300 per night."
]

print("\nToken counts for sample texts:")
for text in sample_texts:
    tokens = encoding.encode(text)
    token_count = len(tokens)
    print(f"  Text: '{text[:50]}...'")
    print(f"  Token count: {token_count}")
    print(f"  First few tokens: {tokens[:10]}\n")

# ============================================================
# 4. Create Collection with OpenAI Embedding Function
# ============================================================
print("4. Creating collection with OpenAI embeddings...")
print("-"*60)

import chromadb
from chromadb.utils import embedding_functions

# Create an embedding function using OpenAI's model
openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    model_name="text-embedding-3-small"
)

print("[OK] Created OpenAI embedding function")
print("  Model: text-embedding-3-small")

# Initialize ChromaDB client
client = chromadb.Client()

# Create a new collection with OpenAI embedding function
openai_collection = client.get_or_create_collection(
    name="travel_policies_openai",
    embedding_function=openai_ef
)

print(f"[OK] Created collection: {openai_collection.name}")

# ============================================================
# 5. Add Documents with OpenAI Embeddings
# ============================================================
print("\n5. Adding documents (using OpenAI to create embeddings)...")
print("-"*60)

openai_collection.add(
    ids=["flight_policy_01", "hotel_policy_01", "rental_car_policy_01"],
    documents=[
        "For domestic flights, employees must book economy class tickets. Business class is only permitted for international flights over 8 hours.",
        "Employees can book hotels up to a maximum of $300 per night. See the portal for preferred partners.",
        "A mid-size sedan is the standard for car rentals. Upgrades require manager approval."
    ],
    metadatas=[
        {"policy_type": "flights"},
        {"policy_type": "hotels"},
        {"policy_type": "rental_cars"}
    ]
)

print("[OK] Added 3 documents to collection")
print(f"  Total documents: {openai_collection.count()}")
print("  Note: OpenAI API was called to generate embeddings")

# ============================================================
# 6. Query with OpenAI Embeddings
# ============================================================
print("\n6. Querying with OpenAI embeddings...")
print("-"*60)

# Query will also use OpenAI to embed the query text
results = openai_collection.query(
    query_texts=["What is the hotel budget?"],
    n_results=2
)

print("Query: 'What is the hotel budget?'\n")
print(f"Top {len(results['documents'][0])} results:")
for i, (doc, distance, metadata) in enumerate(zip(
    results['documents'][0], 
    results['distances'][0],
    results['metadatas'][0]
), 1):
    print(f"\n{i}. Document ID: {results['ids'][0][i-1]}")
    print(f"   Distance: {distance:.4f}")
    print(f"   Policy Type: {metadata['policy_type']}")
    print(f"   Content: {doc[:80]}...")

# ============================================================
# Comparison with Default Embeddings
# ============================================================
print("\n" + "="*60)
print("COMPARISON: OpenAI vs Default Embeddings")
print("="*60)

print("\nOpenAI Embeddings (text-embedding-3-small):")
print("  + More powerful and accurate")
print("  + Better at understanding context and nuance")
print("  + Costs money (but very affordable)")
print("  + Requires API key and internet connection")

print("\nDefault Embeddings (ChromaDB's built-in):")
print("  + Free and local")
print("  + No API key needed")
print("  + Works offline")
print("  + Good for most use cases")

# ============================================================
# SUMMARY
# ============================================================
print("\n" + "="*60)
print("STEP 6 COMPLETE!")
print("="*60)
print("\nYou've learned:")
print("  + How to count tokens with tiktoken")
print("  + How to use OpenAI's embedding models with ChromaDB")
print("  + The difference between OpenAI and default embeddings")
print("\n*** Congratulations! You've completed all 6 steps! ***")
print("="*60)

