import re

with open('/Users/ian/Documents/旅遊/北海道自駕B路線深度計畫書.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the driving badges
content = content.replace('<span class="badge-drive">🚗 自駕</span> ', '')
content = content.replace('<span class="badge-drive">🚗 自駕抵達</span> ', '')
content = content.replace('<span class="badge-drive">🚗 自駕至纜車站</span> ', '')
content = content.replace('<span class="badge-drive" style="background:#8b5cf6">🚡 轉乘纜車</span> ', '')

# 2. Add Japan driving tips
driving_tips = """  <div class="notice flight-info">
    <strong>🔰 首次日本自駕與北海道專屬注意事項</strong>
    <p><strong>【日本右駕基本規則】</strong><br>
    - <strong>方向燈與雨刷相反</strong>：剛上路常會打錯，請保持平常心。<br>
    - <strong>平交道必停</strong>：遇到鐵路平交道，即使柵欄開啟，也必須完全「停車再開」。<br>
    - <strong>紅燈絕對禁止轉彎</strong>：台灣紅燈可右轉，但日本紅燈「無論左右轉皆禁止」，除非有綠色箭頭指示燈。<br>
    - <strong>行人絕對優先</strong>：斑馬線有行人準備通過時，車輛必須完全停讓。<br>
    <br><strong>【道東自駕特殊路段與狀況注意】</strong><br>
    - <strong>野生動物飛撲 (全區皆需注意)</strong>：道東是蝦夷鹿、北狐甚至棕熊的棲息地，特別是清晨與黃昏。看見動物在路邊請減速，若動物突然衝出，<strong>請直接急煞，切勿猛打方向盤</strong>以免翻車。<br>
    - <strong>道東自動車道 (Day 1 千歲至帶廣)</strong>：這段高速公路非常筆直且單調，且多為單線道雙向通行，極易產生「高速公路催眠現象」導致疲勞駕駛。強烈建議在夕張等休息站下車伸展。<br>
    - <strong>知床橫斷道路 (Day 4 知床峠)</strong>：連續彎道的山路，且非常容易起大霧導致視線不佳。強烈建議「絕對不要在此路段夜間駕駛」，下午 3、4 點前盡量下山。<br>
    - <strong>測速照相與警車</strong>：北海道路又直又寬，很容易不知不覺超速。雖然當地人開很快，但請遵循速限，或跟隨車流定速行駛，避免被隱藏警車攔停。</p>
  </div>"""

content = content.replace('<div class="notice flight-info">', driving_tips + '\n\n  <div class="notice flight-info">', 1)

with open('/Users/ian/Documents/旅遊/北海道自駕B路線深度計畫書.html', 'w', encoding='utf-8') as f:
    f.write(content)

