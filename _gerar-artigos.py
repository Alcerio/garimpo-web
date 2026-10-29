# Gera as páginas de artigo (guias) do site a partir de ARTIGOS + o índice guias.html + sitemap.xml.
# Rodar: python _gerar-artigos.py  (dentro de garimpo-afiliado-web). Editar o texto AQUI, não no HTML.
import html, json

BASE = 'https://alcerio.github.io/garimpo-web/'
LOJA = 'https://chromewebstore.google.com/detail/garimpo-do-afiliado/eiaeaofjdpnmkjfocpcmpcedamlhofhn'
DATA = '2026-10-28'

ARTIGOS = [
  {
    'slug': 'como-escolher-produto-para-divulgar-shopee',
    'titulo': 'Como escolher produto para divulgar como afiliado Shopee',
    'desc': 'Os 4 sinais que mostram se um produto da Shopee vale a pena divulgar: comissão, desconto real, vendas e avaliação. Guia prático para afiliados.',
    'corpo': '''
<p>Escolher o produto certo é metade do trabalho de um afiliado Shopee. Um vídeo bom de um produto ruim não vende. Um vídeo simples de um produto certo, vende. A boa notícia é que dá para saber se um produto tem chance antes de gravar qualquer coisa.</p>

<h2>Os 4 sinais de um produto que vale divulgar</h2>

<h3>1. Comissão que compensa</h3>
<p>A comissão é uma porcentagem do preço, e essa porcentagem muda conforme a categoria. Beleza e moda costumam pagar mais. Celulares e eletrônicos costumam pagar bem menos. Um produto de R$ 30 com 20% rende R$ 6 por venda. Um fone de R$ 80 com 8% rende R$ 6,40. Faça a conta antes: a <a href="calculadora-comissao-shopee.html">calculadora de comissão</a> faz isso em segundos.</p>

<h3>2. Desconto de verdade</h3>
<p>Desconto é o que faz a pessoa clicar no seu link agora, e não depois. Mas desconfie de "80% OFF" em produto que nunca custou o preço riscado. Desconto real de 30% a 60% sobre um preço plausível convence mais que um desconto exagerado.</p>

<h3>3. Muitas vendas</h3>
<p>Produto que já vende muito tem preço testado, vendedor que entrega e fotos que funcionam. "Mil vendidos" ou mais é um bom sinal. Produto com 3 vendas pode ser uma aposta, mas é uma aposta.</p>

<h3>4. Boa avaliação</h3>
<p>Nota abaixo de 4,5 com muitas avaliações costuma significar reclamação de qualidade ou de entrega. Isso gera cancelamento, e pedido cancelado não paga comissão. Leia as avaliações com foto antes de divulgar.</p>

<h2>O produto ideal junta os quatro</h2>
<p>Comissão alta com nota ruim dá cancelamento. Desconto bom com poucas vendas é incerto. O produto que mais rende é o que é bom nos quatro ao mesmo tempo, e é aí que se perde tempo: conferir tudo isso produto por produto, no olho, cansa.</p>

<h2>Como fazer isso em segundos</h2>
<p>A extensão <a href="./">Garimpo do Afiliado</a> faz essa conta sozinha. Ela cruza comissão estimada, desconto, vendas e avaliação e mostra uma nota de 0 a 100 no canto da página do produto. Verde é "vale divulgar", amarelo é "razoável", vermelho é "evite". Numa busca, ela dá nota para cada produto da lista e ranqueia os 10 melhores.</p>
''',
  },
  {
    'slug': 'comissao-afiliado-shopee-por-categoria',
    'titulo': 'Comissão de afiliado Shopee por categoria: quanto cada uma paga',
    'desc': 'Tabela com a comissão estimada de afiliado Shopee por categoria: beleza, moda, casa, eletrônicos e mais. Veja quais categorias pagam mais.',
    'corpo': '''
<p>Na Shopee, a comissão do afiliado é uma porcentagem do valor do produto, e essa porcentagem depende principalmente da categoria. Por isso, dois produtos com o mesmo preço podem render valores bem diferentes para você.</p>

<h2>Tabela de comissão estimada por categoria</h2>
<table>
<thead><tr><th>Categoria</th><th>Comissão estimada</th></tr></thead>
<tbody>
<tr><td>Beleza e maquiagem</td><td>~20%</td></tr>
<tr><td>Cuidados pessoais e higiene</td><td>~18%</td></tr>
<tr><td>Moda feminina e masculina</td><td>~18%</td></tr>
<tr><td>Bolsas, mochilas e acessórios de moda</td><td>~16%</td></tr>
<tr><td>Calçados</td><td>~15%</td></tr>
<tr><td>Saúde e suplementos</td><td>~15%</td></tr>
<tr><td>Casa, decoração e cozinha</td><td>~14%</td></tr>
<tr><td>Bebês e maternidade</td><td>~13%</td></tr>
<tr><td>Brinquedos, papelaria, esporte e pet</td><td>~12%</td></tr>
<tr><td>Automotivo, ferramentas e jardim</td><td>~10%</td></tr>
<tr><td>Mercado e áudio</td><td>~8%</td></tr>
<tr><td>Eletrônicos e games</td><td>~6%</td></tr>
<tr><td>Celulares e informática</td><td>~5%</td></tr>
</tbody>
</table>
<p class="nota">Estimativas de faixas públicas (2026), não são valores oficiais. A comissão real muda por produto, campanha e vendedor. Confirme sempre no seu painel do Programa de Afiliados Shopee.</p>

<h2>O que essa tabela ensina</h2>
<h3>Categoria barata pode pagar mais que categoria cara</h3>
<p>Um batom de R$ 35 a 20% rende R$ 7. Um carregador de R$ 60 a 5% rende R$ 3. O produto mais barato paga mais que o dobro, e ainda costuma vender mais fácil.</p>

<h3>Eletrônico só compensa com volume ou preço alto</h3>
<p>Com 5% a 6%, eletrônico precisa ser caro ou vender muito para valer o seu tempo. Não é proibido divulgar, mas faça a conta antes.</p>

<h3>Beleza e moda são o arroz com feijão do afiliado</h3>
<p>Pagam bem, vendem por impulso e rendem vídeo fácil. Não é à toa que a maioria dos perfis de achadinhos vive dessas categorias.</p>

<h2>Calcule o seu caso</h2>
<p>Use a <a href="calculadora-comissao-shopee.html">calculadora de comissão de afiliado Shopee</a>: informe o preço e a categoria e veja quanto rende por venda e por mês. Se você já sabe a sua porcentagem, dá para editar.</p>
''',
  },
  {
    'slug': 'achadinhos-que-vendem-shopee',
    'titulo': 'Achadinhos que vendem: como saber antes de postar',
    'desc': 'Como descobrir se um achadinho da Shopee vai vender antes de gravar o vídeo: sinais de produto que vende e sinais de produto que só dá trabalho.',
    'corpo': '''
<p>Todo perfil de achadinhos já passou por isso: o vídeo teve visualização, mas ninguém comprou. Quase sempre o problema não foi o vídeo, foi o produto. Dá para filtrar boa parte desses erros antes de postar.</p>

<h2>Sinais de achadinho que vende</h2>
<ul>
<li><b>Resolve um problema na hora:</b> organizador, escova que tira pelo, suporte de celular. A pessoa entende em 3 segundos para que serve.</li>
<li><b>Preço de impulso:</b> até uns R$ 50 a pessoa compra sem pensar muito. Acima disso ela pesquisa, compara e às vezes desiste.</li>
<li><b>Já vende muito:</b> milhares de vendidos mostram que o produto agrada e que o vendedor entrega.</li>
<li><b>Desconto real:</b> um preço riscado plausível com 30% a 60% de desconto dá urgência.</li>
<li><b>Nota alta com muitas avaliações:</b> 4,7 com 2 mil avaliações vale mais que 5,0 com 4.</li>
</ul>

<h2>Sinais de achadinho que só dá trabalho</h2>
<ul>
<li><b>Comissão baixa:</b> eletrônico barato a 5% rende centavos por venda.</li>
<li><b>Avaliações com foto reclamando:</b> "veio diferente", "quebrou no primeiro uso". Isso vira cancelamento, e cancelamento não paga comissão.</li>
<li><b>Desconto "mágico":</b> 90% OFF sobre um preço que ninguém nunca pagou. O público já desconfia.</li>
<li><b>Produto que precisa de explicação longa:</b> se você precisa de 30 segundos para explicar, o vídeo curto não dá conta.</li>
</ul>

<h2>Faça a triagem antes de gravar</h2>
<p>Antes de gravar, abra o produto e confira comissão, desconto, vendas e nota. Se dois desses estiverem ruins, pule. Parece pouco, mas evita que você grave 10 vídeos para 1 vender.</p>
<p>A extensão <a href="./">Garimpo do Afiliado</a> faz essa triagem por você: cada produto da Shopee ganha uma nota de 0 a 100, e numa busca ela mostra o Top 10 dos achadinhos com mais chance de vender. É grátis para começar.</p>
''',
  },
  {
    'slug': 'quanto-ganha-afiliado-shopee',
    'titulo': 'Quanto ganha um afiliado Shopee? Faça as contas',
    'desc': 'Quanto dá para ganhar como afiliado Shopee: a conta de comissão por venda, quantas vendas são precisas para R$ 500 ou R$ 1.000 e o que muda o resultado.',
    'corpo': '''
<p>Não existe um salário de afiliado Shopee. O ganho depende de duas coisas: quanto você ganha por venda e quantas vendas faz. Dá para fazer essa conta antes de começar e ter uma meta realista.</p>

<h2>A conta básica</h2>
<p style="font-size:18px"><b>ganho no mês = preço × comissão × número de vendas</b></p>
<p>Exemplo: produtos de R$ 40 em média, com 15% de comissão, rendem R$ 6 por venda. Com 100 vendas no mês, são R$ 600.</p>

<h2>Quantas vendas você precisa</h2>
<table>
<thead><tr><th>Ganho por venda</th><th>Para R$ 500/mês</th><th>Para R$ 1.000/mês</th></tr></thead>
<tbody>
<tr><td>R$ 2</td><td>250 vendas</td><td>500 vendas</td></tr>
<tr><td>R$ 4</td><td>125 vendas</td><td>250 vendas</td></tr>
<tr><td>R$ 6</td><td>84 vendas</td><td>167 vendas</td></tr>
<tr><td>R$ 10</td><td>50 vendas</td><td>100 vendas</td></tr>
</tbody>
</table>
<p>Repare: sair de R$ 2 para R$ 6 por venda corta pela metade (e mais) o número de vendas de que você precisa. Escolher melhor o produto pesa tanto quanto postar mais.</p>

<h2>O que muda o resultado</h2>
<h3>A comissão por venda</h3>
<p>Categorias como beleza e moda pagam bem mais que eletrônicos. Veja a <a href="comissao-afiliado-shopee-por-categoria.html">tabela de comissão por categoria</a>.</p>
<h3>A taxa de conversão</h3>
<p>De cada 100 pessoas que clicam no seu link, algumas compram. Produto com desconto real, nota alta e preço de impulso converte mais.</p>
<h3>Os cancelamentos</h3>
<p>Pedido cancelado ou devolvido não paga comissão. Produto com avaliação ruim cancela mais.</p>
<h3>A constância</h3>
<p>Quem posta todo dia tem mais chances de acertar um vídeo que viraliza. Mas postar todo dia produto ruim só cansa.</p>

<h2>Faça a sua conta</h2>
<p>Use a <a href="calculadora-comissao-shopee.html">calculadora de comissão</a> para ver quanto rende um produto e quantas vendas faltam para chegar a R$ 1.000. E para aumentar o ganho por venda, a extensão <a href="./">Garimpo do Afiliado</a> mostra uma nota de 0 a 100 em cada produto da Shopee para você divulgar os que rendem mais.</p>
''',
  },
  {
    'slug': 'erros-afiliado-shopee-iniciante',
    'titulo': '7 erros de afiliado Shopee iniciante (e como evitar)',
    'desc': 'Os erros mais comuns de quem começa como afiliado Shopee: produto errado, comissão baixa, desconto falso e mais. Veja como evitar cada um.',
    'corpo': '''
<p>Quase todo afiliado Shopee comete os mesmos erros no começo. Nenhum deles é grave sozinho, mas juntos fazem muita gente desistir antes de ver resultado.</p>

<h3>1. Divulgar o que você gosta, e não o que vende</h3>
<p>Seu gosto não é o do público. Antes de divulgar, veja se o produto já vende muito e tem nota alta. O número de vendidos é a opinião de milhares de compradores.</p>

<h3>2. Ignorar a comissão</h3>
<p>Divulgar celular a 5% dá o mesmo trabalho que divulgar um sérum a 20%. Confira a <a href="comissao-afiliado-shopee-por-categoria.html">comissão por categoria</a> antes de escolher.</p>

<h3>3. Cair no desconto falso</h3>
<p>"De R$ 299 por R$ 39" quase nunca é real. O público percebe e perde a confiança em você. Prefira descontos plausíveis.</p>

<h3>4. Não ler as avaliações</h3>
<p>Avaliação com foto mostra o produto que chega de verdade. Produto que decepciona vira cancelamento, e cancelamento não paga comissão.</p>

<h3>5. Postar sem constância</h3>
<p>Três vídeos numa semana e nenhum na outra não ajudam o algoritmo. Um ritmo menor, mas fixo, rende mais.</p>

<h3>6. Gastar tempo demais escolhendo</h3>
<p>Abrir 50 produtos e comparar tudo no olho toma a tarde inteira. O tempo deveria ir para gravar e postar.</p>

<h3>7. Não fazer as contas</h3>
<p>Sem saber quanto rende por venda, não dá para saber se vale a pena. Use a <a href="calculadora-comissao-shopee.html">calculadora de comissão</a> e veja <a href="quanto-ganha-afiliado-shopee.html">quanto ganha um afiliado Shopee</a>.</p>

<h2>O atalho para os erros 1, 2, 4 e 6</h2>
<p>A extensão <a href="./">Garimpo do Afiliado</a> dá uma nota de 0 a 100 para cada produto da Shopee, cruzando comissão, desconto, vendas e avaliação. Você abre uma busca e ela já mostra os 10 melhores. A escolha que levava uma tarde passa a levar alguns minutos.</p>
''',
  },
  {
    'slug': 'desconto-falso-shopee',
    'titulo': 'Como identificar desconto falso na Shopee antes de divulgar',
    'desc': 'Como saber se o desconto de um produto da Shopee é real antes de divulgar como afiliado: sinais de preço inflado e o que olhar na página.',
    'corpo': '''
<p>Desconto é um dos maiores motivos para alguém clicar no seu link de afiliado. Mas desconto inflado (preço "de" que ninguém nunca pagou) cansa o público e queima a sua credibilidade. Veja como separar um do outro.</p>

<h2>Sinais de desconto falso</h2>
<ul>
<li><b>Porcentagem exagerada em produto comum:</b> 85% OFF numa capinha ou num organizador quase sempre é preço "de" inventado.</li>
<li><b>Preço "de" fora da realidade:</b> se produtos iguais de outras lojas custam R$ 40, um "de R$ 249" não é referência.</li>
<li><b>Desconto que só existe com cupom:</b> algumas páginas mostram "ou R$ X sem cupom". O preço que o seu público vai pagar pode ser outro.</li>
<li><b>Desconto permanente:</b> se o produto está sempre com o mesmo "70% OFF", o preço normal dele é o preço com desconto.</li>
</ul>

<h2>Sinais de desconto real</h2>
<ul>
<li>Porcentagem entre 20% e 60% sobre um preço parecido com o de outras lojas.</li>
<li>Campanhas com data, como datas duplas (10/10, 11/11) e ofertas relâmpago.</li>
<li>Preço final que continua igual sem depender de cupom.</li>
</ul>

<h2>Por que isso importa para o afiliado</h2>
<p>O seu público volta quando confia nas suas indicações. Um "achado" que não é achado faz a pessoa ignorar os próximos. E produto que decepciona gera cancelamento, que não paga comissão.</p>

<h2>Como conferir rápido</h2>
<p>A extensão <a href="./">Garimpo do Afiliado</a> lê o preço e o desconto da página (incluindo o caso "sem cupom") e usa isso na nota de 0 a 100 de cada produto, junto com comissão, vendas e avaliação. Assim você vê de cara se o desconto ajuda ou se é só enfeite.</p>
''',
  },
]

