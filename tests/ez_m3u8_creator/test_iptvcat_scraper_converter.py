
from ez_m3u8_creator import iptvcat_scraper_converter


def test_parse_json_file():
    file_path = R"tests\ez_m3u8_creator\TestFiles\test_file_integration.json"
    iptvcat_file = iptvcat_scraper_converter.IptvCatFile(file_path)

    assert iptvcat_file.path == file_path

    expected_ids = ['1', '2', '3', '4', '5']
    assert len(iptvcat_file) == len(expected_ids)

    imported_ids = [d['id'] for d in iptvcat_file]
    assert sorted(imported_ids) == sorted(expected_ids)

'''
def test_filter_channel_list():
    assert False

def test_sort_filter_list():
    assert False

def test_convert_json_to_m3u8():
    assert False

def test_convert_dir_to_m3u8():
    assert False
'''
























