import re

filepath = "/Users/leticiarequiel/Downloads/rodrigo_bio_deploy/index.html"

iframe_code = '''<iframe 
  width="100%" 
  height="450" 
  src="https://www.youtube.com/embed?listType=playlist&list=PLMjb0v-gZ4uU" 
  frameborder="0" 
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
  allowfullscreen>
</iframe>'''

try:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Pattern to find the existing iframe
    pattern = r'<iframe[^>]*youtube[^>]*>.*?</iframe>'
    
    # We will also add the rounded-2xl shadow-md class so it matches the layout, but height is 450 as requested
    iframe_code = iframe_code.replace('height="450"', 'height="450" class="rounded-2xl shadow-md"')
    
    new_content = re.sub(pattern, iframe_code, content, flags=re.DOTALL)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Updated iframe in {filepath}")
except FileNotFoundError:
    print(f"File not found: {filepath}")
