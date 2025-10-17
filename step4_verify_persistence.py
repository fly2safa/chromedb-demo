"""
Step 4 Verification: Check if data persists between runs

This script checks the persistent database without modifying it.
"""

import chromadb

print("="*60)
print("VERIFYING PERSISTENT DATA")
print("="*60)

# Connect to the existing persistent database
persistent_client = chromadb.PersistentClient(path="./chroma_db")

# Get the existing collection (don't create if it doesn't exist)
try:
    p_collection = persistent_client.get_collection(name="saved_policies")
    
    print(f"\n✓ Collection 'saved_policies' found!")
    print(f"  Total documents: {p_collection.count()}")
    
    # Show all document IDs
    all_data = p_collection.get()
    print(f"\n  Document IDs in collection:")
    for doc_id in all_data['ids']:
        print(f"    - {doc_id}")
    
    # Query to verify data
    print(f"\n  Sample documents:")
    for i, (doc_id, doc) in enumerate(zip(all_data['ids'], all_data['documents'])):
        print(f"\n  {i+1}. ID: {doc_id}")
        print(f"     Content: {doc}")
    
    print("\n" + "="*60)
    print("✓ DATA HAS PERSISTED!")
    print("="*60)
    
except Exception as e:
    print(f"\n✗ Collection not found or error: {e}")
    print("\nThis might mean:")
    print("  - You haven't run step4_persistent_database.py yet")
    print("  - The data didn't persist properly")

