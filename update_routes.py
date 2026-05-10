import re
import urllib.parse

html_path = '/Users/ian/Documents/旅遊/_整理備份_20260505/朝聖之路/葡萄牙朝聖之路簡報.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update CSS grid
html = html.replace('grid-template-columns:1fr 1fr;', 'grid-template-columns:repeat(3, 1fr);')

# Data for the 3 routes
days = [
    ("Day 2", "Porto", "抵達日：市區準備約 1-2 hr / 2-4 km"),
    ("Day 3", "Moreira da Maia", "Porto -> Moreira da Maia：約 3-4 hr / 13 km"),
    ("Day 4", "Vilarinho / Vairão", "Moreira da Maia -> Vilarinho：約 4-5 hr / 15 km"),
    ("Day 5", "São Pedro de Rates", "Vilarinho -> Rates：約 4-5 hr / 15 km"),
    ("Day 6", "Barcelos", "Rates -> Barcelos：約 4-5 hr / 16 km"),
    ("Day 7", "Balugães", "Barcelos -> Balugães：約 4-5 hr / 15 km"),
    ("Day 8", "Ponte de Lima", "Balugães -> Ponte de Lima：約 5-6 hr / 18 km"),
    ("Day 9", "Rubiães", "Ponte de Lima -> Rubiães：約 4.75-6 hr / 17.4 km"),
    ("Day 10", "Tui", "Rubiães -> Tui：約 4.75-5.5 hr / 19.1 km"),
    ("Day 11", "O Porriño", "Tui -> O Porriño：約 4-5 hr / 16 km"),
    ("Day 12", "Redondela", "O Porriño -> Redondela：約 4-5 hr / 16.4 km"),
    ("Day 13", "Pontevedra", "Redondela -> Pontevedra：約 5-6 hr / 19.6 km"),
    ("Day 14", "Combarro", "Pontevedra -> Combarro：約 3-4 hr / 11 km"),
    ("Day 15", "Armenteira", "Combarro -> Armenteira：約 3.5-5 hr / 10 km"),
    ("Day 16", "Vilanova de Arousa", "Armenteira -> Vilanova：約 5.75-7 hr / 23.4 km"),
    ("Day 17", "O Milladoiro", "Vilanova -> Milladoiro：船 1.5 hr + 約 4-5 hr / 17 km"),
    ("Day 18", "Santiago", "Milladoiro -> Santiago：約 2-2.5 hr / 8 km")
]

route1_data = [
    ("Hotel Spot Family Suites Porto", "舒適、交通簡單，適合抵達整理"),
    ("Hotel Singular Porto Aeroporto", "機場周邊，第一天步行後進出方便"),
    ("Casa Mindela Guesthouse", "偏民宿型，舒適度高"),
    ("O Palhuço Pilgrims Hostel Pedra Furada", "此區星號唯一選項"),
    ("Hotel Bagoeira", "市區機能好，補給與晚餐方便"),
    ("Quinta da Cancela", "鄉間住宿，適合把節奏放慢"),
    ("ARC MY OTEL", "舒適度高，爬升日前好好休息"),
    ("Quinta do Caminho", "環境優美，翻越山頭後能好好放鬆"),
    ("A Torre do Xudeu", "進入西班牙後的舒適休整點"),
    ("Alojamientos Central", "市區補給方便，評價好"),
    ("Alvear Suites", "套房型，適合人流變多後保留休息品質"),
    ("Rias Bajas Hotel", "進老城方便，隔天進入靈性變體"),
    ("Casa Noelmar", "海濱住宿，舒適度高"),
    ("Hospedería Monasterio de Armenteira", "修道院住宿，和這段路線氛圍很合"),
    ("Hotel Leal La Sirena", "抵達海邊後舒適休息"),
    ("Casa Rural As Bentinas", "品質穩定的鄉村住宿"),
    ("Hospedería San Martín Pinario", "就近大教堂，完美收尾")
]

route2_data = [
    ("Hotel Spot Family Suites Porto", "共同選項"),
    ("Hotel Singular Porto Aeroporto", "共同選項"),
    ("Casa Mindela Guesthouse", "共同選項"),
    ("O Palhuço Pilgrims Hostel Pedra Furada", "體驗傳統朝聖者停靠點"),
    ("In Barcelos Hostel & Guest House", "青旅氛圍，可認識各國朝聖者"),
    ("Casa da Fernanda", "熱門朝聖者名宿，務必提早確認"),
    ("Albergue de Peregrinos de Ponte de Lima", "經典庇護所，感受濃烈朝聖氣氛"),
    ("Casa das Lages", "山區少數住宿選擇之一"),
    ("Albergue de Peregrinos de Tui", "進入最後百公里，準備加強蓋章"),
    ("Alojamiento Camino Portugués", "庇護所選項，交流豐富"),
    ("Santiago de Vilavella", "公立庇護所，人流多需早到"),
    ("Rias Bajas Hotel", "共同選項"),
    ("Albergue de Combarro", "經濟實惠，離海近"),
    ("Caroi Hostel & Rooms", "修道院旁青旅替代方案"),
    ("Albergue A Salazón", "沿海庇護所，感受海風"),
    ("Albergue Milladoiro", "大型庇護所，準備隔天進城"),
    ("Hospedería San Martín Pinario", "共同選項")
]

