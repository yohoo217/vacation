import re

with open('/Users/ian/Documents/旅遊/北海道自駕B路線深度計畫書.html', 'r', encoding='utf-8') as f:
    content = f.read()

insurance_tips = """  <div class="notice flight-info">
    <strong>🛡️ 日本租車保險強烈建議：請直上「最高等級全險」</strong>
    <p>在日本租車，基本費用已包含法定的第三人責任險（無限額），但若發生事故，您仍須負擔「免責額」與「營業損失（NOC）」。強烈建議首次自駕直接購買<strong>最高等級的安心保險包（包含 CDW + NOC 豁免 + 道路救援）</strong>：<br>
    - <strong>CDW (免責補償制度)</strong>：免除您在車輛損毀或財損時，所需支付的 5~10 萬日圓自負額。<br>
    - <strong>NOC (營業損失賠償) 豁免 【最重要！】</strong>：若車輛因刮傷或事故需維修，租車公司會索取 2~5 萬日圓的營業損失。保了 NOC 豁免（各家名稱不同，如 RAP、ECO、安心保險），即使是不小心A到保險桿、被蝦夷鹿撞到、或是停在停車場被別人刮傷，您都<strong>完全不需要賠錢</strong>。<br>
    - <strong>⚠️ 注意事項</strong>：若透過 Klook、Tabirai 等第三方平台訂車，通常只含 CDW。<strong>請務必在抵達機場營業所取車時，向櫃檯人員表示要「加購最高保險（Full Coverage / NOC Support）」</strong>，一天通常只需多加 1000~2000 日圓，能換來整趟旅程的絕對安心。</p>
  </div>"""

# Insert right after the flight-info notice or driving tips notice
content = content.replace('<div class="notice parking-info">', insurance_tips + '\n\n  <div class="notice parking-info">', 1)

with open('/Users/ian/Documents/旅遊/北海道自駕B路線深度計畫書.html', 'w', encoding='utf-8') as f:
    f.write(content)

