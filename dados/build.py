import json, os
OUT=os.path.dirname(os.path.abspath(__file__))
N=[];E=[]
def n(id,nome,tipo,lado,resumo,**kw): N.append(dict(id=id,nome=nome,tipo=tipo,lado=lado,resumo=resumo,**kw))
def e(de,para,status,descricao,data,fontes,desfecho=None):
    d=dict(de=de,para=para,status=status,descricao=descricao,data=data,fontes=fontes)
    if desfecho: d["desfecho"]=desfecho
    E.append(d)
# ---------- PARTIDOS ----------
for i,nm,l,r in [
 ("pt","PT – Partido dos Trabalhadores","esquerda","Partido de Lula, Dilma, Gleisi e Jaques Wagner."),
 ("pdt","PDT – Partido Democrático Trabalhista","esquerda","Centro-esquerda; partido de Carlos Lupi."),
 ("psb","PSB – Partido Socialista Brasileiro","esquerda","Centro-esquerda; partido atual de Geraldo Alckmin."),
 ("pl","PL – Partido Liberal","direita","Partido de Jair, Flávio e Eduardo Bolsonaro; presidido por Valdemar Costa Neto."),
 ("pp","PP – Progressistas","direita","Centro-direita; partido de Arthur Lira e Ciro Nogueira."),
 ("ptb","PTB – Partido Trabalhista Brasileiro","direita","Partido de Roberto Jefferson, Daniel Silveira e Collor na época dos casos; fundiu-se ao Patriota em 2023 (PRD)."),
 ("uniao","União Brasil","direita","Centro-direita; partido de Juscelino Filho e, na época do caso Marielle, de Chiquinho Brazão."),
 ("mdb","MDB – Movimento Democrático Brasileiro","centro","Partido de Temer, Cunha (na época), Geddel e Sérgio Cabral."),
 ("psdb","PSDB – Partido da Social Democracia Brasileira","centro","Centro / centro-direita; partido de Aécio, Serra, Azeredo e de Alckmin até 2021."),
]: n(i,nm,"partido",l,r)
# ---------- EMPRESAS ----------
n("odebrecht","Odebrecht (hoje Novonor)","empresa","n-a","Empreiteira central da Lava Jato; acordo de leniência em 2016. Em 2023 o STF anulou o uso das provas dos sistemas Drousys e MyWebDay em todas as ações.")
n("oas","OAS","empresa","n-a","Empreiteira citada nos casos do triplex e do sítio de Atibaia.")
n("jbs","JBS / J&F","empresa","n-a","Grupo dos irmãos Batista; delação de 2017 atingiu Temer e Aécio.")
n("banco-master","Banco Master","empresa","n-a","Banco de Daniel Vorcaro, liquidado pelo Banco Central em nov/2025; alvo da Operação Compliance Zero.")
n("utc","UTC Engenharia","empresa","n-a","Empreiteira envolvida nos contratos da BR Distribuidora (caso Collor).")
# ---------- PESSOAS ----------
P=[
("lula","Luiz Inácio Lula da Silva","esquerda","pt","Presidente da República (2003–2010 e desde 2023). Nenhuma condenação em vigor."),
("dirceu","José Dirceu","esquerda","pt","Ex-ministro da Casa Civil. Condenado no mensalão; condenações da Lava Jato anuladas em 2024."),
("genoino","José Genoino","esquerda","pt","Ex-presidente do PT, condenado no mensalão."),
("delubio","Delúbio Soares","esquerda","pt","Ex-tesoureiro do PT, condenado no mensalão."),
("palocci","Antonio Palocci","esquerda","pt","Ex-ministro da Fazenda; atos da Lava Jato contra ele anulados em 2025 (delação mantida)."),
("gleisi","Gleisi Hoffmann","esquerda","pt","Ex-presidente do PT; absolvida pelo STF na AP 1003 (2018)."),
("jaques-wagner","Jaques Wagner","esquerda","pt","Senador (PT-BA), líder do governo; alvo da 9ª fase da Compliance Zero (caso Master)."),
("lupi","Carlos Lupi","esquerda","pdt","Ex-ministro da Previdência (2023–2025); deixou o cargo após a operação sobre fraudes no INSS. Não é alvo da PF."),
("frei-chico","José Ferreira da Silva (Frei Chico)","esquerda",None,"Irmão de Lula; foi vice-presidente do Sindnapi, entidade investigada no caso INSS. Não é alvo da PF."),
("lulinha","Fábio Luís Lula da Silva (Lulinha)","esquerda",None,"Filho de Lula; citado na CPMI do INSS por pagamentos do 'Careca do INSS' a empresária próxima dele. Não é investigado pela PF."),
("alckmin","Geraldo Alckmin","centro","psb","Vice-presidente (PSB); na época dos fatos (2014) estava no PSDB."),
("bolsonaro","Jair Bolsonaro","direita","pl","Ex-presidente (2019–2022). Condenado em definitivo a 27 anos e 3 meses na trama golpista; prisão domiciliar desde 24/03/2026."),
("flavio","Flávio Bolsonaro","direita","pl","Senador (PL-RJ). Nenhuma condenação; investigado no inquérito 'Dark Horse' (2026)."),
("eduardo","Eduardo Bolsonaro","direita","pl","Ex-deputado federal (PL-SP), vive nos EUA; condenado por coação no curso do processo (2026)."),
("carlos","Carlos Bolsonaro","direita","pl","Vereador do Rio; investigado no caso Abin paralela (1ª instância)."),
("braga-netto","Walter Braga Netto","direita","pl","General da reserva, ex-ministro e candidato a vice em 2022; condenado a 26 anos na trama golpista."),
("heleno","Augusto Heleno","direita",None,"General da reserva, ex-ministro do GSI do governo Bolsonaro (sem filiação); condenado a 21 anos na trama golpista."),
("ramagem","Alexandre Ramagem","direita","pl","Ex-diretor da Abin e ex-deputado (PL-RJ); condenado a 16 anos e 1 mês na trama golpista; foragido."),
("mauro-cid","Mauro Cid","direita",None,"Tenente-coronel, ex-ajudante de ordens de Bolsonaro (sem filiação); delator da trama golpista."),
("valdemar","Valdemar Costa Neto","direita","pl","Presidente do PL; condenado no mensalão; investigação na trama golpista reaberta em 2025."),
("wassef","Frederick Wassef","direita",None,"Advogado da família Bolsonaro; investigado no caso das joias."),
("queiroz","Fabrício Queiroz","direita",None,"Ex-assessor de Flávio Bolsonaro na Alerj."),
("zambelli","Carla Zambelli","direita","pl","Ex-deputada federal (PL-SP); duas condenações no STF; está na Itália, onde corre o processo de extradição."),
("silveira","Daniel Silveira","direita","ptb","Ex-deputado federal (PTB-RJ na época); condenado pelo STF em 2022; indulto de Bolsonaro anulado em 2023."),
("jefferson","Roberto Jefferson","direita","ptb","Ex-deputado e ex-presidente do PTB; delator e condenado no mensalão; condenado de novo pelo STF em 2024."),
("collor","Fernando Collor","direita","ptb","Ex-presidente e ex-senador (PTB-AL na época); cumpre pena em prisão domiciliar desde 2025."),
("lira","Arthur Lira","direita","pp","Deputado (PP-AL), ex-presidente da Câmara (2021–2025)."),
("ciro-nogueira","Ciro Nogueira","direita","pp","Senador (PP-PI), ex-ministro da Casa Civil de Bolsonaro; alvo da Compliance Zero (caso Master)."),
("claudio-castro","Cláudio Castro","direita","pl","Ex-governador do RJ (PL); PF o aponta como líder do núcleo político do caso Rioprevidência/Master."),
("jose-carlos-oliveira","José Carlos Oliveira (Ahmed Mohamad Oliveira)","direita",None,"Ex-presidente do INSS e ex-ministro do Trabalho e Previdência do governo Bolsonaro; indiciado pela PF no caso INSS."),
("juscelino","Juscelino Filho","direita","uniao","Deputado (União-MA), ex-ministro das Comunicações de Lula; denunciado pela PGR em 2025."),
("chiquinho-brazao","Chiquinho Brazão","direita","uniao","Ex-deputado federal (expulso do União Brasil após a prisão); condenado como mandante do assassinato de Marielle Franco."),
("domingos-brazao","Domingos Brazão","n-a",None,"Ex-conselheiro do TCE-RJ, irmão de Chiquinho; condenado como mandante do assassinato de Marielle Franco."),
("temer","Michel Temer","centro","mdb","Ex-presidente (2016–2018); absolvido ou com ações trancadas nos principais casos."),
("cunha","Eduardo Cunha","centro","mdb","Ex-presidente da Câmara (MDB na época; hoje Republicanos); condenação da Lava Jato anulada em 2023."),
("geddel","Geddel Vieira Lima","centro","mdb","Ex-ministro; condenado pelo STF no caso do bunker de R$ 51 milhões; em liberdade condicional desde 2022."),
("cabral","Sérgio Cabral","centro","mdb","Ex-governador do RJ; dezenas de condenações, parte anulada; em liberdade desde 2022."),
("aecio","Aécio Neves","centro","psdb","Deputado federal (PSDB-MG); absolvido no caso JBS."),
("serra","José Serra","centro","psdb","Ex-senador e ex-governador de SP; ação penal da Lava Jato trancada em 2021."),
("azeredo","Eduardo Azeredo","centro","psdb","Ex-governador de MG; condenação no 'mensalão tucano' suspensa e enviada à Justiça Eleitoral em 2021."),
("marcos-valerio","Marcos Valério","n-a",None,"Publicitário, operador do mensalão; maior pena da AP 470."),
("marcelo-odebrecht","Marcelo Odebrecht","n-a",None,"Ex-presidente da Odebrecht; atos da Lava Jato contra ele anulados em 2024 (delação mantida)."),
("vorcaro","Daniel Vorcaro","n-a",None,"Dono do Banco Master; preso desde mar/2026 na Operação Compliance Zero."),
("careca-inss","Antônio Carlos Camilo Antunes ('Careca do INSS')","n-a",None,"Lobista apontado pela PF como principal operador das fraudes do INSS; preso."),
("stefanutto","Alessandro Stefanutto","n-a",None,"Servidor de carreira, ex-presidente do INSS no governo Lula; indiciado e preso preventivamente."),
]
for i,nm,l,p,r in P:
    kw={"partido":p} if p else {}
    n(i,nm,"pessoa",l,r,**kw)
