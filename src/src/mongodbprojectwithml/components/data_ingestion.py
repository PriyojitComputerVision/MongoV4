import pymongo, pandas as pd
from pymongo import MongoClient

conn="mongodb://localhost:27017"
client=MongoClient(conn)

df=pd.read_csv('C:\\Users\\Hp\\OneDrive\\Desktop\\MLwithMongoDB\\MLwithMongoDB\\Housing.csv') #Give your path
db=client["Housing1"]
collection=db["Hcollection1"]
collectlist=df.to_dict('records')
collection.insert_many(collectlist)
# Aggregation pipeline where main road is present and engineered the values of yes to 1 and no to 0
#Also added an additional parameter of average price per area unit
pipeline = [
    {"$match": {"mainroad": {"$in": ["yes", "no"]}}},  # Filter valid values
    {"$project": {
        "price": 1,
        "area": 1,
        "bedrooms": 1,
        "bathrooms": 1,
        "guestroom":{
            "$cond":[
                {"$eq":["$guestroom","yes"]},
                1,
                0]
        },
        "basement":{
            "$cond":[
                {"$eq":["$basement","yes"]},
                1,
                0]
        },
        "hotwatering":{
            "$cond":[
                {"$eq":["$hotwatering","yes"]},
                1,
                0]
        },
        "airconditioning":{
            "$cond":[
                {"$eq":["$airconditioning","yes"]},
                1,
                0]
        },
        "prefarea":{
            "$cond":[
                {"$eq":["$prefarea","yes"]},
                1,
                0]
        },
        "furnishingstatus": {
            "$cond": [
                {"$eq": ["$furnishingstatus", "fully-furnished"]},
                2,
                {
                    "$cond": [
                        {"$eq": ["$furnishingstatus", "semi-furnished"]},
                        1,
                        0
                    ]
                }
            ]
        },

        "mainroad": {
            "$cond": [
                {"$eq": ["$mainroad", "yes"]},
                1,
                0
            ]
        }
    }},
    {"$group": {
        "_id": {"price": "$price", "stories":"$stories","area": "$area", "bedrooms": "$bedrooms", "bathrooms": "$bathrooms","guestroom":"$guestroom",'basement':'$basement','hotwaterheating':'$hotwaterheating','airconditioning':'$airconditioning', 'parking':'$parking','prefarea':'$prefarea','furnishingstatus':'$furnishingstatus'},
        "average_price_per_area": {"$avg": {"$divide": ["$price", "$area"]}},
    }},
    {"$sort": {"average_price_per_area": 1}},
    {"$project": {
        "_id": 0,  # Exclude the _id field from the output
        "price": "$_id.price",
        "area": "$_id.area",
        "bedrooms": "$_id.bedrooms",
        'hotwaterheating':'$_id.hotwaterheating',
        'airconditioning':'$_id.airconditioning',
        "bathrooms": "$_id.bathrooms",
        "guestroom":"$_id.guestroom",
        'prefarea':'$_id.prefarea',
        "stories":"$_id.stories",
        "mainroad": 1,
        "furnishingstatus": "$_id.furnishingstatus",
        "average_price_per_area": 1
    }}
]
result = list(collection.aggregate(pipeline))

# Convert the result to a DataFrame
result_df = pd.DataFrame(result)

# Print the DataFrame
print(result_df)
result_df.to_csv('filtered_data.csv')
client.close()