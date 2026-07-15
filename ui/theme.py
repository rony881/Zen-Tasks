"""
This File contains stylesheet themes for the Application
"""
font = "Sans Serif"

h1_font_size = 27
h1_font_weight = "semibold"
h1_font_color = "#121212"

h2_font_size = 23
h2_font_weight =  "semibold"
h2_font_color = "#151515"

h3_font_size = 19
h3_font_weight =  "semibold"
h3_font_color = "#151515"

body_font_size = 16
body_font_color = "#222222"

caption_font_size = 12

# button_font_size = 16
# button_font_weight =  "semibold"

TITLE_STYLE = f"""
    color: #000111;
    font-size: {h1_font_size}px;
    font-weight: {h1_font_weight};
    font-family: sans-serif;

"""

ADD_BTN_STYLE = """
QPushButton {
    background    : #2383E2;
    color         : #FFF;
    border        : none;
    border-radius : 6px;
    font-size     : 16px;
    font-weight   : semibold;
    font-family   : 'Segoe UI', sans-serif;
    padding       : 7px 20px;
}
QPushButton:hover   { background: #1A73CE; }
QPushButton:pressed { background: #1260B5; }
"""

TAB_WIDG_STYLE = """            

QTabBar {
    background      : transparent;
    border-bottom   : 1px solid #cdcdcd;
}

QTabBar::tab {
    background      : transparent;
    color           : #6B6B69;
    border          : 1px solid transparent;
    border-radius   : 6px;
    font-size       : 19 px;
    font-family     : sans-serif;
    padding         : 4px 14px;
    margin          : 8px 2px;
    min-height      : 30px;
}

QTabBar::tab:hover {
    background      : #F0EFED;
    color           : #1C1C1C;
}

QTabBar::tab:selected {
    background      : #E8F3FE;
    color           : #2383E2;
    border          : 1px solid #B4D1F8;
    font-weight     : 600;
}
"""