"""Handle data import and convertion for the iptvcat_scraper files."""

import json

from ez_m3u8_creator import m3u8


class IptvCatFile():
    """A single IptvCat scraper file."""

    def __init__(self, file_path):
        self.path = file_path
        self.data = []

        self._parse_file()

    def filter_channels(self, *, status_list, liveliness_min):
        """Filter the channels by the given attributes."""

        new_data = []
        for entry in self.data:
            if entry['status'] not in status_list:
                continue

            if int(entry['liveliness']) < liveliness_min:
                continue

            new_data.append(entry)

        self.data = new_data

    def write_playlist(self, *, out_path):
        m3u8_file = m3u8.M3U8File()

        for channel in self:
            m3u8_file.add_channel(name=channel['channel'], url=channel['link'])

        m3u8_file.write_file(out_path)

    def _parse_file(self):
        """Parse the file."""
        with open(self.path, 'r', encoding='utf-8') as file_ptr:
            self.data = json.load(file_ptr)

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)
