import subprocess
from typing import ClassVar, NamedTuple

from attrs import define
from loguru import logger


class SomeCommand(NamedTuple):
    """
    Attributes:
        sent_text: 发送文本的命令
    """

    sent_text: str = 'am broadcast -a ADB_INPUT_TEXT --es msg'
    click: str = 'input tap'


@define
class MyAdb:
    """
    Attributes:
        sub:adb shell的起手
    """

    sub: ClassVar[str] = 'adb shell'
    const: ClassVar[SomeCommand] = SomeCommand()

    def use_bash_send_text(self, text: str) -> int:
        text1 = ' '.join([self.sub, self.const.sent_text, f'"{text}"'])
        res = subprocess.run(text1, shell=True, check=False)
        logger.info(f'{text1}')
        return res.returncode


@define
class Clicks:
    number: int
    point: tuple[int, int]


@define
class Swipe:
    name: str
    click: tuple[Clicks, ...]


@define
class SendText:
    text: str
    adb: ClassVar[MyAdb] = MyAdb()

    def open_dialog_box(self):
        pass

    def sent_text(self):
        s1 = self.adb.use_bash_send_text(self.text)
        return s1