# ---------- CASOS ----------
C=[
("c-trama-golpista","Trama golpista (AP 2668)","STF condenou o 'núcleo crucial' por tentativa de golpe de Estado após as eleições de 2022. Penas de 2 a 27 anos; trânsito em julgado em nov/2025. Revisão criminal de Bolsonaro pendente, prevista para depois do 2º turno de 2026."),
("c-coacao-eduardo","Coação no curso do processo (AP 2782)","Eduardo Bolsonaro articulou sanções dos EUA para pressionar o STF no julgamento do pai."),
("c-joias","Joias sauditas","Venda e recompra de joias dadas por Arábia Saudita e Bahrein ao governo. PF indiciou Bolsonaro e 11 em 2024; PGR pediu arquivamento em mar/2026; Moraes devolveu à PGR; sem decisão final."),
("c-vacina","Cartão de vacina falso","Inserção de dados falsos de vacinação de Covid no sistema do Ministério da Saúde. Arquivado para Bolsonaro em mar/2025 por falta de prova além da delação."),
("c-abin-paralela","Abin paralela","Uso da Abin para monitoramento ilegal no governo Bolsonaro. Em jul/2026 Moraes arquivou para Bolsonaro e Ramagem e enviou o restante à Justiça Federal do DF."),
("c-rachadinha","'Rachadinha' na Alerj","Suposto desvio de salários de assessores do gabinete de Flávio Bolsonaro. Denúncia rejeitada em mai/2022 depois que STJ e STF anularam provas."),
("c-dark-horse","Inquérito 'Dark Horse'","Apura financiamento por Vorcaro do filme sobre Bolsonaro; suspeita de lavagem, evasão de divisas e corrupção. PF pediu prorrogação em out/2026."),
("c-master","Caso Banco Master (Operação Compliance Zero)","Fraudes no Banco Master e na tentativa de venda ao BRB; fases atingiram políticos de diferentes partidos e o fundo Rioprevidência."),
("c-inss","Fraude do INSS (Operação Sem Desconto)","Descontos não autorizados em aposentadorias por associações (de 2019 em diante). PF indiciou 48 pessoas em jul/2026; PGR ainda não denunciou."),
("c-triplex","Triplex do Guarujá","Acusação de propina da OAS via triplex. Condenação anulada em 2021 (incompetência de Curitiba e suspeição de Moro); prescreveu no DF."),
("c-atibaia","Sítio de Atibaia","Reformas pagas por OAS e Odebrecht. Condenação anulada em 2021; prescrição reconhecida no DF."),
("c-instituto-lula","Instituto Lula (sede e doações)","Ações anuladas em 2021 com as demais da Lava Jato contra Lula e enviadas ao DF; encerradas."),
("c-lava-jato","Lava Jato / Petrolão (ações de Curitiba)","Desvios na Petrobras por cartel de empreiteiras e partidos. Desde 2021 o STF anulou muitas condenações por incompetência, parcialidade ou provas inválidas."),
("c-br-distribuidora","BR Distribuidora (AP 1025)","Propina de R$ 20 milhões em contratos da BR Distribuidora com a UTC. Collor condenado em 2023."),
("c-ap1003","AP 1003 (campanha de Gleisi em 2010)","Suposto R$ 1 milhão da Petrobras para campanha. Absolvição no STF em 2018."),
("c-mensalao","Mensalão (AP 470)","Compra de apoio no Congresso no 1º governo Lula. Julgado pelo STF em 2012."),
("c-mensalao-tucano","Mensalão tucano (MG)","Desvio de estatais mineiras para a campanha de 1998 de Azeredo."),
("c-jbs-aecio","Caso JBS – Aécio","R$ 2 milhões pedidos a Joesley Batista. Absolvição em 2022, mantida pelo TRF-3 em 2023."),
("c-quadrilhao-mdb","'Quadrilhão do MDB'","Denúncia por organização criminosa contra a cúpula do MDB. Absolvição sumária em 2021, mantida em 2023."),
("c-mala-jbs","Mala de R$ 500 mil (JBS)","Mala entregue a Rocha Loures. Ação contra Temer trancada; Fachin manteve encerrada em 2024."),
("c-bunker","Bunker de R$ 51 milhões","Dinheiro achado em apartamento em Salvador ligado a Geddel. Condenação por lavagem mantida."),
("c-cabral","Esquema Cabral (Calicute e desdobramentos)","Propinas no governo do RJ. Dezenas de condenações; 3 anuladas em mar/2024."),
("c-serra","Lavagem transnacional – Serra","Lava Jato SP. Ação trancada e provas anuladas por Gilmar Mendes em 2021."),
("c-alckmin","Caixa 2 da Odebrecht – Alckmin (2014)","Ação penal trancada em 2022; ação de improbidade arquivada em 2024, mantida pela 2ª Turma em 2025."),
("c-marielle","Assassinato de Marielle Franco e Anderson Gomes","STF condenou os mandantes em fev/2026; embargos rejeitados em jun/2026."),
("c-zambelli-cnj","Invasão dos sistemas do CNJ","Inserção de documentos falsos, como mandado de prisão contra Moraes, com o hacker Walter Delgatti."),
("c-zambelli-arma","Perseguição armada em SP (2022)","Zambelli perseguiu um homem com arma na véspera do 2º turno de 2022."),
("c-silveira","Ataques ao STF – Daniel Silveira (AP 1044)","Coação no curso do processo e ameaças ao STF."),
("c-jefferson","Incitação contra Poderes – Jefferson (AP 2493)","Incitação à violência contra a CPI da Covid e o TSE, calúnia e homofobia."),
("c-codevasf","Emendas da Codevasf – Juscelino Filho","Suposto desvio de emendas para pavimentação em Vitorino Freire (MA)."),
("c-lira-cbtu","Propina da CBTU – Lira (Inq 3515)","Suposta propina de R$ 106 mil. Denúncia rejeitada em 2023 a pedido da própria PGR."),
]
for i,nm,r in C: n(i,nm,"caso","n-a",r)

