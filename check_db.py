from pymongo import MongoClient

uri = "mongodb+srv://arnnav:cutiki@cluster0.t83s0ym.mongodb.net/?appName=Cluster0"
client = MongoClient(uri, serverSelectionTimeoutMS=5000)
db = client['mall_shopping_system']

print("Shops count:", db.shops.count_documents({}))
print("Deliveries count:", db.deliveries.count_documents({}))
print("Offers count:", db.offers.count_documents({}))
print("Customers count:", db.customers.count_documents({}))

for shop in db.shops.find():
    print("Shop", shop.get("id"), "products count:", len(shop.get("products", [])))
