import re

html_path = '/Users/ian/Documents/旅遊/_整理備份_20260505/朝聖之路/葡萄牙朝聖之路簡報.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove star from recommended routes table
html = html.replace('<span class="place">⭐ ', '<span class="place">')

# 2. Replace text tags with emojis
def old_tag(cat):
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

def new_tag(cat):
    if cat == '旅館':
        return '<span title="旅館" style="font-size:1.1rem; margin-left:6px; vertical-align:middle; cursor:help;">🏨</span>'
    elif cat == '民宿':
        return '<span title="民宿" style="font-size:1.1rem; margin-left:6px; vertical-align:middle; cursor:help;">🏡</span>'
    elif cat in ['庇護所', '青旅']:
        return f'<span title="{cat}" style="font-size:1.1rem; margin-left:6px; vertical-align:middle; cursor:help;">🛏️</span>'
    return ""

for cat in ['旅館', '民宿', '庇護所', '青旅']:
    html = html.replace(old_tag(cat), new_tag(cat))

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated icons and removed stars in routes.")
