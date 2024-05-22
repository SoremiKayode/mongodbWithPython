import pymongo
import myData

connection = pymongo.MongoClient("mongodb://localhost:27017")

my_database = connection["ecommerceProduct"]
product_info = my_database["product_info"]
image_info = my_database["image_info"]
sales_info = my_database["sales_info"]

# print(my_database.list_collection_names())
# print(connection.list_database_names())

# my_id = my_col.insert_many(myData.my_data2)
# print(my_id.inserted_ids)

# res = my_col.find_one()
# print(res)

# fetch all data
# all_data = my_col.find()

# for data in all_data:
#  print(data)

# res = my_col.find({"_id" : 1743, "sellerId" : "SELLER890"})
# print(res)

# print([data for data in res])
# excluding some certain columns

res = my_col.find({}, )