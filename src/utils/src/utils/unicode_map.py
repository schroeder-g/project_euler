class UnicodeMap:
    characters = {
        # SUPPLEMENTAL LATIN
        "non-breaking space": "\u00A0",  #
        "inverted_exclamation": "\u00A1",  #
        "inverted_question": "\u00BF",  #
        "cent": "\u00A2",  #
        "pound": "\u00A3",  #
        "yen": "\u00A5",  #
        "section": "\u00A7",  #
        "copyright": "\u00A9",  #
        "not": "\u00AC",  #
        "registered": "\u00AE",  #
        "degree": "\u00B0",  #
        "micro": "\u00B5",  #
        "middle_dot": "\u00B7",  #
        "quarter": "\u00BC",  #
        "half": "\u00BD",  #
        "three_quarters": "\u00BE",  #
        # UNICODE SYMBOLS
        "em_dash": "\u2014",  #
        "horiz_bar": "\u2015",  #
        "double_low_line": "\u2016",  #
        "bullet": "\u2022",  #
        # ARROWS
        "single_left_arrow": "\u2190",  #
        "single_up_arrow": "\u2191",  #
        "single_right_arrow": "\u2192",  #
        "single_down_arrow": "\u2193",  #
        "single_bidirectional_arrow": "\u2194",  #
        "single_vertical_bidirectional_arrow": "\u2194",  #
        "thick_left_arrow": "\u21E6",  #
        "thick_up_arrow": "\u21E7",  #
        "thick_right_arrow": "\u21E8",  #
        "thick_down_arrow": "\u21E9",  #
        "thick_bidirectional_arrow": "\u21D4",  #
        "thick_vertical_bidirectional_arrow": "\u21D4",  #
        # MATHEMATICS
        "universal": "\u2200",  #
        "delta": "\u2206",  #
        "contains": "\u2208",  #
        "not_contains": "\u2209",  #
        "pi": "\u220F",  #
        "sigma": "\u2211",  #
        "infinity": "\u221E",  #
        "intersection": "\u2229",  #
        "union": "\u222A",  #
        # MISC TECHNICAL
        "stop_watch": "\u231A",  #
        "hour_glass": "\u231B",  #
        "keyboard": "\u2328",  #
        "circled_star": "\u235F",  #
        "fast_forward": "\u23EC",  #
        "rewind": "\u23ED",  #
        "play_pause": "\u23EF",  #
        # BOX DRAWING
        "light_horizontal": "\u2500",  # ─
        "heavy_horizontal": "\u2501",  # ━
        "light_vertical": "\u2502",  #
        "heavy_vertical": "\u2503",  #
        "light_dash_horizontal": "\u2504",  #
        "heavy_dash_horizontal": "\u2505",  #
        "light_down_right": "\u250C",  #
        "light_down_heavy_right": "\u250D",  #
        "heavy_down_light_right": "\u250E",  #
        "heavy_down_heavy_right": "\u250F",  #
        "double_horizontal": "\u2550",  #
        "double_vertical": "\u2551",  #
        "down_single_right_double": "\u2552",  #
        "down_double_right_single": "\u2552",  #
    }

    @staticmethod
    def get(name, code=None):
        pass