S=dict(
stf_golpe="https://noticias.stf.jus.br/postsnoticias/stf-fixa-penas-de-16-a-27-anos-para-condenados-por-tentativa-de-golpe-de-estado/",
stf_golpe8="https://noticias.stf.jus.br/postsnoticias/stf-condena-os-oito-reus-da-acao-por-golpe-de-estado/",
ab_exec="https://agenciabrasil.ebc.com.br/justica/noticia/2025-11/stf-determina-execucao-das-penas-de-bolsonaro-e-mais-reus-do-nucleo-1",
)
G=[S["stf_golpe"],S["stf_golpe8"],S["ab_exec"]]
# trama golpista
e("bolsonaro","c-trama-golpista","condenado","Condenado a 27 anos e 3 meses (1ª Turma, 4 a 1). Trânsito em julgado em 25/11/2025. Prisão domiciliar humanitária desde 24/03/2026, mantida sem prazo em jul/2026. Revisão criminal pendente.","2025-11-25",G+["https://g1.globo.com/politica/noticia/2026/03/24/moraes-autoriza-prisao-domiciliar-para-jair-bolsonaro.ghtml","https://agenciabrasil.ebc.com.br/justica/noticia/2026-10/stf-deve-julgar-revisao-da-condenacao-de-bolsonaro-apos-eleicoes"])
e("braga-netto","c-trama-golpista","condenado","Condenado a 26 anos.","2025-09-11",G)
e("heleno","c-trama-golpista","condenado","Condenado a 21 anos.","2025-09-11",G)
e("ramagem","c-trama-golpista","condenado","Condenado a 16 anos, 1 mês e 15 dias; segue foragido.","2025-09-11",G)
e("mauro-cid","c-trama-golpista","condenado","Delator; pena de 2 anos em regime aberto, cumprida desde nov/2025.","2025-09-11",["https://noticias.stf.jus.br/postsnoticias/confira-como-foram-calculadas-as-penas-no-julgamento-sobre-tentativa-de-golpe/","https://g1.globo.com/politica/noticia/2025/09/11/primeira-turma-do-stf-define-pena-de-2-anos-em-regime-para-cid-na-trama-golpista.ghtml"])
e("valdemar","c-trama-golpista","investigado","Indiciado pela PF, ficou fora da denúncia da PGR (fev/2025); a 1ª Turma reabriu a investigação contra ele em out/2025.","2025-10-21",["https://www1.folha.uol.com.br/poder/2025/02/valdemar-argentino-padre-e-4-coroneis-indiciados-pela-pf-ficam-fora-de-denuncia-da-pgr.shtml","https://g1.globo.com/politica/noticia/2025/10/21/stf-decide-reabrir-investigacao-de-valdemar-costa-neto-na-tentativa-de-golpe-de-estado.ghtml"])
# coação
CO=["https://noticias.stf.jus.br/postsnoticias/stf-condena-eduardo-bolsonaro-a-4-anos-e-2-meses-de-reclusao-por-tentar-interferir-no-processo-sobre-tentativa-de-golpe/","https://conjur.com.br/2026-set-19/stf-mantem-condenacao-de-eduardo-bolsonaro-por-coacao-no-curso-do-processo/","https://agenciabrasil.ebc.com.br/justica/noticia/2026-02/stf-formaliza-acao-que-tornou-eduardo-bolsonaro-reu-na-corte"]
e("eduardo","c-coacao-eduardo","condenado","Condenado por unanimidade a 4 anos e 2 meses em regime semiaberto (jun/2026); embargos rejeitados em 18/09/2026.","2026-09-18",CO)
e("bolsonaro","c-coacao-eduardo","investigado","Indiciado pela PF no mesmo inquérito, mas não incluído na denúncia da PGR.","2025-09",["https://cbn.globo.com/politica/noticia/2026/02/20/stf-abre-acao-penal-e-torna-eduardo-bolsonaro-reu-por-obstrucao-de-justica-e-coacao.ghtml"])
# joias
J=["https://g1.globo.com/politica/noticia/2026/03/05/pgr-pede-arquivamento-de-investigacao-sobre-joias-de-bolsonaro.ghtml","https://g1.globo.com/politica/noticia/2026/03/19/caso-das-joias-moraes-pede-que-pgr-analise-material-sobre-wassef-antes-de-avaliar-arquivamento.ghtml"]
e("bolsonaro","c-joias","investigado","Indiciado pela PF (jul/2024) por peculato, lavagem e associação criminosa. PGR pediu arquivamento em 05/03/2026; Moraes devolveu à PGR em 19/03/2026. Sem decisão final.","2026-03-19",J+["https://www.gp1.com.br/brasil/noticia/2026/9/21/moraes-determina-que-stf-envie-provas-do-caso-das-joias-sauditas-a-receita-federal-631964.html"])
e("mauro-cid","c-joias","investigado","Indiciado pela PF; vendeu nos EUA um Rolex do acervo.","2024-07",J)
e("wassef","c-joias","investigado","Indiciado pela PF; recomprou o Rolex nos EUA. Moraes pediu manifestação específica da PGR sobre ele.","2026-03-19",J)
# vacina
e("bolsonaro","c-vacina","arquivado","Indiciado pela PF em mar/2024; arquivado por Moraes a pedido da PGR em 28/03/2025 por falta de provas além da delação de Cid. Pode ser reaberto se surgirem provas novas.","2025-03-28",["https://noticias.stf.jus.br/postsnoticias/stf-arquiva-investigacao-contra-ex-presidente-da-republica-por-fraude-em-cartao-de-vacina/","https://agenciabrasil.ebc.com.br/justica/noticia/2025-03/cartao-de-vacina-moraes-arquiva-investigacao-contra-bolsonaro"])
e("mauro-cid","c-vacina","investigado","Indiciado pela PF; delator. A parte dos investigados sem foro foi enviada à Justiça Federal do DF.","2025-03-28",["https://noticias.stf.jus.br/postsnoticias/stf-arquiva-investigacao-contra-ex-presidente-da-republica-por-fraude-em-cartao-de-vacina/"])
# abin
A=["https://valor.globo.com/politica/noticia/2026/07/20/moraes-arquiva-inquerito-contra-bolsonaro-e-ramagem-no-caso-de-abin-paralela.ghtml","https://www.cnnbrasil.com.br/politica/investigacao-contra-carlos-e-antiga-cupula-da-abin-segue-na-1a-instancia/","https://g1.globo.com/politica/noticia/2026/06/18/abin-paralela-pgr-defende-que-investigacao-saia-do-stf-e-seja-transferida-para-a-primeira-instancia.ghtml"]
e("bolsonaro","c-abin-paralela","arquivado","Arquivado em 20/07/2026 por já ter sido condenado pelos fatos conexos na AP 2668.","2026-07-20",A)
e("ramagem","c-abin-paralela","arquivado","Arquivado em 20/07/2026 pelo mesmo motivo.","2026-07-20",A)
e("carlos","c-abin-paralela","investigado","Investigação segue na Justiça Federal do DF; sem denúncia.","2026-07-20",A)
# rachadinha
R=["https://g1.globo.com/rj/rio-de-janeiro/noticia/2022/05/16/tj-rj-rejeita-denuncia-contra-flavio-bolsonaro-no-caso-das-rachadinhas.ghtml","https://agenciabrasil.ebc.com.br/politica/noticia/2022-05/justica-do-rio-arquiva-processo-de-caso-de-supostas-rachadinhas"]
e("flavio","c-rachadinha","arquivado","Denunciado pelo MP-RJ em 2020. O TJ-RJ rejeitou a denúncia em 16/05/2022, a pedido do próprio MP, depois que as provas foram anuladas. Nova investigação não está proibida; em set/2026 houve pedido de reabertura, sem investigação instaurada.","2022-05-16",R)
e("queiroz","c-rachadinha","arquivado","Denunciado com Flávio em 2020; a denúncia foi rejeitada em 2022.","2022-05-16",R)
# dark horse
DH=["https://g1.globo.com/politica/noticia/2026/09/11/flavio-bolsonaro-e-investigado-em-inquerito-da-pf-aberto-para-apurar-financiamento-do-filme-dark-horse.ghtml","https://g1.globo.com/politica/noticia/2026/10/16/caso-dark-horse-pf-pede-a-andre-mendonca-prorrogacao-do-inquerito-por-90-dias.ghtml","https://g1.globo.com/politica/noticia/2026/10/17/dark-horse-pf-aponta-divergencia-severa-entre-recursos-enviados-ao-exterior-e-os-que-retornaram-ao-brasil-para-filme-sobre-bolsonaro.ghtml"]
e("flavio","c-dark-horse","investigado","Investigado no STF (relator André Mendonça); a PF pediu mais 90 dias em 16/10/2026.","2026-10-16",DH)
e("vorcaro","c-dark-horse","investigado","Apontado como financiador do filme.","2026-09-11",DH)
# master
M=["https://g1.globo.com/politica/noticia/2026/05/07/pf-faz-nova-operacao-caso-master.ghtml","https://g1.globo.com/politica/noticia/2026/05/07/caso-master-ciro-nogueira-teria-recebido-vantagens-indevidas-de-vorcaro-em-troca-de-apoio-diz-pf.ghtml"]
e("vorcaro","c-master","investigado","Preso desde mar/2026; nega fraude e pede revogação da prisão. Sem denúncia até agora.","2026-10-15",["https://g1.globo.com/df/distrito-federal/noticia/2026/10/15/pf-ouve-vorcaro-e-paulo-henrique-costa-ex-presidente-do-brb-em-inquerito-sobre-o-banco-master.ghtml","https://www.bbc.com/portuguese/articles/cp322yglvpjo"])
e("banco-master","c-master","investigado","Banco liquidado pelo Banco Central em nov/2025.","2025-11",["https://www.bbc.com/portuguese/articles/cp322yglvpjo"])
e("ciro-nogueira","c-master","investigado","Alvo da 5ª fase (07/05/2026). A PF suspeita de pagamentos mensais e de uma 'emenda Master' à PEC 65/2023. Ele nega.","2026-05-07",M+["https://www.bbc.com/portuguese/articles/clyp32n138po"])
e("jaques-wagner","c-master","investigado","Alvo da 9ª fase (18/06/2026) por supostos repasses, apartamento e atuação a favor do banco. Ele nega.","2026-06-18",["https://g1.globo.com/politica/noticia/2026/06/18/banco-master-9a-fase-da-operacao-compliance-zero.ghtml"])
e("claudio-castro","c-master","investigado","Relatório da PF (set/2026) o aponta, com Vorcaro, como líder do esquema que direcionou cerca de R$ 3,7 bi do Rioprevidência ao Master. Ele nega.","2026-09-12",["https://cbn.globo.com/politica/noticia/2026/09/12/pf-diz-que-castro-e-vorcaro-lideraram-organizacao-criminosa-para-direcionar-recursos-do-rioprevidencia-ao-master.ghtml","https://g1.globo.com/rj/rio-de-janeiro/noticia/2026/05/26/compliance-zero-investigacao-rioprevidencia.ghtml"])
# inss
I=["https://g1.globo.com/jornal-nacional/noticia/2026/07/14/fraude-do-inss-policia-federal-indicia-dois-ex-presidentes-do-instituto-e-mais-46-pessoas.ghtml"]
e("careca-inss","c-inss","investigado","Indiciado pela PF em jul/2026 e preso; PGR ainda decide se denuncia.","2026-07-14",I)
e("stefanutto","c-inss","investigado","Indiciado; segundo a PF, recebeu R$ 250 mil por mês em 2023–2024. Preso desde nov/2025; PGR opinou pela soltura com cautelares.","2026-07-14",I+["https://www.terra.com.br/noticias/brasil/politica/pgr-pede-revogacao-de-prisao-preventiva-de-stefanutto-processos-estao-parados-no-stf,772d4aab8ba5ed69f42c03ffaf6b7c2abr2xaw0j.html"])
e("jose-carlos-oliveira","c-inss","investigado","Ex-presidente do INSS e ex-ministro de Bolsonaro, indiciado pela PF.","2026-07-14",I)
e("lupi","c-inss","citado","Depôs à CPMI e negou envolvimento; não foi indiciado pela PF.","2025-09-08",["https://www12.senado.leg.br/noticias/materias/2025/09/08/carlos-lupi-nega-envolvimento-em-fraudes-no-inss-no-depoimento-a-cpmi"])
e("frei-chico","c-inss","citado","Ex-vice-presidente do Sindnapi, entidade investigada; não é alvo da PF. A CPMI rejeitou convocá-lo.","2025-10",["https://www.bbc.com/portuguese/articles/cj69rj80g00o"])
e("lulinha","c-inss","citado","Pagamentos de R$ 1,5 mi do 'Careca' a uma empresária próxima a ele; não é investigado pela PF.","2025-12-18",["https://www.bbc.com/portuguese/articles/cj69rj80g00o"])
# lula
L=["https://noticias.stf.jus.br/postsnoticias/stf-confirma-anulacao-de-condenacoes-do-ex-presidente-lula-na-lava-jato/","https://noticias.stf.jus.br/postsnoticias/plenario-fixa-competencia-da-justica-federal-do-df-para-julgar-processos-contra-ex-presidente-lula/"]
e("lula","c-triplex","anulado","Condenado por Moro (2017); STJ fixou 8 anos e 10 meses (2019). STF anulou em 2021 (HC 193726) e declarou Moro parcial; o caso prescreveu no DF.","2021-06-23",L+["https://noticias.stf.jus.br/postsnoticias/stf-confirma-suspeicao-de-sergio-moro-na-acao-do-triplex-do-guaruja/"])
e("oas","c-triplex","citado","Acusada de pagar a propina por meio do imóvel.","2017-07-12",L)
e("lula","c-atibaia","anulado","Condenado em 2ª instância a 17 anos e 1 mês; anulado em 2021; prescrição reconhecida no DF.","2021-04-15",L)
e("odebrecht","c-atibaia","citado","Acusada de pagar parte das reformas.","2019",L)
e("oas","c-atibaia","citado","Acusada de pagar parte das reformas.","2019",L)
e("lula","c-instituto-lula","anulado","Anulado em 2021 com as demais ações de Curitiba; encerrado depois no DF, sem ação ativa.","2021-04-15",L)
# lava jato
e("dirceu","c-lava-jato","anulado","Gilmar Mendes anulou os atos de Moro em 28/10/2024; o STJ declarou prescrição em 17/12/2024.","2024-12-17",["https://noticias.stf.jus.br/postsnoticias/stf-anula-atos-processuais-de-duas-acoes-penais-contra-jose-dirceu/","https://g1.globo.com/politica/noticia/2024/12/17/apos-decisao-de-gilmar-mendes-stj-encerra-duas-acoes-da-lava-jato-contra-jose-dirceu.ghtml"])
e("palocci","c-lava-jato","anulado","Toffoli anulou os atos em fev/2025; a 2ª Turma manteve por 3 a 2 em ago/2025. A delação continua válida.","2025-08-15",["https://g1.globo.com/politica/noticia/2025/02/19/toffoli-anula-processos-contra-ex-ministro-antonio-palocci-na-operacao-lava-jato.ghtml","https://g1.globo.com/politica/noticia/2025/08/15/stf-mantem-anulacao-de-atos-da-lava-jato-contra-palocci-por-3-a-2.ghtml"])
e("cunha","c-lava-jato","anulado","Condenação de quase 16 anos anulada em mai/2023 e enviada à Justiça Eleitoral; outras ações continuam na Justiça Eleitoral e na Justiça Federal.","2023-05-29",["https://g1.globo.com/politica/noticia/2023/05/29/stf-anula-condenacao-de-cunha-a-quase-16-anos-de-prisao-na-lava-jato.ghtml","https://noticias.stf.jus.br/postsnoticias/stf-mantem-tramitacao-de-acoes-penais-contra-ex-deputado-eduardo-cunha/"])
e("marcelo-odebrecht","c-lava-jato","anulado","Toffoli anulou os atos em mai/2024; a 2ª Turma manteve em set/2024. A delação continua válida.","2024-09",["https://noticias.stf.jus.br/postsnoticias/stf-mantem-nulidade-de-atos-da-lava-jato-contra-marcelo-odebrecht/","https://oglobo.globo.com/politica/noticia/2024/05/22/confira-perguntas-e-respostas-sobre-decisao-de-toffoli-que-favoreceu-marcelo-odebrecht.ghtml"])
e("odebrecht","c-lava-jato","anulado","Provas dos sistemas Drousys e MyWebDay, vindas da leniência, foram declaradas nulas pelo STF em todas as ações (2023).","2023-09-06",["https://noticias.stf.jus.br/postsnoticias/stf-anula-todas-as-provas-obtidas-em-sistemas-da-odebrecht-em-todas-as-esferas-e-para-todas-as-acoes/"])
# collor
e("collor","c-br-distribuidora","condenado","Condenado a 8 anos e 10 meses por corrupção passiva e lavagem (mai/2023). Pena em execução desde abr/2025, em domiciliar humanitária.","2025-04",["https://noticias.stf.jus.br/postsnoticias/stf-condena-collor-a-oito-anos-e-dez-meses-por-crimes-contra-br-distribuidora/","https://noticias.stf.jus.br/postsnoticias/stf-confirma-cumprimento-imediato-da-pena-do-ex-presidente-fernando-collor/","https://www1.folha.uol.com.br/poder/2026/05/collor-preso-ha-1-ano-vira-trunfo-para-bolsonaro-mas-e-deixado-de-lado-na-politica-de-alagoas.shtml"])
e("utc","c-br-distribuidora","citado","Contratos com a BR Distribuidora que originaram a propina.","2023-05-31",["https://noticias.stf.jus.br/postsnoticias/stf-condena-collor-a-oito-anos-e-dez-meses-por-crimes-contra-br-distribuidora/"])
# gleisi
e("gleisi","c-ap1003","arquivado","Ré no STF; absolvida pela 2ª Turma em 19/06/2018 de corrupção e lavagem.","2018-06-19",["https://noticias.stf.jus.br/postsnoticias/2a-turma-julga-improcedente-acao-penal-contra-senadora-gleisi-hoffmann/","https://g1.globo.com/politica/noticia/stf-absolve-senadora-gleisi-hoffmann-e-ex-ministro-paulo-bernardo-dos-crimes-de-corrupcao-e-lavagem.ghtml"],desfecho="absolvido")
# mensalão
MS=["https://g1.globo.com/politica/mensalao/noticia/2012/12/supremo-conclui-julgamento-do-mensalao-apos-quatro-meses-e-meio.html","https://noticias.stf.jus.br/postsnoticias/ap-470-stf-fixa-penas-do-nucleo-politico-e-inicia-analise-de-dosimetria-quanto-ao-nucleo-financeiro/"]
e("dirceu","c-mensalao","condenado","Condenado por corrupção ativa. Absolvido de formação de quadrilha em 2014; pena já extinta.","2012-12-17",MS+["https://www.camara.leg.br/tv/427795-stf-absolve-oito-condenados-do-mensalao-do-crime-de-formacao-de-quadrilha/"])
e("genoino","c-mensalao","condenado","Condenado por corrupção ativa; quadrilha afastada em 2014.","2012-12-17",MS)
e("delubio","c-mensalao","condenado","Condenado por corrupção ativa; quadrilha afastada em 2014.","2012-12-17",MS)
e("marcos-valerio","c-mensalao","condenado","Maior pena: 40 anos, 2 meses e 10 dias.","2012-12-17",MS)
e("valdemar","c-mensalao","condenado","Condenado por corrupção passiva e lavagem (então no PR, atual PL).","2012-12-17",MS)
e("jefferson","c-mensalao","condenado","Delator do esquema; condenado por corrupção passiva e lavagem.","2012-12-17",MS)
e("azeredo","c-mensalao-tucano","anulado","Condenado a 15 anos e 7 meses (pena fixada pelo STJ); o STF suspendeu a condenação em jun/2021 e mandou o caso à Justiça Eleitoral de MG.","2021-06-29",["https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias/STJ-confirma-condenacao-de-Eduardo-Azeredo-e-redimensiona-pena-para-15-anos-e-sete-meses.aspx","https://www1.folha.uol.com.br/poder/2021/06/supremo-suspende-condenacao-de-ex-governador-eduardo-azeredo-no-mensalao-do-psdb.shtml"])
# aécio
e("aecio","c-jbs-aecio","arquivado","Absolvido em 1ª instância (2022); o TRF-3 manteve por unanimidade em 27/07/2023.","2023-07-27",["https://g1.globo.com/sp/sao-paulo/noticia/2023/07/27/justica-mantem-absolvicao-de-aecio-neves-da-acusacao-de-corrupcao-passiva.ghtml","https://www1.folha.uol.com.br/poder/2023/07/justica-mantem-absolvicao-de-aecio-em-acusacao-de-corrupcao-no-caso-jbs.shtml"],desfecho="absolvido")
e("jbs","c-jbs-aecio","citado","Joesley Batista fez a gravação e a delação que originaram o caso.","2017",["https://oglobo.globo.com/politica/noticia/2023/07/27/aecio-neves-e-absolvido-pelo-trf-3-de-corrupcao-passiva-em-caso-envolvendo-acusacao-de-joesley-batista.ghtml"])
QM=["https://www1.folha.uol.com.br/colunas/monicabergamo/2023/03/justica-mantem-absolvicao-de-cunha-temer-geddel-e-yunes-no-caso-quadrilhao-do-mdb.shtml","https://oglobo.globo.com/politica/juiz-federal-absolve-temer-ex-deputados-no-quadrilhao-do-mdb-25004931"]
for p in ["temer","cunha","geddel"]:
    e(p,"c-quadrilhao-mdb","arquivado","Absolvição sumária em 2021, mantida pelo TRF-1 em mar/2023.","2023-03-07",QM,desfecho="absolvido")
