import argparse
import sys
import requests

# Replace with your actual Zoom access token
# ZOOM_TOKEN = input("Your zoom token: \n")
ZOOM_TOKEN = 'YOUR_ZOOM_TOKEN'
BASE_URL = 'https://api.zoom.us/v2/chat'

headers = {
    'Authorization': f'Bearer {ZOOM_TOKEN}',
    'Content-Type': 'application/json'
}

def create_channel(channel_name):
    url = f'{BASE_URL}/channels'
    data = {
        "name": channel_name,
        "type": 1  # Type 1 indicates a private channel and 2 for public one
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print(f"Channel '{channel_name}' created successfully.")
    else:
        print(f"Failed to create channel: {response.json()}")

def add_members(channel_id, members):
    url = f'{BASE_URL}/channels/{channel_id}/members'
    members_list = [{"email": member} for member in members.split(',')]
    data = {
        "members": members_list
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print(f"Members added successfully to channel ID '{channel_id}'.")
    else:
        print(f"Failed to add members: {response.json()}")

def read_messages(channel_id):
    url = f'{BASE_URL}/channels/{channel_id}/messages'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        messages = response.json().get('messages', [])
        for msg in messages:
            print(f"{msg['sender']}: {msg['message']}")
    else:
        print(f"Failed to read messages: {response.json()}")

def send_message(channel_id, message):
    url = f'{BASE_URL}/channels/{channel_id}/messages'
    data = {
        "message": message
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print(f"Message sent successfully to channel ID '{channel_id}'.")
    else:
        print(f"Failed to send message: {response.json()}")

def perform_action(args):
    if args.create_channel:
        create_channel(args.create_channel)
    elif args.add_members:
        add_members(args.channel_id, args.add_members)
    elif args.read_messages:
        read_messages(args.channel_id)
    elif args.send_message:
        send_message(args.channel_id, args.send_message)

def list_all_channels():
    url = f'{BASE_URL}/users/me/channels'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        channels = response.json().get('channels', [])
        for channel in channels:
            print(f"Channel Name: {channel['name']} - Channel ID: {channel['id']}")
    else:
        print(f"Failed to list channels: {response.json()}")

def main():
    parser = argparse.ArgumentParser(description='Zoom Chat Operations')

    parser.add_argument('-cc', '--create-channel', type=str, help='Create a new channel')
    parser.add_argument('-am', '--add-members', type=str, help='Add members to a channel (comma-separated emails)')
    parser.add_argument('-rm', '--read-messages', action='store_true', help='Read messages from a channel')
    parser.add_argument('-sm', '--send-message', type=str, help='Send a message to a channel')
    parser.add_argument('-ci', '--channel-id', type=str, help='Channel ID for the operation')
    parser.add_argument('-lc', '--list-channels', action='store_true', help='List all channels')


    if len(sys.argv) < 2:
        parser.print_help(sys.stderr)
        sys.exit(1)
    args = parser.parse_args()

    perform_action(args)

if __name__ == '__main__':
    main()
