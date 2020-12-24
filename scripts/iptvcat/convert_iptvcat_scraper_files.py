"""Script to convert iptvcat json files to m3u8."""

import argparse
import os
import sys

sys.path.append(R'D:\# Eric Projects\ez-m3u8-creator')

from ez_m3u8_creator import m3u8

def main():
    """Run the main function."""
    parser = argparse.ArgumentParser()
    parser.add_argument('m3u8_in_dir', help='The directory to read the m3u8 files.')
    args = parser.parse_args()
    parser.add_argument('m3u8_out_dir', help='The directory to store the m3u8 files.')
    args = parser.parse_args()

    if (not os.path.exists(args.m3u8_in_dir)) or (not os.path.isdir(args.m3u8_in_dir)):
        raise ValueError(F'"{args.m3u8_in_dir}" is not a vaid directory')
    if (not os.path.exists(args.m3u8_out_dir)) or (not os.path.isdir(args.m3u8_out_dir)):
        raise ValueError(F'"{args.m3u8_out_dir}" is not a vaid directory')

    for root, _, files in os.walk(args.m3u8_in_dir):
        for filename in files:
            if not filename.lower().endswith('.m3u8') or not filename.lower().endswith('.m3u'):
                continue

            m3u8_file = m3u8.M3U8File(os.path.join(args.m3u8_in_dir, filename))


    iptvcat_scraper_converter.convert_json_dir_to_m3u8(
        in_dir=args.json_dir, out_dir=args.m3u8_dir
    )


if __name__ == '__main__':
    main()
