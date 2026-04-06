import pdfkit
from pathlib import Path
from typing import Optional, Dict, Any
from jinja2 import Environment, FileSystemLoader
import config

class PDFGenerator:
    """PDF Generator using pdfkit and Jinja2 templates"""
    
    def __init__(self):
        """Initialize PDF generator with configuration"""
        self.config = config.PDFKIT_CONFIG
        
        # Setup wkhtmltopdf configuration
        if hasattr(config, 'WKHTMLTOPDF_PATH') and config.WKHTMLTOPDF_PATH:
            self.wkhtmltopdf_path = config.WKHTMLTOPDF_PATH
            self.pdf_config = pdfkit.configuration(wkhtmltopdf=self.wkhtmltopdf_path)
            print(f"✓ Using wkhtmltopdf from: {self.wkhtmltopdf_path}")
        else:
            self.wkhtmltopdf_path = None
            self.pdf_config = None
            print("✓ Using wkhtmltopdf from PATH")
            
        # Setup Jinja2 environment
        self.jinja_env = Environment(
            loader=FileSystemLoader(config.TEMPLATES_DIR)
        )
    
    def generate_from_html(self, html_content: str, output_path: str, 
                          options: Optional[Dict] = None) -> bool:
        """
        Generate PDF from HTML string
        
        Args:
            html_content: HTML string content
            output_path: Path to save PDF file
            options: Additional pdfkit options
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            pdf_config = self.config.copy()
            if options:
                pdf_config['options'].update(options)
            
            # Use configuration if available
            if self.pdf_config:
                pdfkit.from_string(html_content, output_path, 
                                 options=pdf_config['options'],
                                 configuration=self.pdf_config)
            else:
                pdfkit.from_string(html_content, output_path, 
                                 options=pdf_config['options'])
            
            return True
        except Exception as e:
            print(f"Error generating PDF: {e}")
            return False
    
    def generate_from_file(self, html_path: str, output_path: str,
                          options: Optional[Dict] = None) -> bool:
        """
        Generate PDF from HTML file
        
        Args:
            html_path: Path to HTML file
            output_path: Path to save PDF file
            options: Additional pdfkit options
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            pdf_config = self.config.copy()
            if options:
                pdf_config['options'].update(options)
            
            if self.pdf_config:
                pdfkit.from_file(html_path, output_path,
                               options=pdf_config['options'],
                               configuration=self.pdf_config)
            else:
                pdfkit.from_file(html_path, output_path,
                               options=pdf_config['options'])
            
            return True
        except Exception as e:
            print(f"Error generating PDF: {e}")
            return False
    
    def generate_from_url(self, url: str, output_path: str,
                         options: Optional[Dict] = None) -> bool:
        """
        Generate PDF from URL
        
        Args:
            url: Webpage URL
            output_path: Path to save PDF file
            options: Additional pdfkit options
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            pdf_config = self.config.copy()
            if options:
                pdf_config['options'].update(options)
            
            if self.pdf_config:
                pdfkit.from_url(url, output_path,
                              options=pdf_config['options'],
                              configuration=self.pdf_config)
            else:
                pdfkit.from_url(url, output_path,
                              options=pdf_config['options'])
            
            return True
        except Exception as e:
            print(f"Error generating PDF: {e}")
            return False
    
    def generate_from_template(self, template_name: str, context: Dict[str, Any],
                              output_path: str, options: Optional[Dict] = None) -> bool:
        """
        Generate PDF from Jinja2 template
        
        Args:
            template_name: Name of template file (e.g., 'report.html')
            context: Dictionary with template variables
            output_path: Path to save PDF file
            options: Additional pdfkit options
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            template = self.jinja_env.get_template(template_name)
            html_content = template.render(**context)
            return self.generate_from_html(html_content, output_path, options)
        except Exception as e:
            print(f"Error generating PDF from template: {e}")
            return False