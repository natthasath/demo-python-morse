import winsound
import time

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

    def __init__(self, frequency=800, dot_duration=100, dash_duration=300, letter_pause=0.2, word_pause=0.6):
        self.frequency = frequency
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

    def beep_morse(self, morse):
        for letter in morse:
            if letter == '.':
                winsound.Beep(self.frequency, self.dot_duration)
            elif letter == '-':
                winsound.Beep(self.frequency, self.dash_duration)
            elif letter == ' ':
                time.sleep(self.letter_pause)
            elif letter == '/':
                time.sleep(self.word_pause)

    def translate_and_beep(self, text):
        morse = self.text_to_morse(text)
        self.beep_morse(morse)