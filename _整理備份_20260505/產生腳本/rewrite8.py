import re

with open('/Users/ian/Documents/旅遊/北海道自駕B路線深度計畫書.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Ensure the first details block (Notices) is clean
# (Already done in previous script, but let's make it look better)
content = re.sub(
    r'<details style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; margin-bottom: 30px; padding: 15px; cursor: pointer;">',
    r'<details style="background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 12px; margin-bottom: 20px; padding: 5px; cursor: pointer;">',
    content
)

# 2. Fold "行程總覽與歷史深度解析" and "Map Section"
overview_start = content.find('<h2>行程總覽與歷史深度解析</h2>')
map_end = content.find('<!-- Day 1 -->')

if overview_start != -1 and map_end != -1:
    overview_and_map = content[overview_start:map_end]
    folded_overview = f"""
  <details style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; margin-bottom: 30px; padding: 5px; cursor: pointer;">
    <summary style="font-weight: 800; font-size: 1.1rem; color: #1e293b; outline: none; padding: 10px;">
      🗺️ 點擊展開：6天5夜行程總覽與路線地圖
    </summary>
    <div style="margin-top: 15px; padding: 10px;">
      {overview_and_map}
    </div>
  </details>"""
    content = content[:overview_start] + folded_overview + content[map_end:]

with open('/Users/ian/Documents/旅遊/北海道自駕B路線深度計畫書.html', 'w', encoding='utf-8') as f:
    f.write(content)

