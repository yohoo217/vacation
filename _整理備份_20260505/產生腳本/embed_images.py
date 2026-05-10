import re
import base64
import os

html_path = '/Users/ian/Documents/旅遊/北海道自駕B路線深度計畫書.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

def replacer(match):
    img_path = match.group(1)
    # Handle the leading ./ if present
    clean_path = img_path
    if img_path.startswith('./'):
        clean_path = img_path[2:]
    
    full_path = os.path.join('/Users/ian/Documents/旅遊', clean_path)
    
    if os.path.exists(full_path):
        with open(full_path, 'rb') as img_file:
            encoded_string = base64.b64encode(img_file.read()).decode('utf-8')
        
        mime_type = 'image/png'
        if full_path.lower().endswith('.jpg') or full_path.lower().endswith('.jpeg'):
            mime_type = 'image/jpeg'
            
        data_uri = f'data:{mime_type};base64,{encoded_string}'
        return f'src="{data_uri}"'
    else:
        print(f"File not found: {full_path}")
        return match.group(0)

new_html = re.sub(r'src="(\.\/房間圖片\/[^"]+)"', replacer, html_content)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_html)

# Also update the one in Pictures just in case
pic_path = '/Users/ian/Pictures/旅遊/北海道自駕B路線深度計畫書.html'
if os.path.exists(pic_path):
    with open(pic_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Updated Pictures folder HTML as well.")

print("Done.")