e("temer","c-mala-jbs","arquivado","Ação trancada por falta de provas (2021); Fachin manteve encerrada em 08/05/2024.","2024-05-08",["https://g1.globo.com/politica/noticia/2024/05/08/fachin-mantem-encerrada-investigacao-de-temer-no-caso-da-mala-de-r-500-mil.ghtml"],desfecho="trancado")
e("jbs","c-mala-jbs","citado","Origem da mala, segundo a delação da J&F.","2017",["https://g1.globo.com/politica/noticia/2024/05/08/fachin-mantem-encerrada-investigacao-de-temer-no-caso-da-mala-de-r-500-mil.ghtml"])
e("geddel","c-bunker","condenado","Condenado pelo STF (2019); em 2021 a 2ª Turma afastou associação criminosa e manteve lavagem (13 anos e 4 meses). Em liberdade condicional desde 2022.","2021-08-23",["https://g1.globo.com/politica/noticia/2021/08/23/segunda-turma-do-stf-derruba-condenacao-de-geddel-vieira-lima-e-irmao-por-associacao-criminosa.ghtml","https://noticias.stf.jus.br/postsnoticias/fachin-defere-liberdade-condicional-ao-ex-ministro-geddel-vieira-lima/"])
e("cabral","c-cabral","condenado","Três condenações anuladas em mar/2024; restavam 18 em vigor na época. Em liberdade desde 2022; ações enviadas ao STJ em 2025.","2024-03-06",["https://www1.folha.uol.com.br/poder/2024/03/justica-anula-3-condenacoes-de-cabral-e-reduz-em-10-soma-de-suas-penas.shtml","https://www1.folha.uol.com.br/poder/2025/05/acoes-contra-cabral-sao-enviadas-ao-stj-apos-decisao-do-stf-sobre-foro-especial.shtml"])
e("serra","c-serra","anulado","Gilmar Mendes trancou a ação e anulou buscas e quebras de sigilo em 25/08/2021.","2021-08-25",["https://www.cnnbrasil.com.br/politica/gilmar-tranca-acao-contra-jose-serra-por-lavagem-de-dinheiro-transnacional/","https://valor.globo.com/politica/noticia/2021/08/26/gilmar-manda-trancar-acao-penal-contra-serra-movida-pela-lava-jato.ghtml"])
e("alckmin","c-alckmin","arquivado","Ação penal trancada (2022) e improbidade arquivada (out/2024), por nulidade das provas da Odebrecht; a 2ª Turma manteve em ago/2025.","2025-08-10",["https://conjur.com.br/2025-ago-10/stf-nega-recurso-e-mantem-arquivamento-de-acao-de-improbidade-contra-alckmin/","https://g1.globo.com/politica/noticia/2024/10/21/toffoli-manda-arquivar-acao-de-improbidade-administrativa-contra-geraldo-alckmin.ghtml"])
e("odebrecht","c-alckmin","citado","Apontada como origem do caixa 2.","2024-10-21",["https://g1.globo.com/politica/noticia/2024/10/21/toffoli-manda-arquivar-acao-de-improbidade-administrativa-contra-geraldo-alckmin.ghtml"])
MA=["https://noticias.stf.jus.br/postsnoticias/stf-condena-irmaos-brazao-a-76-anos-de-prisao-pelo-assassinato-de-marielle-franco-e-anderson-gomes/","https://noticias.stf.jus.br/postsnoticias/stf-rejeita-recursos-e-mantem-condenacoes-por-assassinato-de-marielle-franco-e-anderson-gomes/","https://g1.globo.com/politica/noticia/2026/02/25/stf-condenacao-marielle.ghtml"]
e("chiquinho-brazao","c-marielle","condenado","Condenado por unanimidade a 76 anos e 3 meses como mandante; embargos rejeitados em jun/2026.","2026-02-25",MA)
e("domingos-brazao","c-marielle","condenado","Condenado por unanimidade a 76 anos e 3 meses como mandante; embargos rejeitados em jun/2026.","2026-02-25",MA)
e("zambelli","c-zambelli-cnj","condenado","Condenada a 10 anos pela 1ª Turma, por unanimidade. Em mai/2026 a Cassação italiana recusou a extradição nesse caso.","2025-05-14",["https://noticias.stf.jus.br/postsnoticias/por-unanimidade-stf-condena-deputada-carla-zambelli-e-hacker-walter-delgatti/","https://g1.globo.com/politica/noticia/2026/10/10/justica-italiana-marca-para-o-fim-de-outubro-novo-julgamento-sobre-extradicao-de-zambelli.ghtml"])
e("zambelli","c-zambelli-arma","condenado","Condenada a 5 anos e 3 meses (9 a 2); trânsito em julgado em 30/10/2025. A Itália reanalisa a extradição em 29/10/2026.","2025-10-30",["https://noticias.stf.jus.br/postsnoticias/deputada-carla-zambelli-e-condenada-pelo-stf-por-porte-ilegal-de-arma-de-fogo-e-constrangimento-ilegal/","https://g1.globo.com/politica/noticia/2025/10/30/carla-zambelli-transito-em-julgado-uso-de-arma.ghtml","https://g1.globo.com/politica/noticia/2026/10/10/justica-italiana-marca-para-o-fim-de-outubro-novo-julgamento-sobre-extradicao-de-zambelli.ghtml"])
e("silveira","c-silveira","condenado","Condenado a 8 anos e 9 meses (10 a 1) em 20/04/2022; o indulto de Bolsonaro foi anulado em 2023. Hoje cumpre a pena em regime aberto.","2022-04-20",["https://noticias.stf.jus.br/postsnoticias/stf-condena-daniel-silveira-a-oito-anos-e-nove-meses-de-prisao/","https://g1.globo.com/politica/noticia/2022/04/20/julgamento-stf-daniel-silveira.ghtml"])
e("jefferson","c-jefferson","condenado","Condenado a 9 anos, 1 mês e 5 dias pelo Plenário (dez/2024); pena em execução.","2024-12-13",["https://noticias.stf.jus.br/postsnoticias/stf-condena-roberto-jefferson-por-atentar-contra-exercicio-dos-poderes/","https://noticias.stf.jus.br/postsnoticias/stf-determina-inicio-do-cumprimento-da-pena-imposta-a-ex-deputado-roberto-jefferson/"])
e("juscelino","c-codevasf","denunciado","Denunciado pela PGR ao STF em 08/04/2025 por corrupção, quando era deputado. Deixou o ministério. Prazos suspensos por Dino em mai/2025; não há registro de que a denúncia já tenha sido recebida.","2025-04-08",["https://g1.globo.com/politica/noticia/2025/04/08/pgr-denuncia-ao-stf-ministro-das-comunicacoes-juscelino-filho-por-suposta-corrupcao-em-emendas-quando-era-deputado.ghtml","https://noticias.uol.com.br/colunas/aguirre-talento/2025/05/13/dino-suspende-denuncia-da-pgr-contra-juscelino-filho-por-estar-ilegivel.htm"])
e("lira","c-lira-cbtu","arquivado","A 1ª Turma rejeitou a denúncia por unanimidade em 06/06/2023, a pedido da PGR, por falta de prova além das delações.","2023-06-06",["https://noticias.stf.jus.br/postsnoticias/1a-turma-rejeita-denuncia-contra-arthur-lira-por-corrupcao-passiva/","https://g1.globo.com/politica/noticia/2023/06/06/turma-do-stf-forma-maioria-para-arquivar-investigacao-contra-lira.ghtml"])

