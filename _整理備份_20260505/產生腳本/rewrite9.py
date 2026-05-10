import re
import base64

# Convert new image to base64
with open('/Users/ian/Documents/旅遊/hokkaido_route_b_map_new.png', 'rb') as img_file:
    img_data = base64.b64encode(img_file.read()).decode('utf-8')
    data_url = f"data:image/png;base64,{img_data}"

with open('/Users/ian/Documents/旅遊/北海道自駕B路線深度計畫書.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Map Section with NEW Base64
content = re.sub(
    r'<img src="data:image/png;base64,.*?" alt="Hokkaido Route B Map"',
    f'<img src="{data_url}" alt="Hokkaido Route B Map"',
    content
)

# 2. Fix colors for first details block (Notices)
# Old: background: #eff6ff; border: 1px solid #bfdbfe; color: #1e293b
content = re.sub(
    r'<details style="background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 12px; margin-bottom: 20px; padding: 5px; cursor: pointer;">',
    r'<details style="background: #1e293b; border: 2px solid #3b82f6; border-radius: 12px; margin-bottom: 20px; padding: 5px; cursor: pointer; color: white;">',
    content
)
content = re.sub(
    r'📢 點擊展開：自駕必看事項、保險、ETC 與航班資訊\s*</summary>',
    r'📢 點擊展開：自駕必看事項、保險、ETC 與航班資訊</summary>',
    content
)
# Ensure the summary text is white for the dark background
content = content.replace('color: #1e293b; outline: none; padding: 10px;">\n      📢 點擊展開', 'color: #ffffff; outline: none; padding: 10px;">\n      📢 點擊展開')

# 3. Fix colors for second details block (Map)
# Old: background: #f8fafc; border: 1px solid #e2e8f0;
content = re.sub(
    r'<details style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; margin-bottom: 30px; padding: 5px; cursor: pointer;">',
    r'<details style="background: #334155; border: 2px solid #64748b; border-radius: 12px; margin-bottom: 30px; padding: 5px; cursor: pointer; color: white;">',
    content
)
content = content.replace('color: #1e293b; outline: none; padding: 10px;">\n      🗺️ 點擊展開', 'color: #ffffff; outline: none; padding: 10px;">\n      🗺️ 點擊展開')

# Ensure the notice boxes inside have dark text since their background is light
content = content.replace('<div class="notice flight-info">', '<div class="notice flight-info" style="color: #1e293b;">')
content = content.replace('<div class="notice parking-info">', '<div class="notice parking-info" style="color: #1e293b;">')
content = content.replace('<div class="notice">', '<div class="notice" style="color: #1e293b;">')

with open('/Users/ian/Documents/旅遊/北海道自駕B路線深度計畫書.html', 'w', encoding='utf-8') as f:
    f.write(content)

