"""
Step 4: Saving Your Work (Persistent Database)

This script demonstrates:
- Using PersistentClient to save data permanently to disk
- Creating collections that persist between sessions
- The difference between in-memory and persistent storage
"""

import chromadb
import os

print("="*60)
print("STEP 4: Persistent Database")
print("="*60)

# ============================================================
# Creating a Persistent Client
# ============================================================
print("\n1. Creating PersistentClient...")
print("-"*60)

# Use PersistentClient and give it a path to a folder
# This client will save all data to the "./chroma_db" directory
persistent_client = chromadb.PersistentClient(path="./chroma_db")

print("✓ PersistentClient created")
print(f"  Data will be stored in: {os.path.abspath('./chroma_db')}")

# ============================================================
# Creating a Persistent Collection
# ============================================================
print("\n2. Creating persistent collection...")
print("-"*60)

# Now, creating a collection works the same way, but it will be saved to disk
p_collection = persistent_client.get_or_create_collection(name="saved_policies")

print(f"✓ Collection created: {p_collection.name}")
print(f"  Current count: {p_collection.count()} documents")

# ============================================================
# Adding Data to Persistent Collection
# ============================================================
print("\n3. Adding data to persistent collection...")
print("-"*60)

# Data added to this collection will persist between sessions
p_collection.add(
    ids=["saved_policy_01"],
    documents=["All expense reports must be submitted within 15 days of trip completion."],
    metadatas=[{"policy_type": "expenses", "deadline_days": 15}]
)

print("✓ Added expense policy document")
print(f"  Total documents: {p_collection.count()}")

# Add a few more policies to demonstrate persistence
p_collection.add(
    ids=["saved_policy_02", "saved_policy_03"],
    documents=[
        "Meal allowance is $75 per day for domestic travel and $100 per day for international travel.",
        "All travel bookings must be made at least 14 days in advance for the best rates."
    ],
    metadatas=[
        {"policy_type": "meals", "domestic_allowance": 75, "international_allowance": 100},
        {"policy_type": "booking", "advance_days": 14}
    ]
)

print("✓ Added 2 more policy documents")
print(f"  Total documents: {p_collection.count()}")

# ============================================================
# Querying Persistent Data
# ============================================================
print("\n4. Querying the persistent collection...")
print("-"*60)

results = p_collection.query(
    query_texts=["What is the meal allowance for international trips?"],
    n_results=2
)

print("Query: 'What is the meal allowance for international trips?'\n")
for i, (doc, metadata) in enumerate(zip(results['documents'][0], results['metadatas'][0]), 1):
    print(f"{i}. {results['ids'][0][i-1]}")
    print(f"   Document: {doc}")
    print(f"   Metadata: {metadata}\n")

# ============================================================
# Verification: Data is Saved
# ============================================================
print("="*60)
print("VERIFICATION: Data is persisted to disk")
print("="*60)

print("\n✓ Data has been saved to: ./chroma_db/")
print("✓ If you run this script again, the data will still be there!")
print("✓ You can restart Python and the data will persist.")

# List all collections in the persistent client
all_collections = persistent_client.list_collections()
print(f"\n✓ Collections in persistent database: {len(all_collections)}")
for coll in all_collections:
    print(f"  - {coll.name} ({coll.count()} documents)")

# ============================================================
# SUMMARY
# ============================================================
print("\n" + "="*60)
print("STEP 4 COMPLETE!")
print("="*60)
print("\nKey differences:")
print("  • chromadb.Client() = In-memory (data lost when program ends)")
print("  • chromadb.PersistentClient(path='./chroma_db') = Saved to disk")
print("\n✓ Your data is now permanently saved in the chroma_db folder!")
print("="*60)

