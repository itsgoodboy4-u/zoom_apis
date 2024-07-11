from urllib.parse import urlencode
import requests

client_id = 'YOUR_CLIENT_ID'
redirect_uri = 'http://localhost:8000/callback'  # Replace with your actual redirect URI
zoom_oauth_url = 'https://zoom.us/oauth/authorize'

auth_params = {
    'response_type': 'code',
    'client_id': client_id,
    'redirect_uri': redirect_uri
}

auth_url = f"{zoom_oauth_url}?{urlencode(auth_params)}"
# print(f"Authorization URL: {auth_url}")


client_id = 'h3qYZseIT7S8WqvbkXHoGQ'
client_secret = '9Vc1GSq51J7yOye3luoX1X4ULWEey9hz'
authorization_code = 'auth_url'  # Replace with the actual authorization code from the redirect URI
redirect_uri = 'http://localhost:8000/callback'  # Replace with your actual redirect URI

token_url = 'https://zoom.us/oauth/token'
headers = {
    'Content-Type': 'application/json'
}
data = {
    'grant_type': 'authorization_code',
    'code': authorization_code,
    'redirect_uri': redirect_uri
}

response = requests.post(token_url, headers=headers, data=data, auth=(client_id, client_secret))
token_data = response.json()
if 'access_token' in token_data:
    access_token = token_data['access_token']
    print(f"Access Token: {access_token}")
else:
    print(f"Failed to obtain access token: {token_data}")