CSS = '''
  * { box-sizing: border-box; margin: 0; padding: 0; }
  :root { --verde: #14532d; --ouro: #facc15; --escuro: #12121a; --card: #1c1c28; }
  body { font-family: system-ui, -apple-system, "Segoe UI", sans-serif; color: #fff;
    background: var(--escuro); line-height: 1.7; }
  .wrap { max-width: 720px; margin: 0 auto; padding: 0 20px; }
  .topo { padding: 20px 0; display: flex; justify-content: space-between; align-items: center; gap: 12px; flex-wrap: wrap; }
  .topo nav .atual { color: var(--ouro); font-size: 14px; margin-left: 16px; }
  .topo nav a { color: #fff; opacity: .75; text-decoration: none; font-size: 14px; margin-left: 16px; }
  .logo { display: inline-flex; align-items: center; gap: 10px; color: #fff; text-decoration: none; }
  .logo .g { background: var(--verde); color: var(--ouro); width: 36px; height: 36px;
    border-radius: 10px; display: flex; align-items: center; justify-content: center;
    font-weight: 800; font-size: 20px; }
  .logo span { font-weight: 700; }
  h1 { font-size: 32px; line-height: 1.25; margin: 28px 0 10px; }
  .data { font-size: 13px; opacity: .55; margin-bottom: 26px; }
  article p, article li { opacity: .9; font-size: 17px; }
  article p { margin-bottom: 16px; }
  article ul { margin: 0 0 18px 22px; }
  article li { margin-bottom: 8px; }
  article h2 { font-size: 24px; margin: 34px 0 12px; }
  article h3 { font-size: 19px; margin: 22px 0 6px; }
  article a, .lista a { color: var(--ouro); }
  table { width: 100%; border-collapse: collapse; font-size: 16px; margin: 8px 0 16px; }
  td, th { padding: 9px 10px; border-bottom: 1px solid rgba(255,255,255,.08); text-align: left; }
  th { opacity: .7; font-weight: 600; font-size: 13px; }
  .nota { font-size: 13px !important; opacity: .6 !important; }
  .cta-box { background: var(--card); border: 2px solid var(--ouro); border-radius: 16px; padding: 26px; text-align: center; margin: 40px 0; }
  .cta-box h2 { font-size: 21px; margin-bottom: 10px; }
  .cta-box p { opacity: .85; margin-bottom: 18px; }
  .cta { display: inline-block; background: var(--ouro); color: var(--escuro); font-weight: 800;
    font-size: 17px; padding: 14px 30px; border-radius: 12px; text-decoration: none; }
  .lista { list-style: none; }
  .lista li { background: var(--card); border-radius: 12px; padding: 16px 18px; margin-bottom: 12px; }
  .lista li a { font-weight: 700; font-size: 17px; text-decoration: none; }
  .lista li p { opacity: .75; font-size: 14px; margin-top: 4px; }
  h2.rel { font-size: 20px; margin: 10px 0 14px; }
  footer { text-align: center; padding: 40px 20px; opacity: .6; font-size: 14px; }
  footer a { color: var(--ouro); }
  @media (max-width: 480px) { h1 { font-size: 26px; } article p, article li { font-size: 16px; } }
'''

