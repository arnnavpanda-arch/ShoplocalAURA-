from pymongo import MongoClient

uri = "mongodb+srv://arnnav:cutiki@cluster0.t83s0ym.mongodb.net/?appName=Cluster0"
client = MongoClient(uri, serverSelectionTimeoutMS=5000)
db = client['mall_shopping_system']

def deduplicate(collection, key):
    print(f"Deduplicating {collection.name} by {key}...")
    pipeline = [
        {"$group": {
            "_id": f"${key}",
            "dups": {"$push": "$_id"},
            "count": {"$sum": 1}
        }},
        {"$match": {
            "count": {"$gt": 1}
        }}
    ]
    
    duplicates = list(collection.aggregate(pipeline))
    total_removed = 0
    for doc in duplicates:
        # Keep the first one, delete the rest
        dups_to_remove = doc['dups'][1:]
        res = collection.delete_many({"_id": {"$in": dups_to_remove}})
        total_removed += res.deleted_count
        
    print(f"Removed {total_removed} duplicates from {collection.name}")

deduplicate(db.shops, "id")
deduplicate(db.deliveries, "id")
deduplicate(db.offers, "id")
deduplicate(db.customers, "phone")

print("Deduplication complete.")
