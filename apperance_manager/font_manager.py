import sys

class FontManager(object):
    def __init__(self):
        if sys.platform == "darwin":
            self.button_font = ("Avenir", 16)
            self.note_display_font = ("Avenir", 72)
            self.note_display_font_medium = ("Avenir", 26)
            self.frequency_text_font = ("Avenir", 15)
            self.info_text_font = ("Avenir", 14)
            self.settings_text_font = ("Avenir", 24)

        elif "win" in sys.platform:
            self.button_font = ("Century Gothic", 14)
            self.note_display_font = ("Century Gothic", 62)
            self.note_display_font_medium = ("Century Gothic", 24)
            self.frequency_text_font = ("Century Gothic", 13)
            self.info_text_font = ("Century Gothic", 12)
            self.settings_text_font = ("Century Gothic", 20)

        else:
            self.button_font = ("Century Gothic", 14)
            self.note_display_font = ("Century Gothic", 62)
            self.note_display_font_medium = ("Century Gothic", 24)
            self.frequency_text_font = ("Century Gothic", 13)
            self.info_text_font = ("Century Gothic", 12)
            self.settings_text_font = ("Century Gothic", 20)