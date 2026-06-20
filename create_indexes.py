from pymongo import MongoClient, ASCENDING

uri = "mongodb+srv://arnnav:cutiki@cluster0.t83s0ym.mongodb.net/?appName=Cluster0"
client = MongoClient(uri, serverSelectionTimeoutMS=5000)
db = client['mall_shopping_system']

# Create unique indexes
db.shops.create_index([("id", ASCENDING)], unique=True)
db.deliveries.create_index([("id", ASCENDING)], unique=True)
db.offers.create_index([("id", ASCENDING)], unique=True)
db.customers.create_index([("phone", ASCENDING)], unique=True)

print("Unique indexes created successfully!")
