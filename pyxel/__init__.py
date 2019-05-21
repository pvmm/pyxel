import inspect
import os
import sys
from ctypes import CFUNCTYPE, c_char_p, c_int32, cast, create_string_buffer
from typing import Any, Callable, List, Optional

import numpy as np  # type: ignore

from . import core  # type: ignore


#
# constants
#
def get_constant_number(name: str) -> int:
    return core.get_constant_number(name.encode("utf-8"))  # type: ignore


def get_constant_string(name: str) -> str:
    return core.get_constant_string(name.encode("utf-8")).decode()  # type: ignore


VERSION: str = get_constant_string("VERSION")

DEFAULT_CAPTION: str = get_constant_string("DEFAULT_CAPTION")
DEFAULT_SCALE: int = get_constant_number("DEFAULT_SCALE")
DEFAULT_PALETTE: List[int] = [
    get_constant_number("DEFAULT_PALETTE_00"),
    get_constant_number("DEFAULT_PALETTE_01"),
    get_constant_number("DEFAULT_PALETTE_02"),
    get_constant_number("DEFAULT_PALETTE_03"),
    get_constant_number("DEFAULT_PALETTE_04"),
    get_constant_number("DEFAULT_PALETTE_05"),
    get_constant_number("DEFAULT_PALETTE_06"),
    get_constant_number("DEFAULT_PALETTE_07"),
    get_constant_number("DEFAULT_PALETTE_08"),
    get_constant_number("DEFAULT_PALETTE_09"),
    get_constant_number("DEFAULT_PALETTE_10"),
    get_constant_number("DEFAULT_PALETTE_11"),
    get_constant_number("DEFAULT_PALETTE_12"),
    get_constant_number("DEFAULT_PALETTE_13"),
    get_constant_number("DEFAULT_PALETTE_14"),
    get_constant_number("DEFAULT_PALETTE_15"),
]
DEFAULT_FPS: int = get_constant_number("DEFAULT_FPS")
DEFAULT_BORDER_WIDTH: int = get_constant_number("DEFAULT_BORDER_WIDTH")
DEFAULT_BORDER_COLOR: int = get_constant_number("DEFAULT_BORDER_COLOR")

IMAGE_BANK_COUNT: int = get_constant_number("IMAGE_BANK_COUNT")
TILEMAP_BANK_COUNT: int = get_constant_number("TILEMAP_BANK_COUNT")
SOUND_BANK_COUNT: int = get_constant_number("SOUND_BANK_COUNT")
MUSIC_BANK_COUNT: int = get_constant_number("MUSIC_BANK_COUNT")
MUSIC_CHANNEL_COUNT: int = get_constant_number("MUSIC_CHANNEL_COUNT")

FONT_WIDTH: int = get_constant_number("FONT_WIDTH")
FONT_HEIGHT: int = get_constant_number("FONT_HEIGHT")

