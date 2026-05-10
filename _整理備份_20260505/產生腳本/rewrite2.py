import re

with open('/Users/ian/Documents/旅遊/北海道自駕B路線深度計畫書.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add CSS for parking badge
css_old = """  .badge-warning { display: inline-block; background: #ef4444; color: #fef2f2; font-size: 0.8rem; font-weight: 800; padding: 2px 8px; border-radius: 4px; margin-left: 8px; vertical-align: middle; }"""
css_new = """  .badge-warning { display: inline-block; background: #ef4444; color: #fef2f2; font-size: 0.8rem; font-weight: 800; padding: 2px 8px; border-radius: 4px; margin-left: 8px; vertical-align: middle; }
  .badge-parking { display: inline-block; background: #10b981; color: #f0fdf4; font-size: 0.8rem; font-weight: 800; padding: 2px 8px; border-radius: 4px; margin-left: 8px; vertical-align: middle; }
  .badge-drive { display: inline-block; background: #6366f1; color: #f0fdf4; font-size: 0.8rem; font-weight: 800; padding: 2px 8px; border-radius: 4px; margin-right: 8px; vertical-align: middle; }"""
content = content.replace(css_old, css_new)

# 2. Add General Notice about Driving & Parking
notice_old = """  <div class="notice flight-info">"""
notice_new = """  <div class="notice parking-info">
    <strong>🚗 全程自駕與停車說明</strong>
    <p>此行程為<strong>全程自駕路線</strong>，點到點之間完全依靠開車移動，不需搭乘大眾運輸。北海道道東地區地廣人稀，<strong>所有排定的景點與飯店皆設有專屬停車場</strong>。<br>
    - <strong>飯店停車</strong>：溫泉區飯店多為免費停車；帶廣、網走等市區飯店可能酌收每晚約 500~1000 日圓的停車費。<br>
    - <strong>景點停車</strong>：多數自然景點為免費停車，少數如知床五湖（約 500 日圓）、摩周湖第一展望台（與硫磺山共用券約 500 日圓）需收取單次停車費。</p>
  </div>

  <div class="notice flight-info">"""
content = content.replace(notice_old, notice_new)

# 3. Add parking tags to hotels
# We will use regex to append <span class="badge-parking">🅿️ 附設停車場</span> after <div class="hotel-price">...</div>
content = re.sub(
    r'(<div class="hotel-price">.*?</div>)',
    r'\1\n          <span class="badge-parking">🅿️ 附設停車場</span>',
    content
)

# 4. Prefix event descriptions with driving info
# Instead of modifying all, we can do a blanket replace for "event-desc\">"
content = re.sub(
    r'(<div class="event-desc">)',
    r'\1<span class="badge-drive">🚗 自駕</span> ',
    content
)

# Fix Day 1 starting flight which is not driving
content = content.replace('<span class="badge-drive">🚗 自駕</span> 搭乘 06:55 班機', '搭乘 06:55 班機')

# Fix Day 4 Kurodake ropeway which involves ropeway
content = content.replace(
    '<span class="badge-drive">🚗 自駕</span> 搭乘纜車至五合目',
    '<span class="badge-drive">🚗 自駕至纜車站</span> <span class="badge-drive" style="background:#8b5cf6">🚡 轉乘纜車</span> 搭乘纜車至五合目'
)

# Fix Shiretoko walking
content = content.replace(
    '<span class="badge-drive">🚗 自駕</span> 參觀這座充滿歷史感',
    '<span class="badge-drive">🚗 自駕抵達</span> 參觀這座充滿歷史感'
)

with open('/Users/ian/Documents/旅遊/北海道自駕B路線深度計畫書.html', 'w', encoding='utf-8') as f:
    f.write(content)

