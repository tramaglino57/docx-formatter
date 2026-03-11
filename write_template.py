html = """<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<title>SLS Formatter</title>
<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:sans-serif}
body{background:#f3f4f6;min-height:100vh}
.hd{background:#fff;padding:14px 28px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid #e5e7eb}
.mn{max-width:800px;margin:40px auto;padding:0 20px}
.cd{background:#fff;border-radius:20px;box-shadow:0 2px 12px rgba(0,0,0,.06);padding:36px;margin-bottom:24px}
.cd h2{font-size:22px;font-weight:700;margin-bottom:8px}
.sb{color:#6b7280;font-size:14px;margin-bottom:24px}
.ua{border:3px dashed #d1d5db;border-radius:16px;padding:48px 24px;text-align:center;cursor:pointer;background:#fafafa}
.ua:hover{border-color:#a855f7}
.fi{display:none}
.fs{display:none;align-items:center;gap:12px;background:#f0fdf4;border:2px solid #86efac;border-radius:12px;padding:14px 18px;margin-top:16px}
.bt{padding:14px 28px;border-radius:12px;font-weight:600;font-size:15px;cursor:pointer;border:none;text-decoration:none;display:inline-flex;align-items:center;gap:8px}
.bp{background:linear-gradient(135deg,#c084fc,#9333ea);color:#fff}
.bp[disabled]{opacity:.5}
.bw{background:#fff;border:2px solid #e5e7eb;color:#374151}
.bg{background:linear-gradient(135deg,#34d399,#10b981);color:#fff}
.br{display:flex;gap:12px;margin-top:24px}
.rp{background:#1e1b2e;color:#e2e8f0;border-radius:14px;padding:20px;font-family:monospace;font-size:12px;line-height:1.7;white-space:pre-wrap;margin-top:20px;max-height:400px;overflow-y:auto}
.fl{padding:14px 20px;border-radius:12px;margin-bottom:20px;font-weight:600;background:#fef2f2;border-left:4px solid #dc2626;color:#991b1b}
.ft{text-align:center;padding:24px;font-size:11px;color:#9ca3af}
</style>
</head>
<body>
<div class="hd"><div><div style="font-size:17px;font-weight:700">SLS Studio Legale</div><div style="font-size:12px;color:#9ca3af">Document Formatter</div></div><a href="/" class="bw" style="padding:8px 16px;font-size:13px">Ricomincia</a></div>
<div class="mn">
{% with messages = get_flashed_messages(with_categories=true) %}{% if messages %}{% for category, message in messages %}<div class="fl">{{ message }}</div>{% endfor %}{% endif %}{% endwith %}
{% if step == 1 %}
<div class="cd"><h2>Formatta il tuo Atto</h2><p class="sb">Carica un file .docx e verra formattato secondo il modello dello studio.</p>
<form action="/format" method="post" enctype="multipart/form-data">
<div class="ua" onclick="document.getElementById('df').click()">
<div style="font-size:48px;margin-bottom:12px">&#x1F4C4;</div>
<div style="font-size:15px;font-weight:600">Clicca qui per selezionare il documento</div>
<div style="font-size:13px;color:#9ca3af;margin-top:6px">Solo file .docx</div>
<input type="file" name="document" id="df" accept=".docx" class="fi" onchange="document.getElementById('fn').textContent=this.files[0].name;document.getElementById('fsi').style.display='flex';document.getElementById('sbt').disabled=false"/>
</div>
<div id="fsi" class="fs"><span>&#x1F4CE;</span><span id="fn"></span></div>
<div class="br"><button type="submit" id="sbt" class="bt bp" disabled>Formatta Documento</button></div>
</form></div>
{% elif step == 2 %}
<div class="cd" style="text-align:center">
<div style="font-size:64px;margin-bottom:16px">&#x1F389;</div>
<h2>Documento Formattato</h2>
<p class="sb">{{ output_name }} - {{ total }} paragrafi{% if used_ai %} (AI){% else %} (regole){% endif %}</p>
{% if report %}<div class="rp" style="text-align:left">{{ report }}</div>{% endif %}
<div class="br" style="justify-content:center;margin-top:28px"><a href="/download" class="bt bg" style="font-size:16px;padding:16px 36px">Scarica Documento</a></div>
<div class="br" style="justify-content:center"><a href="/" class="bt bw">Formatta un altro</a></div>
</div>
{% endif %}
</div>
<div class="ft">VERSION 2.0.0 - SLS TECH</div>
</body>
</html>"""

with open("templates/index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("OK SALVATO")

