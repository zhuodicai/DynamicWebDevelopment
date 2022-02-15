base = [0, 0]

areas = [
    [1260, 730, 1330, 1020, 1530, 1010, 1620, 800],
    [1530, 467, 1780, 590, 1830, 470, 1760, 430],
    [200, 590, 560, 650, 580, 570, 460, 500],
    [780, 530, 900, 585, 1140, 480, 940, 470],
    [690, 720, 700, 850, 990, 800, 790, 690],
]
width = 1800
actual_width = 1900
scale = width / actual_width

for news_idx, area in enumerate(areas):
    for idx in range(len(area)):
        area[idx] = str(int(area[idx] * scale - base[idx % 2]))
    coords = ",".join(area)
    res = f'<area shape="poly" coords="{coords}" href="./news/news_{news_idx+1}.html">'
    print(res)
