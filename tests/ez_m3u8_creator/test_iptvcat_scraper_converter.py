
import pytest

from ez_m3u8_creator import iptvcat_scraper_converter


def test_parse_json_file():
    file_path = R"tests\ez_m3u8_creator\TestFiles\test_file_integration.json"
    iptvcat_file = iptvcat_scraper_converter.IptvCatFile(file_path)

    assert iptvcat_file.path == file_path

    expected_ids = ['1', '2', '3', '4', '5']
    assert len(iptvcat_file) == len(expected_ids)

    imported_ids = [d['id'] for d in iptvcat_file]
    assert sorted(imported_ids) == sorted(expected_ids)

FILTER_IDS = [
    (['INVALID_STATUS'], 0, []),
    (['INVALID_STATUS'], 100, []),
    (['online'], 100, ['2', '5']),
    (['online'], 99, ['2', '3', '5']),
    (['online'], 0, ['1', '2', '3', '5']),
    (['offline'], 0, ['4']),
]
@pytest.mark.parametrize('status_list, liveliness, expected_ids', FILTER_IDS)
def test_filter_channel_list(status_list, liveliness, expected_ids):
    # Test with online, 100
    file_path = R"tests\ez_m3u8_creator\TestFiles\test_file_integration.json"
    iptvcat_file = iptvcat_scraper_converter.IptvCatFile(file_path)

    iptvcat_file.filter_channels(status_list=status_list, liveliness_min=liveliness)
    ids = [d['id'] for d in iptvcat_file]
    assert sorted(ids) == sorted(expected_ids)

'''
def test_sort_filter_list():
    assert False

def test_convert_json_to_m3u8():
    assert False

def test_convert_dir_to_m3u8():
    assert False
'''
























