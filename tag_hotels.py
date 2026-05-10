import re

html_path = '/Users/ian/Documents/旅遊/_整理備份_20260505/朝聖之路/葡萄牙朝聖之路簡報.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

cat_map = {
    'Hotel Spot Family Suites Porto': '旅館',
    'Hotel Singular Porto Aeroporto': '旅館',
    'Casa Mindela Guesthouse': '民宿',
    'O Palhuço Pilgrims Hostel Pedra Furada': '庇護所',
    'Hotel Bagoeira': '旅館',
    'In Barcelos Hostel & Guest House': '青旅',
    'Quinta da Cancela': '民宿',
    'Casa da Fernanda': '庇護所',
    'ARC MY OTEL': '旅館',
    'Albergue de Peregrinos de Ponte de Lima': '庇護所',
    'Casa das Lages': '民宿',
    'Quinta do Caminho': '民宿',
    'Ideas Peregrinas': '青旅',
    'A Torre do Xudeu': '旅館',
    'Albergue de Peregrinos de Tui': '庇護所',
    'Pensión Cando': '民宿',
    'Alojamientos Central': '民宿',
    'Alojamiento Camino Portugués': '庇護所',
    'Alvear Suites': '旅館',
    'A Casa da Herba': '民宿',
    'Santiago de Vilavella': '庇護所',
    'Rias Bajas Hotel': '旅館',
    'Casa Noelmar': '民宿',
    'Albergue de Combarro': '庇護所',
    'Hospedería Monasterio de Armenteira': '旅館',
    'Caroi Hostel & Rooms': '青旅',
    'Hotel Leal La Sirena': '旅館',
    'Albergue A Salazón': '庇護所',
    'Pensión O Camiño Milladoiro': '民宿',
    'Casa Rural As Bentinas': '民宿',
    'Albergue Milladoiro': '庇護所',
    'Hospedería San Martín Pinario': '旅館'
}

def get_tag_html(cat):
    color = "#94a3b8"
    bg = "rgba(148, 163, 184, 0.15)"
    if cat == '旅館':
        color = "#60a5fa"
        bg = "rgba(96, 165, 250, 0.15)"
    elif cat == '民宿':
        color = "#f472b6"
        bg = "rgba(244, 114, 182, 0.15)"
    elif cat in ['庇護所', '青旅']:
        color = "#a3e635"
        bg = "rgba(163, 230, 53, 0.15)"
        
    return f'<span style="font-size:0.7rem; color:{color}; background:{bg}; border:1px solid {color}; border-radius:4px; padding:1px 4px; margin-left:6px; vertical-align:middle;">{cat}</span>'

# Replace only if not already tagged
for hotel, cat in cat_map.items():
    find_str = f'<span class="place">⭐ {hotel}</span>'
    repl_str = f'<span class="place">⭐ {hotel}</span>{get_tag_html(cat)}'
    
    # Avoid double replacing
    if repl_str not in html:
        html = html.replace(find_str, repl_str)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Added tags for accommodations.")