KEY_SPACE: int = get_constant_number("KEY_SPACE")
KEY_APOSTROPHE: int = get_constant_number("KEY_APOSTROPHE")
KEY_COMMA: int = get_constant_number("KEY_COMMA")
KEY_MINUS: int = get_constant_number("KEY_MINUS")
KEY_PERIOD: int = get_constant_number("KEY_PERIOD")
KEY_SLASH: int = get_constant_number("KEY_SLASH")
KEY_0: int = get_constant_number("KEY_0")
KEY_1: int = get_constant_number("KEY_1")
KEY_2: int = get_constant_number("KEY_2")
KEY_3: int = get_constant_number("KEY_3")
KEY_4: int = get_constant_number("KEY_4")
KEY_5: int = get_constant_number("KEY_5")
KEY_6: int = get_constant_number("KEY_6")
KEY_7: int = get_constant_number("KEY_7")
KEY_8: int = get_constant_number("KEY_8")
KEY_9: int = get_constant_number("KEY_9")
KEY_SEMICOLON: int = get_constant_number("KEY_SEMICOLON")
KEY_EQUAL: int = get_constant_number("KEY_EQUAL")
KEY_A: int = get_constant_number("KEY_A")
KEY_B: int = get_constant_number("KEY_B")
KEY_C: int = get_constant_number("KEY_C")
KEY_D: int = get_constant_number("KEY_D")
KEY_E: int = get_constant_number("KEY_E")
KEY_F: int = get_constant_number("KEY_F")
KEY_G: int = get_constant_number("KEY_G")
KEY_H: int = get_constant_number("KEY_H")
KEY_I: int = get_constant_number("KEY_I")
KEY_J: int = get_constant_number("KEY_J")
KEY_K: int = get_constant_number("KEY_K")
KEY_L: int = get_constant_number("KEY_L")
KEY_M: int = get_constant_number("KEY_M")
KEY_N: int = get_constant_number("KEY_N")
KEY_O: int = get_constant_number("KEY_O")
KEY_P: int = get_constant_number("KEY_P")
KEY_Q: int = get_constant_number("KEY_Q")
KEY_R: int = get_constant_number("KEY_R")
KEY_S: int = get_constant_number("KEY_S")
KEY_T: int = get_constant_number("KEY_T")
KEY_U: int = get_constant_number("KEY_U")
KEY_V: int = get_constant_number("KEY_V")
KEY_W: int = get_constant_number("KEY_W")
KEY_X: int = get_constant_number("KEY_X")
KEY_Y: int = get_constant_number("KEY_Y")
KEY_Z: int = get_constant_number("KEY_Z")
KEY_LEFT_BRACKET: int = get_constant_number("KEY_LEFT_BRACKET")
KEY_BACKSLASH: int = get_constant_number("KEY_BACKSLASH")
KEY_RIGHT_BRACKET: int = get_constant_number("KEY_RIGHT_BRACKET")
KEY_GRAVE_ACCENT: int = get_constant_number("KEY_GRAVE_ACCENT")
KEY_ESCAPE: int = get_constant_number("KEY_ESCAPE")
KEY_ENTER: int = get_constant_number("KEY_ENTER")
KEY_TAB: int = get_constant_number("KEY_TAB")
KEY_BACKSPACE: int = get_constant_number("KEY_BACKSPACE")
KEY_INSERT: int = get_constant_number("KEY_INSERT")
KEY_DELETE: int = get_constant_number("KEY_DELETE")
KEY_RIGHT: int = get_constant_number("KEY_RIGHT")
KEY_LEFT: int = get_constant_number("KEY_LEFT")
KEY_DOWN: int = get_constant_number("KEY_DOWN")
KEY_UP: int = get_constant_number("KEY_UP")
KEY_PAGE_UP: int = get_constant_number("KEY_PAGE_UP")
KEY_PAGE_DOWN: int = get_constant_number("KEY_PAGE_DOWN")
KEY_HOME: int = get_constant_number("KEY_HOME")
KEY_END: int = get_constant_number("KEY_END")
KEY_CAPS_LOCK: int = get_constant_number("KEY_CAPS_LOCK")
KEY_SCROLL_LOCK: int = get_constant_number("KEY_SCROLL_LOCK")
KEY_NUM_LOCK: int = get_constant_number("KEY_NUM_LOCK")
KEY_PRINT_SCREEN: int = get_constant_number("KEY_PRINT_SCREEN")
KEY_PAUSE: int = get_constant_number("KEY_PAUSE")
KEY_F1: int = get_constant_number("KEY_F1")
KEY_F2: int = get_constant_number("KEY_F2")
KEY_F3: int = get_constant_number("KEY_F3")
KEY_F4: int = get_constant_number("KEY_F4")
KEY_F5: int = get_constant_number("KEY_F5")
KEY_F6: int = get_constant_number("KEY_F6")
KEY_F7: int = get_constant_number("KEY_F7")
KEY_F8: int = get_constant_number("KEY_F8")
KEY_F9: int = get_constant_number("KEY_F9")
KEY_F10: int = get_constant_number("KEY_F10")
KEY_F11: int = get_constant_number("KEY_F11")
KEY_F12: int = get_constant_number("KEY_F12")
KEY_KP_0: int = get_constant_number("KEY_KP_0")
KEY_KP_1: int = get_constant_number("KEY_KP_1")
KEY_KP_2: int = get_constant_number("KEY_KP_2")
KEY_KP_3: int = get_constant_number("KEY_KP_3")
KEY_KP_4: int = get_constant_number("KEY_KP_4")
KEY_KP_5: int = get_constant_number("KEY_KP_5")
KEY_KP_6: int = get_constant_number("KEY_KP_6")
KEY_KP_7: int = get_constant_number("KEY_KP_7")
KEY_KP_8: int = get_constant_number("KEY_KP_8")
KEY_KP_9: int = get_constant_number("KEY_KP_9")
KEY_KP_DECIMAL: int = get_constant_number("KEY_KP_DECIMAL")
KEY_KP_DIVIDE: int = get_constant_number("KEY_KP_DIVIDE")
KEY_KP_MULTIPLY: int = get_constant_number("KEY_KP_MULTIPLY")
KEY_KP_SUBTRACT: int = get_constant_number("KEY_KP_SUBTRACT")
KEY_KP_ADD: int = get_constant_number("KEY_KP_ADD")
KEY_KP_ENTER: int = get_constant_number("KEY_KP_ENTER")
KEY_KP_EQUAL: int = get_constant_number("KEY_KP_EQUAL")
KEY_LEFT_SHIFT: int = get_constant_number("KEY_LEFT_SHIFT")
KEY_LEFT_CONTROL: int = get_constant_number("KEY_LEFT_CONTROL")
KEY_LEFT_ALT: int = get_constant_number("KEY_LEFT_ALT")
KEY_LEFT_SUPER: int = get_constant_number("KEY_LEFT_SUPER")
KEY_RIGHT_SHIFT: int = get_constant_number("KEY_RIGHT_SHIFT")
KEY_RIGHT_CONTROL: int = get_constant_number("KEY_RIGHT_CONTROL")
KEY_RIGHT_ALT: int = get_constant_number("KEY_RIGHT_ALT")
KEY_RIGHT_SUPER: int = get_constant_number("KEY_RIGHT_SUPER")
KEY_MENU: int = get_constant_number("KEY_MENU")
KEY_SHIFT: int = get_constant_number("KEY_SHIFT")
KEY_CONTROL: int = get_constant_number("KEY_CONTROL")
KEY_ALT: int = get_constant_number("KEY_ALT")
KEY_SUPER: int = get_constant_number("KEY_SUPER")
MOUSE_LEFT_BUTTON: int = get_constant_number("MOUSE_LEFT_BUTTON")
MOUSE_MIDDLE_BUTTON: int = get_constant_number("MOUSE_MIDDLE_BUTTON")
MOUSE_RIGHT_BUTTON: int = get_constant_number("MOUSE_RIGHT_BUTTON")
GAMEPAD_1_A: int = get_constant_number("GAMEPAD_1_A")
GAMEPAD_1_B: int = get_constant_number("GAMEPAD_1_B")
GAMEPAD_1_X: int = get_constant_number("GAMEPAD_1_X")
GAMEPAD_1_Y: int = get_constant_number("GAMEPAD_1_Y")
GAMEPAD_1_LEFT_SHOULDER: int = get_constant_number("GAMEPAD_1_LEFT_SHOULDER")
GAMEPAD_1_RIGHT_SHOULDER: int = get_constant_number("GAMEPAD_1_RIGHT_SHOULDER")
GAMEPAD_1_SELECT: int = get_constant_number("GAMEPAD_1_SELECT")
GAMEPAD_1_START: int = get_constant_number("GAMEPAD_1_START")
GAMEPAD_1_UP: int = get_constant_number("GAMEPAD_1_UP")
GAMEPAD_1_RIGHT: int = get_constant_number("GAMEPAD_1_RIGHT")
GAMEPAD_1_DOWN: int = get_constant_number("GAMEPAD_1_DOWN")
GAMEPAD_1_LEFT: int = get_constant_number("GAMEPAD_1_LEFT")
GAMEPAD_2_A: int = get_constant_number("GAMEPAD_2_A")
GAMEPAD_2_B: int = get_constant_number("GAMEPAD_2_B")
GAMEPAD_2_X: int = get_constant_number("GAMEPAD_2_X")
GAMEPAD_2_Y: int = get_constant_number("GAMEPAD_2_Y")
GAMEPAD_2_LEFT_SHOULDER: int = get_constant_number("GAMEPAD_2_LEFT_SHOULDER")
GAMEPAD_2_RIGHT_SHOULDER: int = get_constant_number("GAMEPAD_2_RIGHT_SHOULDER")
GAMEPAD_2_SELECT: int = get_constant_number("GAMEPAD_2_SELECT")
GAMEPAD_2_START: int = get_constant_number("GAMEPAD_2_START")
GAMEPAD_2_UP: int = get_constant_number("GAMEPAD_2_UP")
GAMEPAD_2_RIGHT: int = get_constant_number("GAMEPAD_2_RIGHT")
GAMEPAD_2_DOWN: int = get_constant_number("GAMEPAD_2_DOWN")
GAMEPAD_2_LEFT: int = get_constant_number("GAMEPAD_2_LEFT")


