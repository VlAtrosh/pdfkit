from pdf_generator import PDFGenerator
import config
import os

def basic_examples():
    """Simple examples of PDF generation"""
    
    pdf_gen = PDFGenerator()
    
    # Simple HTML to PDF
    simple_html = """
    <html>
    <body>
        <h1>Hello World!</h1>
        <p>This is my first PDF generated with pdfkit.</p>
    </body>
    </html>
    """
    
    output = os.path.join(config.OUTPUT_DIR, "hello_world.pdf")
    if pdf_gen.generate_from_html(simple_html, output):
        print("Created hello_world.pdf")
    
    # PDF from URL
    url_output = os.path.join(config.OUTPUT_DIR, "webpage.pdf")
    # Uncomment to test with a real URL
    # pdf_gen.generate_from_url("https://example.com", url_output)
    
    # Custom PDF options
    landscape_html = """
    <html>
    <body>
        <h1>Landscape PDF</h1>
        <p>This PDF uses landscape orientation.</p>
    </body>
    </html>
    """
    
    landscape_output = os.path.join(config.OUTPUT_DIR, "landscape.pdf")
    pdf_gen.generate_from_html(
        landscape_html, 
        landscape_output,
        options={'orientation': 'Landscape'}
    )

if __name__ == "__main__":
    basic_examples()