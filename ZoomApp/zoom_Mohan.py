import argparse
import sys
from JsonUtilities import *

CONFIG_FILE = './config/prod/subscriptionConfig.json'

def isBlank(input):
    if input is None or input=='':
        return True
    return False

def list_all_channels():
    config_data = get_json(CONFIG_FILE)
    for config_block in config_data:
        if 'STRATEGIES' in config_block.keys():
            print(config_block['NAME'])

def list_strategies(channel):
    if isBlank(channel):
        print('Please enter the channel name')
    else:
        config_data = get_json(CONFIG_FILE)
        selected_block = next((config_block for config_block in config_data if config_block.get('NAME') == channel), None)
        if selected_block is None:
            print('Please enter a valid channel name')
        else:
            strategies = selected_block['STRATEGIES']
            for strategy in strategies:
                strategy_entry = strategy.split(':')
                print(strategy_entry[0],'\t',strategy_entry[1])

def add_to_channel(channel, strategies):
    if isBlank(channel) or isBlank(strategies):
        print('Please enter all the required fields (channel, strategy and server)')
    else:
        config_data = get_json(CONFIG_FILE)
        selected_block = next((config_block for config_block in config_data if config_block.get('NAME') == channel), None)
        if selected_block is None:
            print('Please enter a valid channel name')
        else:
            if 'STRATEGIES' not in selected_block.keys():
                selected_block['STRATEGIES'] = []
            for strategy in strategies.split(','):
                if strategy not in selected_block['STRATEGIES']:
                    selected_block['STRATEGIES'].append(strategy)
            write_json(config_data, CONFIG_FILE)
            print(f'Successfully updated strategies for channel: {channel}')

def remove_from_channel(channel, strategies):
    if isBlank(channel) or isBlank(strategies):
        print('Please enter all the required fields (channel, strategy and server)')
    else:
        config_data = get_json(CONFIG_FILE)
        selected_block = next((config_block for config_block in config_data if config_block.get('NAME') == channel), None)
        if selected_block is None:
            print('Please enter a valid channel name')
        else:
            if 'STRATEGIES' not in selected_block.keys():
                return
            for strategy in strategies.split(','):
                if strategy in selected_block['STRATEGIES']:
                    selected_block['STRATEGIES'].remove(strategy)
            write_json(config_data, CONFIG_FILE)
            print(f'Successfully updated strategies for channel: {channel}')

def perform_action(args):
    if args.list_channels:
        list_all_channels()
    elif args.list_strategies:
        list_strategies(args.list_strategies)
    elif args.add:
        add_to_channel(args.c,args.strategies)
    elif args.remove:
        remove_from_channel(args.c,args.strategies)

def main():
    parser = argparse.ArgumentParser(description='Modify the strategies subscribed to zoom alerts\n')

    parser.add_argument('-l','--list-channels', action='store_true', help='List all channels')
    parser.add_argument('-ls','--list-strategies', type=str, help='List all strategies linked to channel')
    parser.add_argument('-a','--add', action='store_true', help='Add a strategy to a channel')
    parser.add_argument('-r','--remove','--rm', action='store_true', help='Remove a strategy from a channel')
    # parser.add_argument('-s','--server', type=str, help='Server the strategy is running on')
    parser.add_argument('-s','-strat','--strategies', type=str, help='Strategy name (Case sensitive) and csv for multiple strategies')
    parser.add_argument('-c','-ch','-channel', type=str, help='Channel name (Case sensitive)')

    if len(sys.argv) < 2:
        parser.print_help(sys.stderr)
        sys.exit(1)
    args = parser.parse_args()

    perform_action(args)

if __name__ == '__main__':
    main()
