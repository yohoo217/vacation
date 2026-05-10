import re

with open('/Users/ian/Documents/旅遊/北海道自駕B路線深度計畫書.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Flight info at the top
flight_info = """  <div class="notice flight-info">
    <strong>✈️ 航班與旅遊期間資訊 (5/16 - 5/21)</strong>
    <p><strong>去程：</strong>5/16 06:55 班機（抵達新千歲約 11:30）<br>
    <strong>回程：</strong>5/21 約 16:00 班機（預計 19:00 左右抵達台灣）</p>
  </div>"""

content = content.replace('<div class="notice">', flight_info + '\n\n  <div class="notice">')

# 2. Update car rental info & Day 1
day1_old = """      <div class="event">
        <div class="time">13:30</div>
        <div class="event-title">新千歲機場取車出發</div>
        <div class="event-desc">直接上高速公路前往帶廣，第一天行程輕鬆，適應右駕。</div>
      </div>"""

day1_new = """      <div class="event">
        <div class="time">06:55</div>
        <div class="event-title">✈️ 桃園機場搭機出發</div>
        <div class="event-desc">搭乘 06:55 班機前往北海道。預計約 11:30 抵達新千歲機場。</div>
      </div>
      <div class="event">
        <div class="time">12:30</div>
        <div class="event-title">辦理租車與取車作業</div>
        <div class="event-desc">抵達新千歲機場後，請前往國內線或國際線一樓的「租車櫃檯」報到，隨後搭乘免費接駁車前往機場周邊的營業所辦理取車手續（請備妥駕照正本與日文譯本）。建議預留 1~1.5 小時通關與取車緩衝時間。</div>
      </div>
      <div class="event">
        <div class="time">13:30</div>
        <div class="event-title">取車出發</div>
        <div class="event-desc">辦妥手續後直接上高速公路前往帶廣，第一天行程輕鬆，適應右駕。</div>
      </div>"""
content = content.replace(day1_old, day1_new)

# 3. Update Day 2
day2_old = """      <div class="event">
        <div class="time">08:30</div>
        <div class="event-title">六花亭 帶廣本店</div>"""
day2_new = """      <div class="event">
        <div class="time">08:00</div>
        <div class="event-title">飯店享用早餐與退房準備 (Buffer)</div>
        <div class="event-desc">早上起床享用飯店早餐，8:30 左右退房準備出發。</div>
      </div>
      <div class="event">
        <div class="time">08:30</div>
        <div class="event-title">六花亭 帶廣本店</div>"""
content = content.replace(day2_old, day2_new)

day2_end_old = """      <div class="event">
        <div class="time">16:00</div>
        <div class="event-title">抵達阿寒湖、參觀愛努村（Kotan）</div>
        <div class="event-desc">逛逛傳統木雕工藝店，晚上推薦觀賞阿寒湖愛努劇場的傳統舞蹈或「Lost Kamuy」數位藝術表演。</div>
      </div>
    </div>"""
day2_end_new = """      <div class="event">
        <div class="time">16:00</div>
        <div class="event-title">抵達阿寒湖、參觀愛努村（Kotan）</div>
        <div class="event-desc">逛逛傳統木雕工藝店，晚上推薦觀賞阿寒湖愛努劇場的傳統舞蹈或「Lost Kamuy」數位藝術表演。</div>
      </div>
      <div class="event">
        <div class="time">18:00</div>
        <div class="event-title">♨️ 飯店晚餐與溫泉休息</div>
        <div class="event-desc">於溫泉飯店內享用豐盛的晚餐（一泊二食），飯後享受阿寒湖溫泉，洗去一天的疲憊。</div>
      </div>
    </div>"""
content = content.replace(day2_end_old, day2_end_new)

# 4. Update Day 3
day3_old = """      <div class="event">
        <div class="time">09:30</div>
        <div class="event-title">摩周湖第一展望台</div>"""
day3_new = """      <div class="event">
        <div class="time">08:00</div>
        <div class="event-title">飯店早餐與退房準備 (Buffer)</div>
        <div class="event-desc">享受早晨溫泉與豐盛早餐，從容退房。</div>
      </div>
      <div class="event">
        <div class="time">09:30</div>
        <div class="event-title">摩周湖第一展望台</div>"""
content = content.replace(day3_old, day3_new)

day3_end_old = """      <div class="event">
        <div class="time">15:30</div>
        <div class="event-title">知床宇登呂溫泉區</div>
        <div class="event-desc">提早抵達溫泉飯店，享受面海的露天風呂，欣賞知床夕陽。</div>
      </div>
    </div>"""
day3_end_new = """      <div class="event">
        <div class="time">15:30</div>
        <div class="event-title">知床宇登呂溫泉區</div>
        <div class="event-desc">提早抵達溫泉飯店，享受面海的露天風呂，欣賞知床夕陽。</div>
      </div>
      <div class="event">
        <div class="time">18:00</div>
        <div class="event-title">♨️ 飯店晚餐與知床之夜</div>
        <div class="event-desc">於飯店內享用知床在地海鮮晚餐，準備迎接隔天的自然探索。</div>
      </div>
    </div>"""
content = content.replace(day3_end_old, day3_end_new)

# 5. Update Day 4
day4_old = """      <div class="event">
        <div class="time">08:30</div>
        <div class="event-title">知床五湖 高架木道</div>"""
day4_new = """      <div class="event">
        <div class="time">08:00</div>
        <div class="event-title">飯店早餐與退房準備 (Buffer)</div>
        <div class="event-desc">吃過早餐後提早出門，前往知床五湖。</div>
      </div>
      <div class="event">
        <div class="time">08:30</div>
        <div class="event-title">知床五湖 高架木道</div>"""
content = content.replace(day4_old, day4_new)

day4_end_old = """      <div class="event">
        <div class="time">16:00</div>
        <div class="event-title">博物館 網走監獄</div>
        <div class="event-desc">參觀這座充滿歷史感、被稱為「最難逃脫」的監獄，了解北海道早期由囚犯以血淚開拓道路的沉重歷史。</div>
      </div>
    </div>"""
day4_end_new = """      <div class="event">
        <div class="time">16:00</div>
        <div class="event-title">博物館 網走監獄</div>
        <div class="event-desc">參觀這座充滿歷史感、被稱為「最難逃脫」的監獄，了解北海道早期由囚犯以血淚開拓道路的沉重歷史。</div>
      </div>
      <div class="event">
        <div class="time">18:00</div>
        <div class="event-title">網走市區晚餐與飯店休息</div>
        <div class="event-desc">於網走市區尋找當地居酒屋或特色餐廳享用晚餐，飯後返回飯店休息。</div>
      </div>
    </div>"""
content = content.replace(day4_end_old, day4_end_new)

# 6. Update Day 5
day5_old = """      <div class="event">
        <div class="time">Day 5 09:30</div>
        <div class="event-title">北見 北狐牧場 (北きつね牧場)</div>"""
day5_new = """      <div class="event">
        <div class="time">Day 5 08:00</div>
        <div class="event-title">飯店早餐與退房準備 (Buffer)</div>
        <div class="event-desc">於網走飯店用過早餐後，驅車前往北見方向。</div>
      </div>
      <div class="event">
        <div class="time">Day 5 09:30</div>
        <div class="event-title">北見 北狐牧場 (北きつね牧場)</div>"""
content = content.replace(day5_old, day5_new)

day5_end_old = """      <div class="event">
        <div class="time">Day 5 15:30</div>
        <div class="event-title">黑岳纜車 (Kurodake Ropeway)</div>
        <div class="event-desc">搭乘纜車至五合目，欣賞大雪山連峰的壯麗山景。5月山頂可能還有殘雪。</div>
      </div>"""
day5_end_new = """      <div class="event">
        <div class="time">Day 5 15:30</div>
        <div class="event-title">黑岳纜車 (Kurodake Ropeway)</div>
        <div class="event-desc">搭乘纜車至五合目，欣賞大雪山連峰的壯麗山景。5月山頂可能還有殘雪。</div>
      </div>
      <div class="event">
        <div class="time">Day 5 17:30</div>
        <div class="event-title">♨️ 層雲峽溫泉飯店入住與晚餐</div>
        <div class="event-desc">結束一天的自然之旅，入住層雲峽溫泉飯店，享用晚餐與溫泉，放鬆身心。</div>
      </div>"""
content = content.replace(day5_end_old, day5_end_new)

# 7. Update Day 6 (Return to Taiwan adjustment)
day6_old = """      <div class="event">
        <div class="time">Day 6 09:00</div>
        <div class="event-title">離開層雲峽</div>
        <div class="event-desc">沿著國道向旭川方向前進。</div>
      </div>
      <div class="event">
        <div class="time">Day 6 09:30</div>
        <div class="event-title">層雲峽晨間散步 ｜ 黑岳石室下層探索</div>
        <div class="event-desc">享受清新空氣。</div>
      </div>
      <div class="event">
        <div class="time">Day 6 10:30</div>
        <div class="event-title">美瑛 白金青池 (青い池)</div>
        <div class="event-desc">短暫繞行至美瑛，欣賞如夢似幻的寶石藍池水。</div>
      </div>
      <div class="event">
        <div class="time">Day 6 11:00</div>
        <div class="event-title">🌾 美瑛 拼布之路 ｜ 四季彩之丘</div>
        <div class="event-desc">開車穿越起伏的丘陵農田，享受北海道特有的田園風光。</div>
      </div>
      <div class="event">
        <div class="time">Day 6 12:30</div>
        <div class="event-title">🍜 午餐：旭川拉麵村 (あさひかわラーメン村)</div>
        <div class="event-desc">匯集了多家旭川著名拉麵店，以醬油拉麵最為經典，為旅程畫下美味句點。</div>
      </div>
      <div class="event">
        <div class="time">Day 6 15:00</div>
        <div class="event-title">新千歲機場還車</div>
        <div class="event-desc">走高速公路返回新千歲，請記得先加滿油再至租車營業所還車，搭乘接駁車至機場準備搭機。</div>
      </div>"""

day6_new = """      <div class="event">
        <div class="time">Day 6 08:00</div>
        <div class="event-title">飯店早餐與退房準備 (Buffer)</div>
        <div class="event-desc">由於今日要搭機返回台灣，建議早上 08:00 吃完早餐後儘早退房出發。</div>
      </div>
      <div class="event">
        <div class="time">Day 6 09:00</div>
        <div class="event-title">美瑛 白金青池 (青い池)</div>
        <div class="event-desc">離開層雲峽後直接前往美瑛，欣賞如夢似幻的寶石藍池水。</div>
      </div>
      <div class="event">
        <div class="time">Day 6 10:00</div>
        <div class="event-title">🌾 美瑛 拼布之路</div>
        <div class="event-desc">開車穿越起伏的丘陵農田，享受北海道特有的田園風光。</div>
      </div>
      <div class="event">
        <div class="time">Day 6 11:30</div>
        <div class="event-title">🍜 午餐：砂川SA 或 沿途快速用餐</div>
        <div class="event-desc">為確保趕上回程班機，建議午餐在高速公路休息站（如砂川SA）快速解決，或外帶輕食車上享用。</div>
      </div>
      <div class="event">
        <div class="time">Day 6 14:00</div>
        <div class="event-title">新千歲機場周邊還車</div>
        <div class="event-desc">走高速公路返回新千歲，請記得先加滿油再至租車營業所還車，搭乘免費接駁車至機場航廈。</div>
      </div>
      <div class="event">
        <div class="time">Day 6 14:30</div>
        <div class="event-title">機場報到與免稅店最後採買</div>
        <div class="event-desc">辦理登機手續、托運行李。新千歲機場國內線與國際線皆有豐富的伴手禮與免稅店可做最後採買。</div>
      </div>
      <div class="event">
        <div class="time">Day 6 16:00</div>
        <div class="event-title">✈️ 搭機準備返回台灣</div>
        <div class="event-desc">結束充滿回憶的 6 天 5 夜北海道自駕深度之旅。</div>
      </div>
      <div class="event">
        <div class="time">Day 6 19:00</div>
        <div class="event-title">抵達台灣</div>
        <div class="event-desc">約晚上 19 點左右抵達台灣，平安返家。</div>
      </div>"""
content = content.replace(day6_old, day6_new)

with open('/Users/ian/Documents/旅遊/北海道自駕B路線深度計畫書.html', 'w', encoding='utf-8') as f:
    f.write(content)

