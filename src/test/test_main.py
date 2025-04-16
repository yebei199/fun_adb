from src.adb.send_text import MyAdb


def test_main():
    """Test main function"""
    assert 1


def test_adb():
    MyAdb().use_bash_send_text('hello')
