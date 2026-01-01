import os
import sys
import webview
from backend.api import Api

def get_base_dir():
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    
    return os.path.dirname(os.path.abspath(__file__))

def get_html_path():
    return os.path.join(get_base_dir(), 'frontend', 'index.html')

if __name__ == '__main__':
    api = Api()

    window = webview.create_window(
        title='AI Email Sender',
        url=get_html_path(),
        js_api=api,
        width=1000,
        height=800,
        resizable=True
    )

    webview.start(debug=False)