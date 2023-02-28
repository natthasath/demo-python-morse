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

    def __init__(self, dot_duration=0.2, dash_duration=0.5, letter_pause=0.2, word_pause=0.6):
        self.dot_duration = dot_duration
        self.dash_duration = dash_duration
        self.letter_pause = letter_pause
        self.word_pause = word_pause

    def text_to_morse(self, text):
        morse = ''
        for letter in text.upper():
            if letter != ' ':
                morse += self.MORSE_CODE_DICT.get(letter, '') + ' '
            else:
                morse += ' '
        return morse

    def blink_cursor(self, length):
        for i in range(length):
            print('_', end='', flush=True)
            time.sleep(self.dot_duration)

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

# example usage
mc = MorseCursor()
mc.translate_and_blink('Hello world!')
