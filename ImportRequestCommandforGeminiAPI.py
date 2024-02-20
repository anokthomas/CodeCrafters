import requests
import json

# Replace these with your actual API key and secret
API_KEY = 'your_api_key'
API_SECRET = 'your_api_secret'

# Define API endpoints
BASE_URL = 'https://api.gemini.com'
ORDERS_ENDPOINT = '/v1/order/new'

# Sample order data
order_data = {
    "request": "/v1/order/new",
    "nonce": 123456,
    "symbol": "btcusd",
    "amount": "0.01",
    "price": "1000.00",
    "side": "buy",
    "type": "exchange limit"
}

# Generate signature
payload = json.dumps(order_data)
signature = hmac.new(API_SECRET.encode(), payload.encode(), hashlib.sha384).hexdigest()

# Add authentication headers
headers = {
    'Content-Type': 'text/plain',
    'Content-Length': '0',
    'X-GEMINI-APIKEY': API_KEY,
    'X-GEMINI-PAYLOAD': base64.b64encode(payload.encode()).decode(),
    'X-GEMINI-SIGNATURE': signature,
}

# Make the request
response = requests.post(BASE_URL + ORDERS_ENDPOINT, headers=headers, data=payload)

# Handle response
if response.status_code == 200:
    print("Order placed successfully:", response.json())
else:
    print("Failed to place order:", response.text)
