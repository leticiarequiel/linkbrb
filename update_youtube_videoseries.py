import re

filepath = "/Users/leticiarequiel/Downloads/rodrigo_bio_deploy/index.html"

iframe_code = '''<iframe 
  class="rounded-2xl shadow-md"
  width="100%" 
  height="450" 
  src="https://www.youtube.com/embed/videoseries?list=PLMjb0v-gZ4uU" 
  frameborder="0" 
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
  allowfullscreen>
</iframe>'''

try:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Pattern to find the existing iframe
    pattern = r'<iframe[^>]*youtube[^>]*>.*?</iframe>'
    
    new_content = re.sub(pattern, iframe_code, content, flags=re.DOTALL)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Updated iframe in {filepath}")
except FileNotFoundError:
    print(f"File not found: {filepath}")
