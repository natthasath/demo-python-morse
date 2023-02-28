import time
import winsound

class MorseBeep:
    MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 
                        'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---',
                        'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---',
                        'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-',
                        'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--',
                        'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-',
                        '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',
                        '0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.',
                        '-':'-....-', '(':'-.--.', ')':'-.--.-'}

    def __init__(self, wpm=20, farnsworth=False):
        self.dot_duration = 1200 / (wpm * (1 if not farnsworth else 2))
        self.dash_duration = 3 * self.dot_duration
        self.letter_pause = self.dot_duration
        self.word_pause = 7 * self.dot_duration

    def text_to_morse(self, text):
        morse = ''
        for letter in text.upper():
            if letter != ' ':
                morse += self.MORSE_CODE_DICT.get(letter, '') + ' '
            else:
                morse += ' '
        return morse

    def play_sound(self, duration):
        # Play a beep sound for the specified duration in milliseconds
        winsound.Beep(440, int(duration))

    def translate_and_play(self, text):
        morse = self.text_to_morse(text)
        for letter in morse:
            if letter == '.':
                self.play_sound(self.dot_duration)
                time.sleep(self.letter_pause / 1000)
            elif letter == '-':
                self.play_sound(self.dash_duration)
                time.sleep(self.letter_pause / 1000)
            elif letter == ' ':
                time.sleep(self.word_pause / 1000)
            else:
                # Invalid character, ignore it
                pass