import pymongo
import myData

connection = pymongo.MongoClient("mongodb://localhost:27017")

my_database = connection["myEcommerceDatabase"]

product_info = my_database["product_info"]
product_images = my_database["product_images"]
sales_info = my_database["sales_info"]

# inserting data into the database
# pd_info = product_info.insert_many(myData.my_data2)
# pd_images = product_images.insert_many(myData.productImages)
# sl_info = sales_info.insert_many(myData.sales_details)

# print(f"product info : {pd_info.inserted_ids}")
# print(f"product images : {pd_images.inserted_ids}")
# print(f"Sales info info : {sl_info.inserted_ids}")

# using the limit
# res = product_info.find().limit(10)

# s = [data for data in res]
# print(len(s))

# sorting data

# sorting in ascending order
# res = product_info.find({}).sort("price")

# sorting in descending order
# res = product_info.find({}).sort("price", -1).skip(5)

# for data in res :
#     print(data)
    
# Aggregration
""" 
- first specify use a list
- then a dictionary with a key of $group
- create a key name to hold the the column details you
want to use to aggregriate in our case the key is "_id" the column
name in the table is "sellerId", remember to append it with a 
dolar sign like "$sellerId"
- if you want to use accumulators it has to be a dictionary 
with the accumulator as the key and column name in the database as the
value, eg. "totalProductPrice" : {"$sum" : "$price"},
- Following are list of accumulators you can use

$sum: Calculates the sum of numeric values.
$avg: Calculates the average of numeric values.
$min: Finds the minimum value.
$max: Finds the maximum value.
$first: Returns the first value in the group.
$last: Returns the last value in the group.
$push: Appends a value to an array of values.
$addToSet: Adds a value to an array of values if it doesn’t already exist in the array (unique values).

"""
# res = product_info.aggregate([
# {
# "$group" : {
# "_id" : "$sellerId",
# "sumTotalOfAllProduct" : {"$sum" : "$price"},
# "averagePrice" : {"$avg" : "$price"},
# "count" : {"$sum" : 1}
# }
# }
# ])

# for data in res :
#     print(data)

# using the $unwind
# res = sales_info.aggregate([
# {
# "$unwind" : {
# "path" : "$additionalImages",
# "preserveNullAndEmptyArrays" : True
# }
# }
# ])

# for data in res :
#     print(data)

# $lookup
""" 
We use the lookup to perform a left outer join
"""

# res = sales_info.aggregate([{
# "$lookup" : {
# "from" : "product_info",
# "localField" : "product_id",
# "foreignField" : "_id",
# "as" : "leftOuterJoinedData"
# }
# }])

# for data in res :
#     print(data)

# addFields

# res = product_info.aggregate([
# {
# "$addFields" :{
# "taxRate" : {"$multiply" : ["$price", 0.2]}
# }
    
# }
# ])

# for data in res :
#     print(data)

# using the $out
# res = product_info.aggregate([
# {
# "$group" : {
# "_id" : "$sellerId",
# "sumTotalOfAllProduct" : {"$sum" : "$price"},
# "averagePrice" : {"$avg" : "$price"},
# "count" : {"$sum" : 1}
# }
# }, 

# {
# "$out" : "aggregratedData"
# }
# ])

# update single data
# old = {"sellerId" :"SELLER112"}
# new = {"$set" : {"productTitle" : "External Solid State Drive, 400GB"}}

# product_info.update_one(old, new)

# #updating multiple data
# old = {"sellerId" : "SELLER112"}
# new = {"$mul" : {"price" : 1.10}}

# product_info.update_many(old, new)

# deleting a single data
# data_to_delete = {"price":2643}
# product_info.delete_one(data_to_delete)

# deleting a single data
# data_to_delete = {"price": {"$gte" : 400}}
# product_info.delete_many(data_to_delete)

product_info.drop()

