# Junta dados/dados.json (King Bot) com os dados originais do mapa (data.js antigo, salvo em /tmp/mine.json -> dados/original.json)
import json
kb=json.load(open('dados/dados.json')); m=json.load(open('dados/original.json'))
idmap={'c_trama':'c-trama-golpista','c_coacao':'c-coacao-eduardo','c_abin':'c-abin-paralela','c_joias':'c-joias','c_vacina':'c-vacina','c_cnj':'c-zambelli-cnj','c_inss':'c-inss','c_codevasf':'c-codevasf','c_master':'c-master',
 'cid':'mauro-cid','castro':'claudio-castro','joseoliv':'jose-carlos-oliveira','ciro':'ciro-nogueira','wagner':'jaques-wagner','freichico':'frei-chico','careca':'careca-inss'}
LADO={'dir':'direita','cen':'centro','esq':'esquerda','jud':'judiciario','emp':'n-a'}
ST={'cond':'condenado','den':'denunciado','ind':'indiciado','inv':'investigado','cit':'citado','arq':'arquivado'}
mp=lambda i:idmap.get(i,i)
nodes={n['id']:n for n in kb['nodes']}
for c in m['CASES']:
  if mp(c[0]) not in nodes: nodes[mp(c[0])]={'id':mp(c[0]),'nome':c[1],'tipo':'caso','lado':'n-a','resumo':c[2]}
for p in m['PEOPLE']:
  i=mp(p[0])
  if i not in nodes: nodes[i]={'id':i,'nome':p[1],'tipo':'pessoa','lado':LADO[p[2]],'resumo':p[3]}
pairs={(e['de'],e['para']) for e in kb['edges']}
edges=list(kb['edges'])
for l in m['LINKS']:
  if not l[3]: continue
  k=(mp(l[0]),mp(l[1]))
  if k in pairs: continue
  s=m['SRC'].get(l[4]); edges.append({'de':k[0],'para':k[1],'status':ST[l[2]],'descricao':l[3],'fontes':[s[1]] if s else []})
  pairs.add(k)
ties=[{'de':mp(t[0]),'para':mp(t[1]),'rotulo':t[2]} for t in m['TIES']]
out={'meta':kb['meta'],'nodes':list(nodes.values()),'edges':edges,'ligacoes':ties}
bad=[e for e in edges+ties if e['de'] not in nodes or e['para'] not in nodes]
assert not bad, bad
open('mapa-data.js','w').write('const D='+json.dumps(out,ensure_ascii=False)+';')
import collections as C
print(len(out['nodes']),C.Counter(n['tipo'] for n in out['nodes']),len(edges),len(ties))