#
# Image class
#
class Image:
    def __init__(self, obj: Any):
        self._obj = obj

    @property
    def width(self) -> int:
        return core.image_width_getter(self._obj)  # type: ignore

    @property
    def height(self) -> int:
        return core.image_height_getter(self._obj)  # type: ignore

    @property
    def data(self) -> Any:
        return np.ctypeslib.as_array(
            core.image_data_getter(self._obj), shape=(self.height, self.width)
        )

    def get(self, x: int, y: int) -> int:
        return core.image_get(self._obj, int(x), int(y))  # type: ignore

    def set(self, x: int, y: int, val: Any) -> None:
        if type(val) is int:
            core.image_set1(self._obj, int(x), int(y), int(val))
        else:
            data_count = len(val)
            c_data = (c_char_p * data_count)()

            for i in range(data_count):
                c_str = create_string_buffer(val[i].encode("utf-8"))
                c_data[i] = cast(c_str, c_char_p)

            core.image_set(self._obj, int(x), int(y), c_data, data_count)

    def load(self, x: int, y: int, filename: str) -> bool:
        dirname = os.path.dirname(inspect.stack()[-1].filename)
        filename = os.path.join(dirname, filename)

        return core.image_load(  # type: ignore
            self._obj, int(x), int(y), filename.encode("utf-8")
        )

    def copy(self, x: int, y: int, img: int, u: int, v: int, w: int, h: int) -> None:
        core.image_copy(
            self._obj, int(x), int(y), int(img), int(u), int(v), int(w), int(h)
        )


