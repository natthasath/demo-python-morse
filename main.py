from morse.beep import MorseBeep
from morse.blink import MorseCursor

# example usage
mt = MorseBeep(wpm=5)
mt.translate_and_play('Hello world!')

# example usage
mc = MorseCursor(wpm=5)
mc.translate_and_blink('Hello world!')