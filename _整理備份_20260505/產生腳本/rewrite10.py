import re

with open('/Users/ian/Documents/旅遊/北海道自駕B路線深度計畫書.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Flight & Hotel Info
old_flight_info = """<div class="notice flight-info" style="color: #1e293b;">
    <strong>✈️ 航班與旅遊期間資訊 (5/16 - 5/21)</strong>
    <p><strong>去程：</strong>5/16 06:55 班機（抵達新千歲約 11:30）<br>
    <strong>回程：</strong>5/21 約 16:00 班機（預計 19:00 左右抵達台灣）</p>
  </div>"""

new_flight_info = """<div class="notice flight-info" style="color: #1e293b;">
    <strong>✈️ 航班、出發與賦歸資訊 (5/15 - 5/21)</strong>
    <p><strong>🏨 出發前一晚 (5/15) 住宿：</strong><br>
    - <a href="https://www.agoda.com/zh-tw/cp-hotel-h35445723/hotel/taoyuan-tw.html" target="_blank" style="color:#2563eb; text-decoration:underline;">青埔商旅 (CP-HOTEL)</a> (<a href="https://www.google.com/maps/place/青埔商旅+CP-HOTEL/@25.0049338,121.2103316,17z" target="_blank" style="color:#2563eb; text-decoration:underline;">🗺️ Google Maps</a>)<br>
    - <strong>🚕 前往機場方式 (計程車)：</strong> 飯店距離桃園機場第二航廈約 12 公里，車程約 <strong>15~20 分鐘</strong>。為了趕上 06:55 的長榮 BR166 班機，最晚需在 04:55 抵達機場報到。<strong>強烈建議您安排在 04:30 AM 從飯店搭乘計程車出發。</strong></p>
    <p><strong>✈️ 去程 (5/16)：</strong> 06:55 桃園(TPE) 出發 → 11:55 抵達 新千歲(CTS) (長榮 BR 166)<br>
    <strong>✈️ 回程 (5/21)：</strong> 13:00 新千歲(CTS) 出發 → 16:20 抵達 桃園(TPE) (長榮 BR 165)<br>
    <strong>🚆 返花蓮 (5/21)：</strong> 20:50 桃園車站 出發 → 23:39 抵達 花蓮車站 (普悠瑪 288)</p>
  </div>"""

content = content.replace(old_flight_info, new_flight_info)

# 2. Add Car Rental Info
car_rental_info = """<div class="notice" style="color: #1e293b;">
    <strong>🚘 租車與緊急道路救援聯絡 (ToCoo! 預訂)</strong>
    <p>您的租車是由 ToCoo! 平台預訂的 <strong>Hokkaido Travel Car Rental / Car Rental Hokkaido</strong> 小型油電車。<br>
    - <strong>中文客服與拋錨處理：</strong> 雖然當地租車行可能僅提供日/英文服務，但因為您透過 ToCoo! 預訂並加購了 <strong>T.A.S. (補償 N.O.C 營業損失賠償和道路拖吊費)</strong>，您可以直接使用 ToCoo! 的專屬多國語言支援中心！<br>
    - <strong>⚠️ 遇到事故或拋錨時的標準流程：</strong><br>
      1. 將車輛移至安全處並擺放故障標誌。<br>
      2. 撥打 110 報警取得事故證明 (理賠必備)。<br>
      3. 撥打 <strong>ToCoo! 緊急聯絡電話 (預訂確認信內會提供)</strong>，他們會提供中文線上翻譯，並協助您聯絡租車公司與安排免費的拖吊道路救援。</p>
  </div>"""

content = content.replace('<div class="notice parking-info"', car_rental_info + '\n  <div class="notice parking-info"')

# 3 & 4. Separate Day 5 and 6 and redesign Day 6
day5_start = content.find('<div class="time">Day 5 08:00</div>')
day6_start = content.find('<div class="time">Day 6 08:00</div>')

if day5_start != -1 and day6_start != -1:
    # First, split the container
    day6_html = """
    </div>
  </div>

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
"""
    
    # Locate the end of the timeline
    timeline_end = content.find('<h2>推薦住宿安排</h2>')
    if timeline_end != -1:
        # Extract the content from Day 6 start to the end of the timeline div
        content = content[:day6_start] + day6_html + content[timeline_end:]
    else:
        print("Could not find '推薦住宿安排'")

with open('/Users/ian/Documents/旅遊/北海道自駕B路線深度計畫書.html', 'w', encoding='utf-8') as f:
    f.write(content)

