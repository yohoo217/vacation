import re

with open('/Users/ian/Documents/旅遊/北海道自駕B路線深度計畫書.html', 'r', encoding='utf-8') as f:
    content = f.read()

map_section = """  <div class="map-section" style="margin-bottom: 40px; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.15); background: white;">
    <div style="padding: 20px; background: #1e293b; color: white;">
      <h3 style="margin: 0; display: flex; align-items: center; gap: 10px;">🗺️ 6天5夜道東大環線 路線總覽</h3>
    </div>
    <div style="padding: 10px; text-align: center;">
      <img src="hokkaido_route_b_map.png" alt="Hokkaido Route B Map" style="max-width: 100%; height: auto; border-radius: 8px;">
      <p style="color: #64748b; font-size: 0.9rem; margin-top: 10px;">新千歲機場 ↔ 帶廣 ↔ 釧路 ↔ 阿寒湖 ↔ 知床 ↔ 網走 ↔ 層雲峽 ↔ 旭川/美瑛</p>
    </div>
  </div>"""

# Insert before Day 1
content = content.replace('<!-- Day 1 -->', map_section + '\n\n  <!-- Day 1 -->', 1)

with open('/Users/ian/Documents/旅遊/北海道自駕B路線深度計畫書.html', 'w', encoding='utf-8') as f:
    f.write(content)

