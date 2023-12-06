import requests

# Replace 'YOUR_BOT_TOKEN' and 'YOUR_CHAT_ID' with your actual token and chat ID
bot_token = 'YOUR_BOT_TOKEN'
chat_id = 'YOUR_CHAT_ID'
message = 'Someone logged in to your PC.'

url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
params = {'chat_id': chat_id, 'text': message}

response = requests.post(url, params=params)

print(response.json())  # Print the API response (optional)