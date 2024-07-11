import requests

client_id = 'h3qYZseIT7S8WqvbkXHoGQ'
client_secret = '9Vc1GSq51J7yOye3luoX1X4ULWEey9hz'
# authorization_code = 'https://zoom.us/oauth/authorize?response_type=code&client_id=YOUR_CLIENT_ID&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Fcallback'  # Replace with the actual authorization code
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

response = requests.post(token_url, headers=headers, json=data, auth=(client_id, client_secret))
token_data = response.json()
if 'access_token' in token_data:
    access_token = token_data['access_token']
    print(f"Access Token: {access_token}")
else:
    print(f"Failed to obtain access token: {token_data}")


# authorization_code = '-lAYqt-7Qe-CyYiL-TnXUA'
# client_id = 'h3qYZseIT7S8WqvbkXHoGQ'
# client_secret = '9Vc1GSq51J7yOye3luoX1X4ULWEey9hz'
# redirect_uri = 'http://localhost:8000/callback'