#
# Tilemap class
#
class Tilemap:
    def __init__(self, obj: Any):
        self._obj = obj

    @property
    def width(self) -> int:
        return core.tilemap_width_getter(self._obj)  # type: ignore

    @property
    def height(self) -> int:
        return core.tilemap_height_getter(self._obj)  # type: ignore

    @property
    def data(self) -> Any:
        return np.ctypeslib.as_array(
            core.tilemap_data_getter(self._obj), shape=(self.height, self.width)
        )

    @property
    def refimg(self) -> int:
        return core.tilemap_refimg_getter(self._obj)  # type: ignore

    @refimg.setter
    def refimg(self, img: int) -> int:
        return core.tilemap_refimg_setter(self._obj, int(img))  # type: ignore

    def get(self, x: int, y: int) -> int:
        return core.tilemap_get(self._obj, int(x), int(y))  # type: ignore

    def set(self, x: int, y: int, val: Any) -> None:
        if type(val) is int:
            core.tilemap_set1(self._obj, int(x), int(y), int(val))
        else:
            data_count = len(val)
            c_data = (c_char_p * data_count)()

            for i in range(data_count):
                c_str = create_string_buffer(val[i].encode("utf-8"))
                c_data[i] = cast(c_str, c_char_p)

            core.tilemap_set(self._obj, int(x), int(y), c_data, data_count)

    def copy(self, x: int, y: int, tm: int, u: int, v: int, w: int, h: int) -> None:
        core.tilemap_copy(
            self._obj, int(x), int(y), int(tm), int(u), int(v), int(w), int(h)
        )


