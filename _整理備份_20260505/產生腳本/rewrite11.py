import re

with open('/Users/ian/Documents/旅遊/北海道自駕B路線深度計畫書.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Locate the beginning of Day 6 events
day6_start_match = re.search(r'\s*<div class="event">\s*<div class="time">Day 6 08:00</div>', content)
if not day6_start_match:
    print("Day 6 start not found!")
    exit(1)

day6_start_idx = day6_start_match.start()

# Now find the end of the timeline div that contains Day 6
# It's right before <div class="hotel-section">
hotel_section_match = re.search(r'\s*</div>\s*<div class="hotel-section">\s*<h4>🏨 Day 5', content[day6_start_idx:])
if not hotel_section_match:
    print("Hotel section for Day 5 not found after Day 6!")
    exit(1)

timeline_end_idx = day6_start_idx + hotel_section_match.start()

# Delete the Day 6 events from the Day 5 timeline
content = content[:day6_start_idx] + content[timeline_end_idx:]

# Now, we need to insert the new Day 6 card AFTER the entire Day 5 card.
# Find the end of the Day 5 card.
# The Day 5 card ends right before </body> or right after its hotel-section.
# Let's find </div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</body>
# Actually, the easiest way is to find the closing div of the whole container or </body>
body_match = content.rfind('</div>\s*</body>')
if body_match == -1:
    body_match = content.rfind('</body>')

day6_html = """
  <!-- Day 6 -->
  <div class="day-card">
    <div class="day-header">
      <div class="day-title">Day 6：依依不捨的賦歸</div>
      <div class="day-route">層雲峽 → 新千歲機場 (約 200km) → 台灣</div>
    </div>

    <div class="history-box" style="background: rgba(59, 130, 246, 0.05); border: 1px dashed rgba(59, 130, 246, 0.3);">
      <h4>✈️ 返程特別提醒</h4>
      <p>由於您的回程班機為 13:00 起飛，依照國際線規定需提前 2 小時 (11:00) 抵達機場，加上機場租車營業所辦理還車與搭乘接駁車回航廈需預留 30 分鐘，因此最遲必須在 <strong>10:30 前完成還車</strong>。層雲峽距離新千歲機場約 200 公里，走高速公路需 2.5 至 3 小時。因此，<strong>今天無法安排其他觀光行程，吃完早餐後請直接上路！</strong></p>
    </div>

    <div class="timeline">
      <div class="event">
        <div class="time">07:00</div>
        <div class="event-title">飯店享用早餐與退房</div>
        <div class="event-desc">為了趕上飛機，今天必須早起。07:00 享用飯店早餐，最晚 07:30 務必退房出發。</div>
      </div>
      <div class="event">
        <div class="time">07:30</div>
        <div class="event-title">層雲峽出發 直奔新千歲</div>
        <div class="event-desc">從層雲峽出發，駛入上川層雲峽 IC 上高速公路（道央自動車道）。沿途如需上廁所，可短暫停留「砂川 SA」休息站。</div>
      </div>
      <div class="event">
        <div class="time">10:30</div>
        <div class="event-title">新千歲機場周邊營業所還車</div>
        <div class="event-desc">導航請設定回租車營業所。還車前<strong>務必加滿油</strong>（營業所附近通常有指定加油站），並保留收據以供檢查。完成手續後搭乘免費接駁車前往國際線航廈。</div>
      </div>
      <div class="event">
        <div class="time">11:00</div>
        <div class="event-title">機場報到與最後採買</div>
        <div class="event-desc">辦理長榮航空報到與托運行李。通關後，在新千歲機場國內線/國際線航廈進行最後的免稅品採買（如白色戀人、薯條三兄弟、六花亭等）。</div>
      </div>
      <div class="event">
        <div class="time">13:00</div>
        <div class="event-title">✈️ 搭機返回台灣 (BR 165)</div>
        <div class="event-desc">搭乘 13:00 班機，告別美麗的北海道。</div>
      </div>
      <div class="event">
        <div class="time">16:20</div>
        <div class="event-title">抵達台灣 桃園國際機場</div>
        <div class="event-desc">抵達桃園機場第二航廈，領取行李並通關。</div>
      </div>
      <div class="event">
        <div class="time">20:50</div>
        <div class="event-title">🚆 轉乘台鐵 普悠瑪 288 返回花蓮</div>
        <div class="event-desc">從桃園車站搭乘 20:50 發車的普悠瑪 288 車次，預計將於 23:39 抵達溫暖的家（花蓮車站）。<br><span class="badge-meal">晚餐建議</span> 由於距離火車發車有一段時間，建議可以在機場或桃園車站附近享用晚餐。</div>
      </div>
    </div>
  </div>
</div>
"""

content = content[:body_match] + day6_html + content[body_match:]

with open('/Users/ian/Documents/旅遊/北海道自駕B路線深度計畫書.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
