
def test_main():
    """ Test main function """
    assert 1
def test_adb():
    import subprocess

    subprocess.run(
        'adb shell am broadcast -a ADB_INPUT_TEXT --es msg "我老"',
        shell=True,
        check=False,
    )
