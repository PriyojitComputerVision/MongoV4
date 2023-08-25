from pymongo import MongoClient
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
def eval_model():
    conn="mongodb://localhost:27017"
    client=MongoClient(conn)
    # Load the saved model
    loaded_model = joblib.load("C:\\Users\\Hp\\OneDrive\\Desktop\\MLwithMongoDB\\MLwithMongoDB\\src\\src\\mongodbprojectwithml\\components\\best_model.pkl")

    # Take user input for 'main_road'
    main_road = input("Is the main road (1 for yes, 0 for no)? ")
    main_road = int(main_road)

    if main_road == 1:
        # Create a dictionary with the input features
        input_data = {
            'average_price_per_area': float(input("Enter average price per area: ")),
            'area': float(input("Enter area: ")),
            'bedrooms': int(input("Enter number of bedrooms: ")),
            'airconditioning': int(input("Is there air conditioning (1 for yes, 0 for no)? ")),
            'bathrooms': int(input("Enter number of bathrooms: ")),
            'guestroom': int(input("Is there a guest room (1 for yes, 0 for no)? ")),
            'prefarea': int(input("Is it a preferred area (1 for yes, 0 for no)? ")),
            'furnishingstatus': int(input("Enter furnishing status (2 for fully, 1 for semi, 0 for none): "))
        }

        # Convert the input dictionary to a DataFrame
        input_df = pd.DataFrame([input_data])

        # Replace this with your actual selected features obtained from feature selection
        selected_features = ["average_price_per_area", "area", "bedrooms", "airconditioning", "bathrooms", "guestroom", "prefarea", "furnishingstatus"]

        # Apply the same scaling steps as before
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(input_df[selected_features])

        # Make predictions using the loaded model
        predictions = loaded_model.predict(X_scaled)

        print("Predicted Price:", predictions[0])

        # Insert the input data into MongoDB collection
        client = MongoClient("mongodb://localhost:27017/")
        db = client["Housing_Result"]
        collection = db["HcollResult"]

        input_dict = input_data.copy()
        input_dict['Predicted'] = f'Rs. {predictions[0]}'

        # Insert the dictionary into the collection
        collection.insert_one(input_dict)

    else:
        print("Main road is not selected, so prediction is not applicable.")
    client.close()