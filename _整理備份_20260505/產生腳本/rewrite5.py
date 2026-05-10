import re

with open('/Users/ian/Documents/旅遊/北海道自駕B路線深度計畫書.html', 'r', encoding='utf-8') as f:
    content = f.read()

etc_tips = """  <div class="notice flight-info">
    <strong>🛣️ 高速公路收費 (ETC) 與 HEP 建議</strong>
    <p>此行程有兩段主要的收費高速公路路段：<br>
    - <strong>Day 1</strong>：新千歲機場 → 帶廣（道東自動車道，費用約 4,000 日圓）。<br>
    - <strong>Day 6</strong>：旭川/深川區域 → 新千歲機場（道央自動車道，費用約 4,000 日圓）。<br>
    - <strong>其餘路段</strong>：道東地區（如釧路、北見周邊）許多快速道路目前為「免費區間」。<br>
    <br><strong>💡 租車建議：</strong><br>
    1. <strong>必租 ETC 卡</strong>：取車時請務必跟櫃檯租借 ETC 卡（租借費約 330 日圓），過收費站時走 ETC 專用車道即可，不需停車付現，還車時再結清即可。<br>
    2. <strong>考慮購買 HEP (Hokkaido Expressway Pass)</strong>：這是針對外國遊客的「高速公路吃到飽」通行證。以您的 6 天行程來說，HEP 費用約 7,300 日圓，而您來回機場的過路費總計約 8,000 日圓以上，購買 HEP 通常能省下一點錢，更重要的是<strong>省去計算路費的麻煩</strong>，錯過交流道或臨時想開高速公路也沒壓力。</p>
  </div>"""

# Insert after the insurance tips
content = content.replace('<div class="notice parking-info">', etc_tips + '\n\n  <div class="notice parking-info">', 1)

with open('/Users/ian/Documents/旅遊/北海道自駕B路線深度計畫書.html', 'w', encoding='utf-8') as f:
    f.write(content)

