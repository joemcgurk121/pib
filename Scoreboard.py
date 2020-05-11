from Helpers import color_name_to_rgb_tuple
from apa102 import Apa102PixelStrip
from Digit import Digit

class Scoreboard:
    num_leds = 58
    led_strip = Apa102PixelStrip(num_leds)

    def __init__(self, home_color, away_color):
        self.led_values = []
        self.score_hyphen_color_value = color_name_to_rgb_tuple['purple']
        self.home_color_value = color_name_to_rgb_tuple[home_color]
        self.away_color_value = color_name_to_rgb_tuple[away_color]
        self.hour_color_value = color_name_to_rgb_tuple['purple']
        self.minute_color_value = color_name_to_rgb_tuple['purple']
        self.clock_hyphen_color_value = color_name_to_rgb_tuple['purple']
        self.char_color_value = color_name_to_rgb_tuple['white']
        self.char_hyphen_color_value = color_name_to_rgb_tuple['black']
        self.digits = []
        self.reset_led_values(self.score_hyphen_color_value)
        for i in range(4):
            self.digits.append(Digit(i))

    def reset_led_values(self, hyphen_color_value):
        self.led_values = [(0, 0, 0)] * self.num_leds
        self.led_values[-1] = hyphen_color_value
        self.led_values[-2] = hyphen_color_value

    def score_to_digits(self, score):
        return [score // 10, score % 10]

    def token_to_digits(self, token):
        return [(token // 1000), ((token % 1000) // 100), ((token % 100) // 10), (token % 10)]

    def show_score(self, home_score, away_score):
        self.reset_led_values(self.score_hyphen_color_value)
        numbers_to_display = self.score_to_digits(home_score)
        numbers_to_display += self.score_to_digits(away_score)

        leds_to_display = []
        for i in range(len(numbers_to_display)):
            leds_to_display += self.digits[i].leds_for_display_number(numbers_to_display[i])

        for led in leds_to_display:
            if(led <= 27):
                self.led_values[led] = self.home_color_value
            else:
                self.led_values[led] = self.away_color_value
        self.led_strip.value = self.led_values

    def show_time(self, hour, minute):
        self.reset_led_values(self.clock_hyphen_color_value)
        numbers_to_display = self.score_to_digits(hour)
        numbers_to_display += self.score_to_digits(minute)

        leds_to_display = []
        for i in range(len(numbers_to_display)):
            leds_to_display += self.digits[i].leds_for_display_number(numbers_to_display[i])

        for led in leds_to_display:
            if(led <= 27):
                self.led_values[led] = self.hour_color_value
            else:
                self.led_values[led] = self.minute_color_value
        self.led_strip.value = self.led_values

    def show_chars(self, chars_to_display):
        self.reset_led_values(self.char_hyphen_color_value)

        leds_to_display = []
        for i in range(len(chars_to_display)):
            leds_to_display += self.digits[i].leds_for_display_char(chars_to_display[i])

        for led in leds_to_display:
            self.led_values[led] = self.char_color_value
        self.led_strip.value = self.led_values

    def show_token(self, token):
        self.reset_led_values(self.score_hyphen_color_value)
        numbers_to_display = self.token_to_digits(token)

        leds_to_display = []
        for i in range(len(numbers_to_display)):
            leds_to_display += self.digits[i].leds_for_display_number(numbers_to_display[i])

        for led in leds_to_display:
            self.led_values[led] = self.hyphen_color_value
        self.led_strip.value = self.led_values

    def show_final_score(self, home_score, away_score):
        self.reset_led_values(self.score_hyphen_color_value)
        numbers_to_display = self.score_to_digits(home_score)
        numbers_to_display += self.score_to_digits(away_score)

        leds_to_display = []
        for i in range(len(numbers_to_display)):
            leds_to_display += self.digits[i].leds_for_display_number(numbers_to_display[i])
        for led in leds_to_display:
            self.led_values[led] = self.hyphen_color_value
        self.led_strip.value = self.led_values

    def sleep(self):
        self.led_values = [(0, 0, 0)] * self.num_leds
        self.led_strip.value = self.led_values
