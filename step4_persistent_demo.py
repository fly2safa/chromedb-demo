"""
Step 4: Persistent Database - Smart Demo

This script demonstrates persistence by checking if data exists first.
"""

import chromadb

print("="*60)
print("STEP 4: Persistent Database (Smart Demo)")
print("="*60)

# Create persistent client
persistent_client = chromadb.PersistentClient(path="./chroma_db")

# Get or create collection
p_collection = persistent_client.get_or_create_collection(name="saved_policies")

print(f"\n✓ Connected to collection: {p_collection.name}")
print(f"  Current document count: {p_collection.count()}")

# Check if data already exists
existing_data = p_collection.get()
existing_ids = existing_data['ids']

if len(existing_ids) > 0:
    print("\n✓ DATA ALREADY EXISTS (Persistence confirmed!)")
    print(f"  Found {len(existing_ids)} existing documents:")
    for doc_id in existing_ids:
        print(f"    - {doc_id}")
    print("\n  Skipping data insertion (already exists)")
else:
    print("\n  No existing data found. Adding new documents...")
    
    # Add data only if it doesn't exist
    p_collection.add(
        ids=["saved_policy_01", "saved_policy_02", "saved_policy_03"],
        documents=[
            "All expense reports must be submitted within 15 days of trip completion.",
            "Meal allowance is $75 per day for domestic travel and $100 per day for international travel.",
            "All travel bookings must be made at least 14 days in advance for the best rates."
        ],
        metadatas=[
            {"policy_type": "expenses", "deadline_days": 15},
            {"policy_type": "meals", "domestic_allowance": 75, "international_allowance": 100},
            {"policy_type": "booking", "advance_days": 14}
        ]
    )
    
    print(f"  ✓ Added 3 documents")

# Query the data (works whether it's new or existing)
print("\n" + "-"*60)
print("Querying: 'What is the meal allowance?'")
print("-"*60)

results = p_collection.query(
    query_texts=["What is the meal allowance?"],
    n_results=1
)

print(f"\nTop result:")
print(f"  ID: {results['ids'][0][0]}")
print(f"  Document: {results['documents'][0][0]}")
print(f"  Metadata: {results['metadatas'][0][0]}")

print("\n" + "="*60)
print("STEP 4 COMPLETE!")
print("="*60)
print("\n✓ Data persists in ./chroma_db/")
print("✓ Run this script multiple times - data will remain!")
print("="*60)

