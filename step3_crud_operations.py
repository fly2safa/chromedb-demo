"""
Step 3: Managing Your Data (CRUD on Data Points)

This script demonstrates:
- CREATE: Adding documents to the collection
- READ: Querying documents
- UPDATE: Modifying documents with upsert()
- DELETE: Removing documents
"""

import chromadb

# Initialize the ChromaDB client
print("Initializing ChromaDB client...")
client = chromadb.Client()

# Create/get the collection
collection = client.get_or_create_collection(name="travel_policies")
print(f"✓ Collection: {collection.name}\n")

# ============================================================
# CREATE: Adding Documents
# ============================================================
print("="*60)
print("CREATE: Adding travel policy documents")
print("="*60)

collection.add(
    ids=[
        "flight_policy_01",
        "hotel_policy_01",
        "rental_car_policy_01",
        "flight_policy_02"
    ],
    documents=[
        "For domestic flights, employees must book economy class tickets. Business class is only permitted for international flights over 8 hours.",
        "Employees can book hotels up to a maximum of $250 per night in major cities. A list of preferred hotel partners is available.",
        "A mid-size sedan is the standard for car rentals. Upgrades require manager approval. Always select the company's insurance option.",
        "All flights, regardless of destination, must be booked through the official company travel portal, 'Concur'."
    ],
    metadatas=[
        {"policy_type": "flights"},
        {"policy_type": "hotels"},
        {"policy_type": "rental_cars"},
        {"policy_type": "flights", "requires_portal": "True"}
    ]
)

print(f"✓ Added 4 documents to collection")
print(f"  Total documents in collection: {collection.count()}\n")

# ============================================================
# READ: Querying Documents
# ============================================================
print("="*60)
print("READ: Querying for international flight policy")
print("="*60)

results = collection.query(
    query_texts=["What is the policy for international flights?"],
    n_results=2  # Ask for the top 2 most relevant results
)

print(f"Query: 'What is the policy for international flights?'\n")
print(f"Top {len(results['documents'][0])} results:")
for i, (doc, distance) in enumerate(zip(results['documents'][0], results['distances'][0]), 1):
    print(f"\n{i}. Document ID: {results['ids'][0][i-1]}")
    print(f"   Distance (similarity): {distance:.4f}")
    print(f"   Content: {doc[:100]}...")

print("\n")

# ============================================================
# UPDATE: Modifying Documents
# ============================================================
print("="*60)
print("UPDATE: Changing hotel budget and adding train policy")
print("="*60)

collection.upsert(
    ids=["hotel_policy_01", "train_policy_01"],
    documents=[
        "Employees can book hotels up to a maximum of $300 per night. See the portal for preferred partners.",
        "Train travel is encouraged for trips under 4 hours. Business class tickets are approved for all train journeys."
    ],
    metadatas=[
        {"policy_type": "hotels", "max_spend": 300},
        {"policy_type": "train", "last_updated": "2025-10-15"}
    ]
)

print("✓ Updated hotel_policy_01 (increased budget to $300)")
print("✓ Added train_policy_01 (new policy)")
print(f"  Total documents in collection: {collection.count()}\n")

# Verify the update
updated_results = collection.query(
    query_texts=["What is the hotel budget?"],
    n_results=1
)
print(f"Verification query: 'What is the hotel budget?'")
print(f"Result: {updated_results['documents'][0][0]}\n")

# ============================================================
# DELETE: Removing Documents
# ============================================================
print("="*60)
print("DELETE: Removing train policy")
print("="*60)

collection.delete(ids=["train_policy_01"])

print("✓ Deleted train_policy_01")
print(f"  Total documents in collection: {collection.count()}\n")

# ============================================================
# SUMMARY
# ============================================================
print("="*60)
print("STEP 3 COMPLETE!")
print("="*60)
print("\nYou've learned how to:")
print("  ✓ CREATE documents with add()")
print("  ✓ READ documents with query()")
print("  ✓ UPDATE documents with upsert()")
print("  ✓ DELETE documents with delete()")
print(f"\nFinal collection count: {collection.count()} documents")
print("="*60)

