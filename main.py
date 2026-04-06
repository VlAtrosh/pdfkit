import os
from datetime import datetime
from pdf_generator import PDFGenerator
import config

def main():
    """Main function demonstrating PDF generation"""
    
    # Initialize generator
    pdf_gen = PDFGenerator()
    
    # Example 1: Generate from HTML string
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            h1 {{ color: #333; }}
            .header {{ text-align: center; margin-bottom: 30px; }}
            .content {{ line-height: 1.6; }}
            .footer {{ position: fixed; bottom: 0; text-align: center; font-size: 12px; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>PDF Generated with pdfkit</h1>
            <p>Date: {current_date}</p>
        </div>
        <div class="content">
            <h2>Sample Document</h2>
            <p>This is a sample PDF document generated using Python's pdfkit library.</p>
            <p>You can add any HTML content here, including tables, images, and formatted text.</p>
        </div>
        <div class="footer">
            Page <script>document.write(document.page)</script> of <script>document.write(document.pages)</script>
        </div>
    </body>
    </html>
    """
    
    output_file = os.path.join(config.OUTPUT_DIR, "sample_from_string.pdf")
    if pdf_gen.generate_from_html(html_content, output_file):
        print(f"✓ PDF generated successfully: {output_file}")
    else:
        print("✗ Failed to generate PDF")
    
    # Example 2: Generate from template (if template exists)
    template_context = {
        'title': 'Monthly Report',
        'date': datetime.now().strftime("%B %d, %Y"),
        'company': 'Your Company Name',
        'data': [
            {'item': 'Product A', 'quantity': 100, 'price': '$10.00'},
            {'item': 'Product B', 'quantity': 50, 'price': '$25.00'},
            {'item': 'Product C', 'quantity': 75, 'price': '$15.00'},
        ]
    }
    
    output_file = os.path.join(config.OUTPUT_DIR, "sample_from_template.pdf")
    if pdf_gen.generate_from_template('example.html', template_context, output_file):
        print(f"✓ PDF generated from template: {output_file}")
    else:
        print("✗ Failed to generate PDF from template")

if __name__ == "__main__":
    print("PDFKit PDF Generator")
    print("=" * 50)
    
    # Check if wkhtmltopdf is installed
    try:
        import pdfkit
        print("✓ pdfkit is installed")
    except ImportError:
        print("✗ pdfkit is not installed. Run: pip install pdfkit")
        exit(1)
    
    main()