import requests 
import json 

def fetch_api_data():
    api_url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(api_url)

    users = response.json()

    processed_data = []
    for user in users[:5]:
        processed_data.append({
            "id": user["id"],
            "name": user["name"],
            "email": user["email"],
            "address": user["address"]["city"],
            "company": user["company"]["name"],
        })

    print("Processed API Data: ")
    for item in processed_data:
        print(f"UserID: {item["id"]} | Username: {item["name"]} | Useremail: {item["email"]} | Address: {item["address"]} | Company: {item["company"]}")

    with open("output.json", "w") as f:
        json.dump(processed_data, f, indent=4)
    
    print("Data saved to output.json")

fetch_api_data()