def pagina(titulo_tag, desc, url, corpo, extra_head='', atual=''):
    e = html.escape
    nav = '<span class="atual">Guias</span>' if atual == 'guias' else '<a href="guias.html">Guias</a>'
    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(titulo_tag)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:title" content="{e(titulo_tag)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="pt_BR">
{extra_head}<style>{CSS}</style>
</head>
<body>
<div class="wrap">
  <div class="topo">
    <a class="logo" href="./"><span class="g">G</span><span>Garimpo do Afiliado</span></a>
    <nav>{nav}<a href="calculadora-comissao-shopee.html">Calculadora</a></nav>
  </div>
{corpo}
</div>
<footer>
  <p><a href="./">Garimpo do Afiliado</a> · <a href="guias.html">Guias</a> · <a href="privacy.html">Política de Privacidade</a> · Site independente, sem vínculo com a Shopee.</p>
</footer>
</body>
</html>
'''

CTA = f'''  <div class="cta-box">
    <h2>Descubra em segundos o que vale divulgar</h2>
    <p>O Garimpo do Afiliado é uma extensão grátis do Chrome que dá uma nota de 0 a 100 para cada produto da Shopee.</p>
    <a class="cta" href="{LOJA}" target="_blank" rel="noopener">⛏️ Instalar grátis no Chrome</a>
  </div>
'''

def item(a):
    return f'    <li><a href="{a["slug"]}.html">{html.escape(a["titulo"])}</a><p>{html.escape(a["desc"])}</p></li>'

for a in ARTIGOS:
    url = BASE + a['slug'] + '.html'
    ld = json.dumps({'@context': 'https://schema.org', '@type': 'Article', 'headline': a['titulo'],
                     'description': a['desc'], 'datePublished': DATA, 'dateModified': DATA,
                     'inLanguage': 'pt-BR', 'mainEntityOfPage': url,
                     'author': {'@type': 'Organization', 'name': 'Garimpo do Afiliado', 'url': BASE}},
                    ensure_ascii=False)
    outros = [x for x in ARTIGOS if x is not a][:3]
    corpo = f'''  <article>
    <h1>{html.escape(a['titulo'])}</h1>
    <p class="data">Atualizado em 28/10/2026 · Guia para afiliados</p>
{a['corpo'].strip()}
  </article>
{CTA}  <h2 class="rel">Leia também</h2>
  <ul class="lista">
{chr(10).join(item(x) for x in outros)}
  </ul>'''
    with open(a['slug'] + '.html', 'w', encoding='utf-8', newline='\n') as f:
        f.write(pagina(a['titulo'] + ' — Garimpo do Afiliado', a['desc'], url, corpo,
                       f'<script type="application/ld+json">{ld}</script>\n'))

corpo_guias = f'''  <h1>Guias para afiliados Shopee</h1>
  <p class="data">Como escolher produto, quanto rende cada categoria e como ganhar mais comissão.</p>
  <ul class="lista">
    <li><a href="calculadora-comissao-shopee.html">Calculadora de comissão de afiliado Shopee</a><p>Informe o preço e a categoria e veja quanto você ganha por venda e por mês.</p></li>
{chr(10).join(item(x) for x in ARTIGOS)}
  </ul>
{CTA}'''
with open('guias.html', 'w', encoding='utf-8', newline='\n') as f:
    f.write(pagina('Guias para afiliados Shopee — Garimpo do Afiliado',
                   'Guias práticos para afiliados Shopee: como escolher produto para divulgar, comissão por categoria, achadinhos que vendem e quanto dá para ganhar.',
                   BASE + 'guias.html', corpo_guias, atual='guias'))

urls = ['', 'calculadora-comissao-shopee.html', 'guias.html'] + [a['slug'] + '.html' for a in ARTIGOS] + ['privacy.html']
with open('sitemap.xml', 'w', encoding='utf-8', newline='\n') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    f.write(''.join(f'  <url><loc>{BASE}{u}</loc><lastmod>{DATA}</lastmod></url>\n' for u in urls))
    f.write('</urlset>\n')
print(len(ARTIGOS), 'artigos + guias.html + sitemap.xml')
