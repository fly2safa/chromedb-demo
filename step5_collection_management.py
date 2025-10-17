"""
Step 5: Managing Collections (CRUD on Collections)

This script demonstrates:
- CREATE: Creating collections (we've already done this)
- READ: Listing all collections
- UPDATE: Modifying collection name/metadata
- DELETE: Removing collections
"""

import chromadb

print("="*60)
print("STEP 5: Managing Collections (CRUD)")
print("="*60)

# Initialize client (using regular client for demo purposes)
client = chromadb.Client()

# ============================================================
# CREATE: Create some sample collections
# ============================================================
print("\n1. CREATE: Setting up sample collections...")
print("-"*60)

collection1 = client.get_or_create_collection(name="travel_policies")
collection2 = client.get_or_create_collection(name="hr_policies")
collection3 = client.get_or_create_collection(name="it_policies")

# Add some sample data to make them interesting
collection1.add(ids=["doc1"], documents=["Sample travel policy"])
collection2.add(ids=["doc1"], documents=["Sample HR policy"])
collection3.add(ids=["doc1"], documents=["Sample IT policy"])

print("✓ Created 3 collections:")
print("  - travel_policies")
print("  - hr_policies")
print("  - it_policies")

# ============================================================
# READ: List All Collections
# ============================================================
print("\n2. READ: Listing all collections...")
print("-"*60)

all_collections = client.list_collections()

print(f"✓ Found {len(all_collections)} collections:\n")
for coll in all_collections:
    print(f"  - {coll.name} ({coll.count()} documents)")

# ============================================================
# UPDATE: Modify a Collection
# ============================================================
print("\n3. UPDATE: Modifying a collection...")
print("-"*60)

# Get the collection we want to modify
collection_to_update = client.get_collection(name="travel_policies")

print(f"  Original name: {collection_to_update.name}")

# Rename it
collection_to_update.modify(name="legacy_travel_policies")

print(f"  ✓ Renamed to: legacy_travel_policies")

# Verify the change by listing collections again
all_collections_after = client.list_collections()
print(f"\n  Collections after rename:")
for coll in all_collections_after:
    print(f"    - {coll.name}")

# ============================================================
# UPDATE: Modify Collection Metadata
# ============================================================
print("\n4. UPDATE: Adding metadata to collection...")
print("-"*60)

# You can also modify collection metadata
collection_to_update.modify(
    metadata={"description": "Archived travel policies from 2024"}
)

print("  ✓ Added metadata: {'description': 'Archived travel policies from 2024'}")

# Get the collection again to see metadata
updated_coll = client.get_collection(name="legacy_travel_policies")
print(f"  Metadata: {updated_coll.metadata}")

# ============================================================
# DELETE: Remove a Collection
# ============================================================
print("\n5. DELETE: Removing a collection...")
print("-"*60)

print("  Deleting 'it_policies' collection...")

# Delete the collection
client.delete_collection(name="it_policies")

print("  ✓ Collection deleted")

# Verify deletion
remaining_collections = client.list_collections()
print(f"\n  Remaining collections ({len(remaining_collections)}):")
for coll in remaining_collections:
    print(f"    - {coll.name}")

# ============================================================
# WARNING about DELETE
# ============================================================
print("\n" + "!"*60)
print("⚠️  WARNING: Deleting a collection is PERMANENT!")
print("!"*60)
print("  - All documents in the collection are deleted")
print("  - This action CANNOT be undone")
print("  - Always backup important data before deleting")

# ============================================================
# SUMMARY
# ============================================================
print("\n" + "="*60)
print("STEP 5 COMPLETE!")
print("="*60)
print("\nYou've learned how to manage collections:")
print("  ✓ CREATE collections with get_or_create_collection()")
print("  ✓ READ/LIST collections with list_collections()")
print("  ✓ UPDATE collection name/metadata with modify()")
print("  ✓ DELETE collections with delete_collection()")
print("\n" + "="*60)

