import re
import base64

# Convert image to base64
with open('/Users/ian/Documents/旅遊/hokkaido_route_b_map.png', 'rb') as img_file:
    img_data = base64.b64encode(img_file.read()).decode('utf-8')
    data_url = f"data:image/png;base64,{img_data}"

with open('/Users/ian/Documents/旅遊/北海道自駕B路線深度計畫書.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Map Section with Base64
# Remove old map section first
content = re.sub(r'<div class="map-section".*?</div>\s*</div>', '', content, flags=re.DOTALL)

map_section = f"""  <div class="map-section" style="margin-bottom: 40px; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.15); background: white;">
    <div style="padding: 20px; background: #1e293b; color: white;">
      <h3 style="margin: 0; display: flex; align-items: center; gap: 10px;">🗺️ 6天5夜道東大環線 路線總覽</h3>
    </div>
    <div style="padding: 10px; text-align: center;">
      <img src="{data_url}" alt="Hokkaido Route B Map" style="max-width: 100%; height: auto; border-radius: 8px;">
      <p style="color: #64748b; font-size: 0.9rem; margin-top: 10px;">新千歲機場 ↔ 帶廣 ↔ 釧路 ↔ 阿寒湖 ↔ 知床 ↔ 網走 ↔ 層雲峽 ↔ 旭川/美瑛</p>
    </div>
  </div>"""

# Re-insert before Day 1
if '<!-- Day 1 -->' in content:
    content = content.replace('<!-- Day 1 -->', map_section + '\n\n  <!-- Day 1 -->', 1)

# 2. Fold initial info
# Find all <div class="notice ..."> blocks
notices = re.findall(r'<div class="notice.*?</div>', content, re.DOTALL)
if notices:
    # Remove them from content
    for n in notices:
        content = content.replace(n, '')
    
    # Re-insert them inside a details tag
    all_notices_html = "\n".join(notices)
    collapsible_notices = f"""
  <details style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; margin-bottom: 30px; padding: 15px; cursor: pointer;">
    <summary style="font-weight: 800; font-size: 1.1rem; color: #1e293b; outline: none; padding: 10px;">
      📢 點擊展開：自駕必看事項、保險、ETC 與航班資訊
    </summary>
    <div style="margin-top: 15px;">
      {all_notices_html}
    </div>
  </details>"""
    
    # Insert right after the hero section (around line 190)
    content = content.replace('<div class="container">', '<div class="container">\n' + collapsible_notices, 1)

with open('/Users/ian/Documents/旅遊/北海道自駕B路線深度計畫書.html', 'w', encoding='utf-8') as f:
    f.write(content)

