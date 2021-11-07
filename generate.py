import json


def _clean():
    with open('puzzle.html', 'w') as f:
        f.write("""
<html>
<head>
<title>Musical Chairs</title>
<link href="https://fonts.googleapis.com/css?family=EB+Garamond:300,400,500,600,700|Roboto+Mono:300,400,500,600,700" rel="stylesheet">
<link href="main.css" rel="stylesheet">
</head>
<body>
<div class="content">
<h1>Musical Chairs</h1>
<div class="puzzle">
<p class="flavor"><i></i></p>""")


def _write(html):
    with open('puzzle.html', 'a') as f:
        f.write(f'\n{html}')

def _close():
    with open('puzzle.html', 'a') as f:
        f.write("""
</div>
<script src="main.js"></script>
</body>
</html>
""")

def generate_puzzle():
    _clean()

    data_set = json.load(open('_spoilers.json'))
    for (i, d) in enumerate(data_set):
        assert d["No."] == i + 1

    alpha_data_set = sorted(data_set, key=lambda x: x['Role'])

    _write('<ul>')
    for d in alpha_data_set:
        _write(f'<li>{d["Clue"]}</li>')
    _write('</ul>')

    _write('<hr/>')

    extraction = ''
    for d in data_set[0:-1]:
        _write('<div class="row">')
        for i in range(len(d["Role"])):
            if i + 1 == d["Index"]:
                extraction += d["Role"][i]
                _write('<input maxlength=1 class="e"/>')
            else:
                _write('<input maxlength=1 />')
        _write('</div>')

    _write('<p class="final">(4 2 4 5)</p>')

    _close()


if __name__ == '__main__':
    generate_puzzle()
