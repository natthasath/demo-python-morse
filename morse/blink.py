import time

class MorseCursor:
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
        self.dot_duration = 1.2 / (wpm * (1 if not farnsworth else 2))
        self.dash_duration = 3 * self.dot_duration
        self.letter_pause = self.dot_duration
        self.word_pause = 3 * self.dot_duration

    def text_to_morse(self, text):
        morse = ''
        for letter in text.upper():
            if letter != ' ':
                morse += self.MORSE_CODE_DICT.get(letter, '') + ' '
            else:
                morse += ' '
        return morse

    def blink_cursor(self, length):
        print('_', end='', flush=True)
        time.sleep(length * self.dot_duration)

    def translate_and_blink(self, text):
        morse = self.text_to_morse(text)
        for letter in morse:
            if letter == '.':
                self.blink_cursor(1)
                time.sleep(self.letter_pause)
            elif letter == '-':
                self.blink_cursor(3)
                time.sleep(self.letter_pause)
            elif letter == ' ':
                time.sleep(self.word_pause)
                print(' ', end='', flush=True)