#
# Sound class
#
class Sound:
    def __init__(self, obj: Any):
        self._obj = obj

    @property
    def note(self) -> Any:
        return np.ctypeslib.as_array(core.sound_note_getter(self._obj), shape=(256,))

    @property
    def note_length(self) -> int:
        return core.sound_note_length_getter(self._obj)  # type: ignore

    @note_length.setter
    def note_length(self, length: int) -> None:
        core.sound_note_length_setter(self._obj, length)

    @property
    def tone(self) -> Any:
        return np.ctypeslib.as_array(core.sound_tone_getter(self._obj), shape=(256,))

    @property
    def tone_length(self) -> int:
        return core.sound_tone_length_getter(self._obj)  # type: ignore

    @tone_length.setter
    def tone_length(self, length: int) -> None:
        core.sound_tone_length_setter(self._obj, length)

    @property
    def volume(self) -> Any:
        return np.ctypeslib.as_array(core.sound_volume_getter(self._obj), shape=(256,))

    @property
    def volume_length(self) -> int:
        return core.sound_volume_length_getter(self._obj)  # type: ignore

    @volume_length.setter
    def volume_length(self, length: int) -> None:
        core.sound_volume_length_setter(self._obj, length)

    @property
    def effect(self) -> Any:
        return np.ctypeslib.as_array(core.sound_effect_getter(self._obj), shape=(256,))

    @property
    def effect_length(self) -> int:
        return core.sound_effect_length_getter(self._obj)  # type: ignore

    @effect_length.setter
    def effect_length(self, length: int) -> None:
        core.sound_effect_length_setter(self._obj, length)

    @property
    def speed(self) -> int:
        return core.sound_speed_getter(self._obj)  # type: ignore

    @speed.setter
    def speed(self, speed: int) -> None:
        core.sound_speed_setter(self._obj, speed)

    def set(self, note: str, tone: str, volume: str, effect: str, speed: int) -> None:
        core.sound_set(
            self._obj,
            note.encode("utf-8"),
            tone.encode("utf-8"),
            volume.encode("utf-8"),
            effect.encode("utf-8"),
            speed,
        )

    def set_note(self, note: str) -> None:
        core.sound_set_note(note.encode("utf-8"))

    def set_tone(self, tone: str) -> None:
        core.sound_set_tone(tone.encode("utf-8"))

    def set_volume(self, volume: str) -> None:
        core.sound_set_volume(volume.encode("utf-8"))

    def set_effect(self, effect: str) -> None:
        core.sound_set_effect(effect.encode("utf-8"))


#
# Music class
#
class Music:
    def __init__(self, obj: Any):
        self._obj = obj

    @property
    def ch0(self) -> Any:
        return np.ctypeslib.as_array(core.music_ch0_getter(self._obj), shape=(256,))

    @property
    def ch0_length(self) -> int:
        return core.music_ch0_length_getter(self._obj)  # type: ignore

    @ch0_length.setter
    def ch0_length(self, length: int) -> None:
        core.music_ch0_length_setter(self._obj, length)

    @property
    def ch1(self) -> Any:
        return np.ctypeslib.as_array(core.music_ch1_getter(self._obj), shape=(256,))

    @property
    def ch1_length(self) -> int:
        return core.music_ch1_length_getter(self._obj)  # type: ignore

    @ch1_length.setter
    def ch1_length(self, length: int) -> None:
        core.music_ch1_length_setter(self._obj, length)

    @property
    def ch2(self) -> Any:
        return np.ctypeslib.as_array(core.music_ch2_getter(self._obj), shape=(256,))

    @property
    def ch2_length(self) -> int:
        return core.music_ch2_length_getter(self._obj)  # type: ignore

    @ch2_length.setter
    def ch2_length(self, length: int) -> None:
        core.music_ch2_length_setter(self._obj, length)

    @property
    def ch3(self) -> Any:
        return np.ctypeslib.as_array(core.music_ch3_getter(self._obj), shape=(256,))

    @property
    def ch3_length(self) -> int:
        return core.music_ch3_length_getter(self._obj)  # type: ignore

    @ch3_length.setter
    def ch3_length(self, length: int) -> None:
        core.music_ch3_length_setter(self._obj, length)

    def set(self, ch0: str, ch1: str, ch2: str, ch3: str) -> None:
        core.music_set(
            ch0.encode("utf-8"),
            ch1.encode("utf-8"),
            ch2.encode("utf-8"),
            ch3.encode("utf-8"),
        )

    def set_ch0(self, ch0: str) -> None:
        core.music_set(ch0.encode("utf-8"))

    def set_ch1(self, ch1: str) -> None:
        core.music_set(ch1.encode("utf-8"))

    def set_ch2(self, ch2: str) -> None:
        core.music_set(ch2.encode("utf-8"))

    def set_ch3(self, ch3: str) -> None:
        core.music_set(ch3.encode("utf-8"))


