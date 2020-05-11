from Helpers import number_to_segment
from Segment import Segment

class Digit:

    def __init__(self, index):
        self.segments = []
        self.index = index
        self.create_segments()

    def create_segments(self):
        for i in range(7):
            first_led = (self.index * 14) + (i * 2)
            self.segments.append(Segment(first_led, first_led + 1))

    def leds_for_display_char(self, display_char):
        segments_for_display_char = char_to_segment[display_char]

        leds = []
        for segment_index in segments_for_display_char:
            leds += self.segments[segment_index].leds
        return leds

    def leds_for_display_number(self, display_number):
        segments_for_display_number = number_to_segment[str(display_number)]

        leds = []
        for segment_index in segments_for_display_number:
            leds += self.segments[segment_index].leds
        return leds
