"""Script to convert m3u4u channel files to a fake m3u playlist."""

import argparse
import json
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from ez_m3u8_creator import m3u8


def main():
    """Run the main function."""
    parser = argparse.ArgumentParser()
    parser.add_argument('-if', '--input_file', help='The m3u playlist to process.', required=True)
    parser.add_argument('-of', '--out_file', help='The m3u playlist to write to', required=True)
    parser.add_argument('-jf', '--json_file', help='The json file with the channel info.', required=True)
    args = parser.parse_args()

    if (not os.path.exists(args.input_file)) or not os.path.isfile(args.input_file):
        raise ValueError(F'"{args.input_file}" is not a vaid file')
    if (not os.path.exists(args.json_file)) or not os.path.isfile(args.json_file):
        raise ValueError(F'"{args.json_file}" is not a vaid file')

    m3u8_file = m3u8.M3U8File(args.input_file)

    json_data = {}
    raw_json_data = None
    with open(args.json_file, 'r') as file_ptr:
        raw_json_data = json.load(file_ptr)

    # Clean up json data
    for info in raw_json_data:
        json_data[m3u8.remove_meta_data_from_channel_name(info['name']).upper()] = info['tvgid']

    # Find matching channels
    count = 0
    for _, channel_list in m3u8_file.channel_url_dict.items():
        for channel in channel_list:
            channel_name = m3u8.remove_meta_data_from_channel_name(channel['name'])

            if 'DAZN' in channel['name'].upper():
                print(F'''"{channel['name']}" -> "{channel_name}"''')

            channel_key = channel_name.upper()
            if channel_key in json_data:
                channel['id'] = json_data[channel_key]
                count += 1

            # for info in json_data:
            #     json_name = m3u8.remove_meta_data_from_channel_name(info['name'])
            #     if json_name.upper() == channel_name.upper():
            #         channel['id'] = info['tvgid']
            #         count += 1
            #         break

    print('FOUND:', count)

    m3u8_file.write_file(args.out_file)


if __name__ == '__main__':
    main()
