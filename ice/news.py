import os.path as osp

newses = [
    ["title 1", "content 1 <br> content 1"],
    ["title 2", "content 2 <br> content 2"],
    ["title 3", "content 3 <br> content 3"],
    ["title 4", "content 4 <br> content 4"],
    ["title 5", "content 5 <br> content 5"],
]

for idx, (title, body) in enumerate(newses):
    f = open(osp.join("news", f"news_{idx+1}.html"), "w")
    print(
        f"""
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
    <body style="background:#314156;">
    <div align="center" style="color: white;">
        <h1>{title}</h1>
        <p>{body}</p>
        <img src='../asset/float{idx+1}.png'/>
    </div>
  </body>
</html
""".strip(),
        file=f,
    )
    f.close()
