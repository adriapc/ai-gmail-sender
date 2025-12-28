import os
import webview
from backend.api import Api

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_html_path():
    return os.path.join(BASE_DIR, 'frontend', 'index.html')

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