#
# System
#
width: int = 0
height: int = 0
frame_count: int = 0


def _update_properties():  # type: ignore
    module = sys.modules[__name__]

    module.width = core.width_getter()  # type: ignore
    module.height = core.height_getter()  # type: ignore
    module.frame_count = core.frame_count_getter()  # type: ignore

    module.mouse_x = core.mouse_x_getter()  # type: ignore
    module.mouse_y = core.mouse_y_getter()  # type: ignore


def init(
    width: int,
    height: int,
    *,
    caption: str = DEFAULT_CAPTION,
    scale: int = DEFAULT_SCALE,
    palette: List[int] = DEFAULT_PALETTE,
    fps: int = DEFAULT_FPS,
    border_width: int = DEFAULT_BORDER_WIDTH,
    border_color: int = DEFAULT_BORDER_COLOR
) -> None:
    COLOR_COUNT = get_constant_number("COLOR_COUNT")

    core.init(
        int(width),
        int(height),
        caption.encode("utf-8"),
        int(scale),
        (c_int32 * COLOR_COUNT)(*palette),
        int(fps),
        int(border_width),
        int(border_color),
    )

    _update_properties()  # type: ignore


def run(update: Callable[[], None], draw: Callable[[], None]) -> None:
    def update_wrapper():  # type: ignore
        _update_properties()  # type: ignore
        update()

    core.run(CFUNCTYPE(None)(update_wrapper), CFUNCTYPE(None)(draw))


def quit() -> None:
    core.quit()


#
# Resource
#
def save(filename: str) -> bool:
    dirname = os.path.dirname(inspect.stack()[-1].filename)
    filename = os.path.join(dirname, filename)

    return core.save(filename.encode("utf-8"))  # type: ignore


def load(filename: str) -> bool:
    if load_as_old_pyxel_format(filename):
        return True

    dirname = os.path.dirname(inspect.stack()[-1].filename)
    filename = os.path.join(dirname, filename)

    return core.load(filename.encode("utf-8"))  # type: ignore


#
# Input
#
mouse_x: int = 0
mouse_y: int = 0


def btn(key: int) -> bool:
    return core.btn(int(key))  # type: ignore


def btnp(key: int, hold: int = 0, period: int = 0) -> bool:
    return core.btnp(int(key), int(hold), int(period))  # type: ignore


def btnr(key: int) -> bool:
    return core.btnr(int(key))  # type: ignore


def mouse(visible: bool) -> None:
    core.mouse(int(visible))


#
# Graphics
#
def image(img: int, *, system: bool = False) -> Image:
    return Image(core.image(int(img), int(system)))


def tilemap(tm: int) -> Tilemap:
    return Tilemap(core.tilemap(int(tm)))


def clip(
    x1: Optional[int] = None,
    y1: Optional[int] = None,
    x2: Optional[int] = None,
    y2: Optional[int] = None,
) -> None:
    if x1 is None:
        core.clip0()
    else:
        core.clip(int(x1), int(y1), int(x2), int(y2))  # type: ignore


def pal(col1: Optional[int] = None, col2: Optional[int] = None) -> None:
    if col1 is None:
        core.pal0()
    else:
        core.pal(int(col1), int(col2))  # type: ignore


def cls(col: int) -> None:
    core.cls(int(col))


def pix(x: int, y: int, col: int) -> None:
    core.pix(int(x), int(y), int(col))


def line(x1: int, y1: int, x2: int, y2: int, col: int) -> None:
    core.line(int(x1), int(y1), int(x2), int(y2), int(col))


def rect(x1: int, y1: int, x2: int, y2: int, col: int) -> None:
    core.rect(int(x1), int(y1), int(x2), int(y2), int(col))


def rectb(x1: int, y1: int, x2: int, y2: int, col: int) -> None:
    core.rectb(int(x1), int(y1), int(x2), int(y2), int(col))


