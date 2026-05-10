import re

with open('/Users/ian/Documents/旅遊/北海道自駕B路線深度計畫書.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all events
events = re.findall(r'<div class="time">(.*?)</div>\s*<div class="event-title">(.*?)</div>\s*<div class="event-desc">(.*?)</div>', content, re.DOTALL)

for i, (time, title, desc) in enumerate(events):
    print(f"Event {i}: {time} | {title}")

