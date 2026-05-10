import re

html_path = '/Users/ian/Documents/旅遊/_整理備份_20260505/朝聖之路/葡萄牙朝聖之路簡報.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Day 1 flight slide
old_day1 = '<div class="day-card flight"><div class="day-label">Day 1 ｜ 🛫 去程航班與倫敦住宿</div><div class="day-text"><div class="route-line">台北 (TPE) ➔ 曼谷 (BKK) ➔ 倫敦 (LHR/LGW)</div><span class="decision">去程已確認：台北 ➔ 曼谷 ➔ 倫敦，倫敦機場附近住一晚。隔天飛波多。</span></div></div>'
new_day1 = '<div class="day-card flight"><div class="day-label">Day 1 (6/6) ｜ 🛫 去程航班與倫敦住宿</div><div class="day-text"><div class="route-line">6/6 台北 (TPE) 08:15 ➔ 倫敦 (LHR) 19:20 (長榮 BR67)</div><span class="decision">去程已確認：抵達倫敦後，於機場附近住一晚，隔天清晨飛波多。</span></div></div>'
html = html.replace(old_day1, new_day1)

# Replace Day 2 flight slide
old_day2 = '<div class="day-card flight"><div class="day-label">Day 2 ｜ 抵達與準備</div><div class="day-text"><div class="route-line">倫敦飛往波多，抵達後辦理朝聖前置事項</div><span class="transport">前往波多主教座堂購買朝聖者護照，採買行動糧水</span></div></div>'
new_day2 = '<div class="day-card flight"><div class="day-label">Day 2 (6/7) ｜ 抵達波多與準備</div><div class="day-text"><div class="route-line">6/7 倫敦 06:10 ➔ 里斯本轉機 ➔ 波多 (OPO) 13:00 (TP1353/1922)</div><span class="transport">13:00 抵達波多後，前往主教座堂購買朝聖者護照與採買物資</span></div></div>'
html = html.replace(old_day2, new_day2)

# Replace Return flight slide
old_return = '<div class="day-card flight"><div class="day-label">Day 22/23 ｜ 🛫 回程航班待議</div><div class="day-text"><div class="route-line">Barcelona (BCN) ➔ 轉機點 ➔ 台北 (TPE)</div><span class="decision">實際日期依巴塞隆納停留 2–3 天與票價決定</span></div></div>'
new_return = '<div class="day-card flight"><div class="day-label">7/8 ｜ 🛫 回程航班</div><div class="day-text"><div class="route-line">7/8 倫敦 (LHR) 21:35 ➔ 台北 (TPE) (長榮 BR68)</div><span class="decision">回程已確認：巴塞隆納結束後，將有約兩週彈性時間，最後於 7/8 從倫敦返台。</span></div></div>'
html = html.replace(old_return, new_return)

# Replace dayDetails array lines
html = html.replace("['Day 1','台北 → 曼谷 → 倫敦','航班確認；倫敦會住一晚，Mabel 會訂機場附近住宿。','把第一晚倫敦住宿與隔天到波多的航班接駁準備好。']", "['Day 1 (6/6)','台北 → 倫敦','長榮 BR67 (08:15 - 19:20)。抵達後入住倫敦機場周邊住宿。','準備隔天清晨的班機前往波多。']")
html = html.replace("['Day 2','Porto 前置日','辦 Credencial、買 SIM/eSIM、採買水壺/行動糧、確認隔日路線與天氣。','建議先試走到主教座堂周邊，熟悉黃箭頭與貝殼標誌。']", "['Day 2 (6/7)','倫敦 → 波多 (13:00 抵達)','葡萄牙航空 TP1353/1922 (06:10 LHR - 13:00 OPO)。抵達後前往市區辦 Credencial。','下午可到主教座堂周邊熟悉黃箭頭與採買。']")
html = html.replace("['Day 21/22','Barcelona 彈性日','依停留 2 或 3 天決定海邊、市場、Montjuic 或自由購物。','回程航班待議，最後一天住宿看起飛時間決定是否續住。']", "['Day 21~','Barcelona 與彈性行程','朝聖結束後有充足時間，可安排巴塞隆納及其他歐洲行程。','7/8 晚上 21:35 由倫敦 (LHR) 搭機返台。']")

# Slide 1 text update
old_badge = '<span class="badge">🇬🇧 去程曼谷轉機、倫敦停留一晚</span>'
new_badge = '<span class="badge">🇬🇧 6/6 去程、7/8 回程 (長榮/倫敦進出)</span>'
html = html.replace(old_badge, new_badge)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated flights successfully.")
