import google.generativeai as genai
from pathlib import Path
import json

def read_file(filename):
    """Read content from the input file."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: {filename} not found!")
        return None

def setup_gemini():
    """Configure and get Gemini model."""
    try:
        GOOGLE_API_KEY = "AIzaSyAjhjE1-c6vcFixyO6lOIHQUE8a15peRd0"
        genai.configure(api_key=GOOGLE_API_KEY)
        
  
        generation_config = {
            "temperature": 0.7,
            "top_p": 0.8,
            "top_k": 40,
            "max_output_tokens": 2048,
        }
        
        # Initialize model
        model = genai.GenerativeModel(
            model_name="gemini-pro",
            generation_config=generation_config
        )
        
        return model
    except Exception as e:
        print(f"Error setting up Gemini: {str(e)}")
        return None

def generate_html_with_gemini(model, content):
    """Use Gemini to generate HTML from the content."""
    try:
        prompt = f"""
        Generate a visually appealing HTML page for the following content. 
        Requirements:
        - Use modern, clean design
        - Include proper styling with CSS
        - Use semantic HTML5 elements
        - Include proper formatting and spacing
        - Add visual hierarchy with typography
        - Use a pleasant color scheme
        - Include any relevant sections or divisions based on the content
        
        Here's the content to format:
        
        {content}
        
        Provide only the complete HTML code without any explanations or markdown.
        """
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error generating HTML: {str(e)}")
        return None

def save_html(html_content, output_file):
    """Save the generated HTML to a file."""
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"HTML report successfully generated: {output_file}")
        return True
    except Exception as e:
        print(f"Error saving HTML file: {str(e)}")
        return False

def main():
    # Setup
    input_file = "geminioutput.txt"
    output_file = "generated_report.html"
    
    content = read_file(input_file)
    if not content:
        return
    model = setup_gemini()
    if not model:
        return

    html_content = generate_html_with_gemini(model, content)
    if not html_content:
        return
    
 
    save_html(html_content, output_file)

if __name__ == "__main__":
    main()