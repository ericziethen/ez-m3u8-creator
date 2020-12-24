"""Code to handle m3u8 file type."""

M3U8_OPENING_TAG = '#EXTM3U'
M3U8_CHANNEL_INFO_PREFIX = '#EXTINF:'


class M3U8File():
    """An m3u8 file representation."""

    def __init__(self, file_path=None):
        """Initialize the M3U8 file."""
        self.channel_list = []

        if file_path is not None:
            self._load_file(file_path)

    def add_channel(self, *, name, url):
        """Add a channel to the file."""
        self.channel_list.append({
            'name': name,
            'url': url
        })

    def _load_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file_ptr:
            name = None
            for line in file_ptr:
                line = line.rstrip()
                if line.startswith(M3U8_OPENING_TAG):
                    pass
                elif line.startswith(M3U8_CHANNEL_INFO_PREFIX):
                    idx = line.rfind(',')
                    if idx >= 0:
                        name = line[idx + 1:]  # New str from after the last comma
                else:  # Assume it's the url
                    self.add_channel(name=name, url=line)
                    name = None

    def write_file(self, file_path):
        """Write the m3u8 file."""
        with open(file_path, 'w', encoding='utf-8') as file_ptr:
            file_ptr.write(F'{M3U8_OPENING_TAG}\n')
            for channel in self.channel_list:
                file_ptr.write(F'{M3U8_CHANNEL_INFO_PREFIX}0,{channel["name"]}\n')
                file_ptr.write(F'{channel["url"]}\n')
