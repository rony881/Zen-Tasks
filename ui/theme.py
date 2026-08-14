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
    font-weight: semibold;
    font-family: sans-serif;

"""

PRIORITY_COLORS = {
    "Low":      {"bg": "#E8F5E9", "text": "#2E7D32"},  # soft green
    "Medium":   {"bg": "#FFF3E0", "text": "#EF6C00"},  # soft amber
    "High":     {"bg": "#FBE9E7", "text": "#D84315"},  # soft deep orange
    "Critical": {"bg": "#FFEBEE", "text": "#C62828"},  # soft red
}


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

PRIORITY_STYLE = """
QComboBox {
    color: #6B6B69;
    background: transparent;
    border: 1px solid #cccccc;
    border-bottom: 1px solid #cdcdcd;
    border-top: 1px solid #cccccc;
    border-radius: 6px;
    padding: 4px 10px;
    min-width: 100px;
}

QComboBox QAbstractItemView {
    background: white;
    border: 1px solid #777777;
    border-radius: 6px;
    outline: none;
}

QComboBox QAbstractItemView::item {
    color: #6B6B69;
    padding: 6px 10px;
    min-height: 24px;
}

QComboBox QAbstractItemView::item:selected {
    background: #2383E2;
    color: white;
}

QComboBox QAbstractItemView::item:hover {
    background: #1A73CE;
    color: #ffffff;
}
"""

SUBMIT_BTN_STYLE = """
    QPushButton {
        background: #1A73CE;
        color: white;
        border: none;
        border-radius: 6px;
        padding: 0 24px;
        font-size: 14px;
        font-weight: 700;
    }
    QPushButton:hover   { background: #2383E2; }
    QPushButton:pressed { background: #1260B5; }
"""
CANCEL_BTN_STYLE = """
    QPushButton {
        background: transparent;
        color: #666666;
        border: 1px solid #a1a1a1;
        border-radius: 6px;
        padding: 0 24px;
        font-size: 14px;
    }
    QPushButton:hover   { background: #F0F0F0; }
    QPushButton:pressed { background: #cdcdcd; }
"""

TASK_INPUT_STYLE = """
    QTextEdit {
        border: none;
        font-size: 17px;
        color: #444444;
        background: transparent;
    }
"""

CLOSE_BTN_STYLE = """
    QPushButton {
        border: none; border-radius: 14px;
        color: #888; font-size: 14px; background: transparent;
    }
    QPushButton:hover { background: #F0F0F0; color: #111111; }
"""

DIALOG_CARD_STYLE = """
    QWidget#container {
        background: #FFFFFF;
        border-radius: 16px;
        border: 1px solid #e8e8e8;
    }
    """