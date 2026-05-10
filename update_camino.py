import re

path = '/Users/ian/Documents/旅遊/_整理備份_20260505/朝聖之路/葡萄牙朝聖之路簡報.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

hotels = [
    'Hotel Spot Family Suites Porto',
    'Hotel Singular Porto Aeroporto',
    'Casa Mindela Guesthouse',
    'O Palhuço Pilgrims Hostel Pedra Furada',
    'Hotel Bagoeira',
    'In Barcelos Hostel & Guest House',
    'Quinta da Cancela',
    'Casa da Fernanda',
    'ARC MY OTEL',
    'Albergue de Peregrinos de Ponte de Lima',
    'Casa das Lages',
    'Quinta do Caminho',
    'Ideas Peregrinas',
    'A Torre do Xudeu',
    'Albergue de Peregrinos de Tui',
    'Pensión Cando',
    'Alojamientos Central',
    'Alojamiento Camino Portugués',
    'Alvear Suites',
    'A Casa da Herba',
    'Santiago de Vilavella',
    'Rias Bajas Hotel',
    'Casa Noelmar',
    'Albergue de Combarro',
    'Hospedería Monasterio de Armenteira',
    'Caroi Hostel & Rooms',
    'Hotel Leal La Sirena',
    'Albergue A Salazón',
    'Pensión O Camiño Milladoiro',
    'Casa Rural As Bentinas',
    'Albergue Milladoiro',
    'Hospedería San Martín Pinario'
]

# Extract stayDays string and replace
start_idx = content.find('const stayDays=[')
end_idx = content.find('];\n\nfunction enc(q)')
if start_idx != -1 and end_idx != -1:
    stayDays_str = content[start_idx:end_idx]
    for hotel in hotels:
        stayDays_str = stayDays_str.replace(f"'{hotel}'", f"'⭐ {hotel}'")
    content = content[:start_idx] + stayDays_str + content[end_idx:]

# JS replacements
js_replacements = [
    (
"""function stayRow(option, city){
  const [band,name,price,bathStatus,bathClass,directUrl]=option;
  const query=`${name} ${city}`;
  const directLink=directUrl ? `<a href="${directUrl}" target="_blank" class="link-phone">住宿直連</a>` : '';
  const bookingLink=bookingDirect[name] ? `<a href="${bookingDirect[name]}" target="_blank" class="link-booking">Booking直連</a>` : '';
  const agodaLink=agodaDirect[name] ? `<a href="${agodaDirect[name]}" target="_blank" class="link-agoda">Agoda直連</a>` : '';""",
"""function stayRow(option, city){
  const [band,name,price,bathStatus,bathClass,directUrl]=option;
  const cleanName=name.replace(/^⭐\\s*/, '');
  const query=`${cleanName} ${city}`;
  const directLink=directUrl ? `<a href="${directUrl}" target="_blank" class="link-phone">住宿直連</a>` : '';
  const bookingLink=bookingDirect[cleanName] ? `<a href="${bookingDirect[cleanName]}" target="_blank" class="link-booking">Booking直連</a>` : '';
  const agodaLink=agodaDirect[cleanName] ? `<a href="${agodaDirect[cleanName]}" target="_blank" class="link-agoda">Agoda直連</a>` : '';"""
    ),
    (
"""function stayMapBlock(city, options){
  const stops=options.map(option=>`${option[1]} ${city}`);
  const mapLinks=options.map(option=>{
    const query=`${option[1]} ${city}`;
    return `<a href="${maps(query)}" target="_blank" class="link-map">${option[1]}</a>`;
  }).join('');""",
"""function stayMapBlock(city, options){
  const stops=options.map(option=>`${option[1].replace(/^⭐\\s*/, '')} ${city}`);
  const mapLinks=options.map(option=>{
    const cleanName=option[1].replace(/^⭐\\s*/, '');
    const query=`${cleanName} ${city}`;
    return `<a href="${maps(query)}" target="_blank" class="link-map">${option[1]}</a>`;
  }).join('');"""
    ),
    (
"""function routeStayInfo(){
  const stayInfo=new Map();
  stayDays.forEach(day=>{
    day.options.forEach(option=>{
      const [band,name,price,bathStatus,bathClass,directUrl]=option;
      stayInfo.set(name,{band,name,price,bathStatus,bathClass,directUrl,city:day.city});
    });
  });""",
"""function routeStayInfo(){
  const stayInfo=new Map();
  stayDays.forEach(day=>{
    day.options.forEach(option=>{
      const [band,name,price,bathStatus,bathClass,directUrl]=option;
      const cleanName=name.replace(/^⭐\\s*/, '');
      stayInfo.set(cleanName,{band,name,price,bathStatus,bathClass,directUrl,city:day.city});
    });
  });"""
    )
]

for old_str, new_str in js_replacements:
    content = content.replace(old_str, new_str)

# London text replacements
content = content.replace('🇸🇬 去程新加坡轉機待議', '🇬🇧 去程曼谷轉機、倫敦停留一晚')
content = content.replace('去程待議：預計在新加坡轉機並短暫停留，實際航班與停留時間再確認', '去程已確認：台北 ➔ 曼谷 ➔ 倫敦，倫敦機場附近住一晚。隔天飛波多。')
content = content.replace('台北 (TPE) ➔ 新加坡 (SIN) ➔ 葡萄牙波多 (OPO)', '台北 (TPE) ➔ 曼谷 (BKK) ➔ 倫敦 (LHR/LGW)')
content = content.replace('<div class="day-label">Day 1 ｜ 🛫 去程航班待議</div>', '<div class="day-label">Day 1 ｜ 🛫 去程航班與倫敦住宿</div>')
content = content.replace("['Day 1','台北 → 新加坡 → 波多','航班待議；確認新加坡停留長度、轉機行李規則、歐洲入境資料與旅平險。','把第一晚 Porto 住宿與機場到市區交通先訂好。']", "['Day 1','台北 → 曼谷 → 倫敦','航班確認；倫敦會住一晚，Mabel 會訂機場附近住宿。','把第一晚倫敦住宿與隔天到波多的航班接駁準備好。']")

content = content.replace('<div class="route-line">抵達波多，辦理朝聖前置事項</div>', '<div class="route-line">倫敦飛往波多，抵達後辦理朝聖前置事項</div>')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Update complete")
