#!/bin/sh
# Regera o site: junta os dados, gera index.html (página principal) e mapa.html (mapa em rede)
python3 merge.py && python3 - <<'PY'
d=open('mapa-data.js').read()
t=open('template-index.html').read().replace('/*DATA*/',d);open('index.html','w').write(t)
t=open('template-mapa.html').read().replace('/*VIS*/',open('vis.js').read()).replace('/*DATA*/',d);open('mapa.html','w').write(t)
PY