def circ(x: int, y: int, r: int, col: int) -> None:
    core.circ(int(x), int(y), int(r), int(col))


def circb(x: int, y: int, r: int, col: int) -> None:
    core.circb(int(x), int(y), int(r), int(col))


def blt(
    x: int, y: int, img: int, u: int, v: int, w: int, h: int, colkey: int = -1
) -> None:
    core.blt(int(x), int(y), int(img), int(u), int(v), int(w), int(h), int(colkey))


def bltm(
    x: int, y: int, tm: int, u: int, v: int, w: int, h: int, colkey: int = -1
) -> None:
    core.bltm(int(x), int(y), int(tm), int(u), int(v), int(w), int(h), int(colkey))


def text(x: int, y: int, s: str, col: int) -> None:
    core.text(int(x), int(y), s.encode("utf-8"), int(col))


#
# Audio
#
def sound(snd: int, *, system: bool = False) -> Sound:
    return Sound(core.sound(int(snd), int(system)))


def music(msc: int) -> Music:
    return Music(core.music(int(msc)))


def play(ch: int, snd: Any, *, loop: bool = False) -> None:
    if isinstance(snd, list):
        snd_count = len(snd)
        core.play(int(ch), (c_int32 * snd_count)(*snd), int(snd_count), int(loop))
    else:
        core.play1(int(ch), int(snd), int(loop))


def playm(msc: int, *, loop: bool = False) -> None:
    core.playm(int(msc), int(loop))


def stop(ch: int = -1) -> None:
    core.stop(int(ch))


def load_as_old_pyxel_format(filename: str) -> bool:
    import gzip
    import pickle

    dirname = os.path.dirname(inspect.stack()[-1].filename)
    filename = os.path.join(dirname, filename)

    with gzip.open(filename, mode="rb") as fp:
        pickled_data = fp.read()

    if pickled_data[-1:] != pickle.STOP:
        return False

    print("load as old pyxel format")

    _sound = sound
    _music = music

    data = pickle.loads(pickled_data)

    image_list = data.get("image")
    if image_list:
        for i in range(IMAGE_BANK_COUNT - 1):
            image(i).data[:, :] = pickle.loads(image_list[i])

    tilemap_list = data.get("tilemap")
    if tilemap_list:
        if type(tilemap_list[0]) is tuple:
            for i in range(TILEMAP_BANK_COUNT):
                tilemap(i).data[:, :] = pickle.loads(tilemap_list[i][0])
                tilemap(i).refimg = tilemap_list[i][1]
        else:  # todo: delete this block in the future
            for i in range(TILEMAP_BANK_COUNT):
                tilemap(i).data[:, :] = pickle.loads(tilemap_list[i])

    sound_list = data.get("sound")
    if sound_list:
        for i in range(len(sound_list)):
            src = sound_list[i]
            dest = _sound(i)

            dest.note_length = len(src._note)
            for i in range(dest.note_length):
                dest.note[i] = src._note[i]

            dest.tone_length = len(src._tone)
            for i in range(dest.tone_length):
                dest.tone[i] = src._tone[i]

            dest.volume_length = len(src._volume)
            for i in range(dest.volume_length):
                dest.volume[i] = src._volume[i]

            dest.effect_length = len(src._effect)
            for i in range(dest.effect_length):
                dest.effect[i] = src._effect[i]

            dest.speed = src.speed

    music_list = data.get("music")
    if music_list:
        for i in range(len(music_list)):
            src = music_list[i]
            dest = _music(i)

            dest.ch0_length = len(src._ch0)  # type: ignore
            for i in range(dest.ch0_length):  # type: ignore
                dest.ch0[i] = src._ch0[i]  # type: ignore

            dest.ch1_length = len(src._ch1)  # type: ignore
            for i in range(dest.ch1_length):  # type: ignore
                dest.ch1[i] = src._ch1[i]  # type: ignore

            dest.ch2_length = len(src._ch2)  # type: ignore
            for i in range(dest.ch2_length):  # type: ignore
                dest.ch2[i] = src._ch2[i]  # type: ignore

            dest.ch3_length = len(src._ch3)  # type: ignore
            for i in range(dest.ch3_length):  # type: ignore
                dest.ch3[i] = src._ch3[i]  # type: ignore

    return True
