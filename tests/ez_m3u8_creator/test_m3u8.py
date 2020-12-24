
from ez_m3u8_creator import m3u8

TEST_FILE_INTEGRATION_CONVERTED_PATH = R'tests/ez_m3u8_creator/TestFiles/test_file_integration_converted.m3u8'


def test_write_m3u8_file(tmpdir):
    m3u8_file = m3u8.M3U8File()

    m3u8_file.add_channel(name='Channel 1', url='channel_url')
    m3u8_file.add_channel(name='Channel 2', url='channel_url2')

    out_file = tmpdir.join('test.m3u8')
    m3u8_file.write_file(out_file)

    with open(out_file, 'r') as file_ptr:
        line_list = list(file_ptr)
        assert line_list[0].rstrip() == '#EXTM3U'
        assert line_list[1].rstrip() == '#EXTINF:0,Channel 1'
        assert line_list[2].rstrip() == 'channel_url'
        assert line_list[3].rstrip() == '#EXTINF:0,Channel 2'
        assert line_list[4].rstrip() == 'channel_url2'


def test_load_m3u8_file(tmpdir):
    m3u8_file = m3u8.M3U8File(TEST_FILE_INTEGRATION_CONVERTED_PATH)
    out_file = tmpdir.join('output.m3u8')
    m3u8_file.write_file(out_file)

    with open(TEST_FILE_INTEGRATION_CONVERTED_PATH, 'r', encoding='utf-8') as file_ptr:
        in_file_line_list = list(file_ptr)
        out_file_line_list = out_file.read_text(encoding='utf-8').split('\n')

        print(out_file_line_list)

        assert len(in_file_line_list) == 5

        # Rough test that all the lines are matching
        for idx, line in enumerate(in_file_line_list):
            assert line.rstrip() == out_file_line_list[idx]


def test_get_categories_from_json():
    assert False


def test_add_categories_from_json_to_m3u():
    assert False

