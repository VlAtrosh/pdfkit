import os

# Configuration for pdfkit
PDFKIT_CONFIG = {
    'options': {
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': 'UTF-8',
        'no-outline': None,
        'enable-local-file-access': None
    }
}

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')

# Create directories if they don't exist
os.makedirs(TEMPLATES_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

WKHTMLTOPDF_PATH = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
# WKHTMLTOPDF_PATH = '/usr/local/bin/wkhtmltopdf'  # Linux/Mac