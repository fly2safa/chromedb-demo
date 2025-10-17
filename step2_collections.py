"""
Step 2: Creating Your First "Filing Cabinet" (Collection)

This script demonstrates how to:
- Initialize ChromaDB client
- Create a collection
"""

import chromadb

# Initialize the ChromaDB client. This creates an in-memory database.
print("Initializing ChromaDB client...")
client = chromadb.Client()
print("✓ Client initialized")

# Create a new collection or get it if it already exists.
print("\nCreating 'travel_policies' collection...")
collection = client.get_or_create_collection(name="travel_policies")
print(f"✓ Collection created: {collection.name}")
print(f"  Collection count: {collection.count()} documents")

print("\n" + "="*50)
print("Step 2 Complete! Collection is ready for data.")
print("="*50)