route3_data = [
    ("Hotel Spot Family Suites Porto", "共同選項"),
    ("Hotel Singular Porto Aeroporto", "共同選項"),
    ("Casa Mindela Guesthouse", "共同選項"),
    ("O Palhuço Pilgrims Hostel Pedra Furada", "共同選項"),
    ("Hotel Bagoeira", "市區補給後舒適休息"),
    ("Casa da Fernanda", "穿插熱門朝聖名宿體驗"),
    ("ARC MY OTEL", "大城鎮選擇旅館保留隱私"),
    ("Casa das Lages", "山區不同民宿體驗"),
    ("Ideas Peregrinas", "現代青旅，設計感強且舒適"),
    ("Pensión Cando", "小型民宿，安靜休息"),
    ("A Casa da Herba", "特色民宿，體驗不同風格"),
    ("Rias Bajas Hotel", "大城市住飯店好逛街"),
    ("Casa Noelmar", "海濱美景民宿"),
    ("Caroi Hostel & Rooms", "混搭青旅平衡預算"),
    ("Hotel Leal La Sirena", "住好一點準備搭船"),
    ("Pensión O Camiño Milladoiro", "進城前最後一晚寧靜"),
    ("Hospedería San Martín Pinario", "共同選項")
]

def make_map_url(route_data, days):
    stops = []
    for i, (hotel, _) in enumerate(route_data):
        stops.append(f"{hotel}, {days[i][1]}, Portugal" if i < 8 else f"{hotel}, {days[i][1]}, Spain")
    origin = urllib.parse.quote_plus(stops[0])
    daddr = "+to:".join(urllib.parse.quote_plus(stop) for stop in stops[1:])
    return f"https://maps.google.com/maps?saddr={origin}&daddr={daddr}&dirflg=w"

def build_table(route_data, days):
    html_tb = '<table class="route-table">\n<thead><tr><th>日程</th><th>落腳點</th><th>建議住宿</th></tr></thead>\n<tbody>\n'
    for i in range(len(days)):
        day_num, city, leg_meta = days[i]
        hotel, note = route_data[i]
        html_tb += f'<tr><td>{day_num}</td><td>{city}</td><td><span class="place">⭐ {hotel}</span><div class="note">{note}</div><div class="leg-meta">{leg_meta}</div></td></tr>\n'
    html_tb += '</tbody>\n</table>'
    return html_tb

col1 = f"""      <div class="compare-column">
        <div class="compare-head">
          <h3>路線 1：舒適優先</h3>
          <p>在星號名單中，優先為您挑選旅館、套房與民宿，確保沿途擁有較佳的睡眠品質與私人衛浴。</p>
          <div class="route-actions"><a class="route-link" target="_blank" href="{make_map_url(route1_data, days)}">舒適路線總地圖</a></div>
        </div>
        {build_table(route1_data, days)}
      </div>"""

col2 = f"""      <div class="compare-column">
        <div class="compare-head" style="background:rgba(52,211,153,0.1);">
          <h3 style="color:#6ee7b7;">路線 2：庇護所優先</h3>
          <p>在星號名單中，優先挑選朝聖者庇護所或青年旅館，讓您能深度體驗 Camino 的交流氛圍。</p>
          <div class="route-actions"><a class="route-link" target="_blank" href="{make_map_url(route2_data, days)}">庇護所路線總地圖</a></div>
        </div>
        {build_table(route2_data, days)}
      </div>"""

col3 = f"""      <div class="compare-column">
        <div class="compare-head" style="background:rgba(96,165,250,0.1);">
          <h3 style="color:#93c5fd;">路線 3：混搭與第三備案</h3>
          <p>為您篩選出星號名單中的第三個選項，或是將旅館與青旅交錯安排，達成預算與體力的平衡。</p>
          <div class="route-actions"><a class="route-link" target="_blank" href="{make_map_url(route3_data, days)}">混搭路線總地圖</a></div>
        </div>
        {build_table(route3_data, days)}
      </div>"""

new_grid = f'<div class="compare-grid">\n{col1}\n{col2}\n{col3}\n    </div>'

start_str = '<div class="compare-grid">'
end_str = '    </div>\n  </div>\n</section>'

start_idx = html.find(start_str)
end_idx = html.find(end_str)

if start_idx != -1 and end_idx != -1:
    new_html = html[:start_idx] + new_grid + html[end_idx:]
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Successfully updated routes.")
else:
    print("Could not find compare-grid block. start_idx:", start_idx, "end_idx:", end_idx)
