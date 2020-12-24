"""Code to handle m3u8 file type."""

import re

M3U8_OPENING_TAG = '#EXTM3U'
M3U8_CHANNEL_INFO_PREFIX = '#EXTINF:'


class M3U8File():
    """An m3u8 file representation."""

    def __init__(self, file_path=None):
        """Initialize the M3U8 file."""
        self.channel_list = []

        if file_path is not None:
            self._load_file(file_path)

    def add_channel(self, *, name, url, group=''):
        """Add a channel to the file."""
        self.channel_list.append({
            'name': name,
            'url': url,
            'group': group,
        })

    def add_groups_from_category_dic(self, category_dic, *, overwrite=True):
        """Calculate the groups based on the given json file."""
        for channel in self.channel_list:
            categories = get_categories_from_json(channel_name=channel['name'], json_data=category_dic)
            if categories and overwrite:
                channel['group'] = ';'.join(categories)

    def _load_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file_ptr:
            details = {}
            for line in file_ptr:
                line = line.rstrip()
                if line.startswith(M3U8_OPENING_TAG):
                    pass
                elif line.startswith(M3U8_CHANNEL_INFO_PREFIX):
                    # Get the Channel Name
                    # Assume for now we MUST always have a ',' so not adding any checking for now
                    details['name'] = line[line.rfind(',') + 1:]  # New str from after the last comma

                    # Get the channel Group
                    details['group'] = ''
                    group_pattern = 'group-title="(?P<group>.*?)"'
                    result = re.search(group_pattern, line)
                    details['group'] = result.group('group') if bool(result) else ''
                else:  # Assume it's the url
                    self.add_channel(name=details['name'], url=line, group=details['group'])
                    details = {}

    def write_file(self, file_path):
        """Write the m3u8 file."""
        with open(file_path, 'w', encoding='utf-8') as file_ptr:
            file_ptr.write(F'{M3U8_OPENING_TAG}\n')
            for channel in self.channel_list:
                file_ptr.write(F'''{M3U8_CHANNEL_INFO_PREFIX}0 group-title="{channel['group']}",{channel["name"]}\n''')
                file_ptr.write(F'{channel["url"]}\n')


def get_categories_from_json(*, channel_name, json_data):
    """Get the categories for a channel name."""

    categories = []

    for category, criterias in json_data.items():
        for criteria in criterias:
            if criteria == 'contains':
                for keyword in criterias[criteria]:
                    if keyword.lower() in channel_name.lower():
                        categories.append(category)
                        break

    return categories
