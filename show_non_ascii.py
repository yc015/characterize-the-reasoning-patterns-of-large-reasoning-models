from pathlib import Path
text = Path('index.html').read_text(encoding='utf-8')
chars = sorted(set(ch for ch in text if ord(ch) > 127))
for ch in chars:
    idx = text.find(ch)
    snippet = text[max(0, idx-20):idx+20]
    print(ch.encode('unicode_escape').decode('ascii'), '->', snippet.encode('unicode_escape').decode('ascii'))