# validate
ids={x["id"] for x in N}; assert len(ids)==len(N)
ST={"citado","investigado","denunciado","reu","condenado","arquivado","anulado"}
for x in E:
    assert x["de"] in ids and x["para"] in ids, x
    assert x["status"] in ST and x["fontes"]
for x in N:
    if x.get("partido"): assert x["partido"] in ids
used={x["de"] for x in E}|{x["para"] for x in E}
orph=[x["id"] for x in N if x["id"] not in used and x["tipo"]!="partido"]
assert not orph, orph
meta=dict(titulo="Mapa de casos: políticos, partidos, empresas e processos",atualizado_em="2026-10-17",
 notas=["status = situação atual da pessoa ou empresa em cada caso. Citado não é investigado, e investigado não é réu.",
        "Absolvições e trancamentos aparecem como 'arquivado', com o campo 'desfecho' explicando.",
        "'lado' das pessoas segue o partido ou o campo político na época do caso. Casos têm lado 'n-a'.",
        "A filiação partidária está no campo 'partido' do nó da pessoa, não como aresta."])
json.dump(dict(meta=meta,nodes=N,edges=E),open(os.path.join(OUT,"dados.json"),"w"),ensure_ascii=False,indent=2)
# md
name={x["id"]:x["nome"] for x in N}; lado={x["id"]:x["lado"] for x in N}
md=["# Mapa de casos: dados","",f"Atualizado em 17/10/2026. {len(N)} nós e {len(E)} ligações.",""]+["- "+s for s in meta["notas"]]
from collections import Counter
md+=["","## Resumo","","| Status | Ligações |","|---|---|"]+[f"| {k} | {v} |" for k,v in sorted(Counter(x['status'] for x in E).items())]
md+=["","| Lado (pessoas) | Pessoas |","|---|---|"]+[f"| {k} | {v} |" for k,v in sorted(Counter(x['lado'] for x in N if x['tipo']=='pessoa').items())]
md+=["","## Ligações (pessoa/empresa → caso)","","| Quem | Lado | Caso | Status | Data | O que houve | Fontes |","|---|---|---|---|---|---|---|"]
for x in sorted(E,key=lambda x:(x["para"],x["de"])):
    st=x["status"]+(f" ({x['desfecho']})" if x.get("desfecho") else "")
    f=" ".join(f"[{i+1}]({u})" for i,u in enumerate(x["fontes"]))
    md.append(f"| {name[x['de']]} | {lado[x['de']]} | {name[x['para']]} | {st} | {x['data']} | {x['descricao'].replace('|','/')} | {f} |")
for t,ttl in [("caso","Casos"),("pessoa","Pessoas"),("partido","Partidos"),("empresa","Empresas")]:
    md+=["",f"## {ttl}","","| id | Nome | Lado | Partido | Resumo |","|---|---|---|---|---|"]
    for x in N:
        if x["tipo"]==t: md.append(f"| {x['id']} | {x['nome']} | {x['lado']} | {x.get('partido','')} | {x['resumo']} |")
open(os.path.join(OUT,"dados.md"),"w").write("\n".join(md)+"\n")
print(len(N),Counter(x['tipo'] for x in N),len(E),Counter(x['status'] for x in E),Counter(x['lado'] for x in N if x['tipo']=='pessoa'))
