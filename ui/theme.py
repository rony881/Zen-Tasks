"""
This File contains stylesheet themes for the Application
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
    font-size       : 12.5px;
    font-family     : 'Segoe UI', sans-serif;
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

ADD_BTN_STYLE = """
QPushButton {
    background    : #2383E2;
    color         : #FFF;
    border        : none;
    border-radius : 6px;
    font-size     : 14px;
    font-weight   : 600;
    font-family   : 'Segoe UI', sans-serif;
    padding       : 7px 20px;
}
QPushButton:hover   { background: #1A73CE; }
QPushButton:pressed { background: #1260B5; }
"""