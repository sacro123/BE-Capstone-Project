import requests

url = "http://localhost:8000/api/products/"  # Note the change here
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI5NDM1MzMyLCJpYXQiOjE3Mjg4MzA1MzIsImp0aSI6Ijg5YmM4NDExMjQ0MTRhNWM4ZGU5NzcyYTU4ZWJmMTk5IiwidXNlcl9pZCI6NH0.HjHSsSBsjntSgPIBMJ5W1LsVCkTi2XhZK3WmKvHkFLg"
}
data = {
    "name": "Test Product",
    "description": "A test product",
    "price": 19.99,
    "category": "Test",
    "stock_quantity": 10
}

response = requests.post(url, json=data, headers=headers)
print(response.status_code)
print("Response content:", response.content)
try:
    print(response.json())
except requests.exceptions.JSONDecodeError:
    print("Could not decode JSON response")