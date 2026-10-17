#!/bin/sh
# Regera o site: junta os dados e embute tudo em index.html
python3 merge.py && python3 -c "t=open('template.html').read();t=t.replace('/*VIS*/',open('vis.js').read()).replace('/*DATA*/',open('mapa-data.js').read());open('index.html','w').write(t)"
