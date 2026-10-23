"""Copies de travail des compléments officiels ; aucun PDF externe n'est publié sur GitHub."""
import json,pathlib,sys,urllib.request,concurrent.futures
from pypdf import PdfReader
sys.stdout.reconfigure(encoding='utf-8')
root=pathlib.Path(__file__).resolve().parents[1]
out=root/'docs/sources';out.mkdir(exist_ok=True)
tags=['005','033','110','115','116','117','120','121','125','126','127','128','135','181','182','183','203','231','283','301','316','541']
def collect(tag):
    lang='eng' if tag in ['203','283'] else 'fre'
    url='https://www.transition-bibliographique.fr/B'+tag+'_'+lang
    dest=out/('Expansion-'+tag+'.pdf')
    if not dest.exists():urllib.request.urlretrieve(url,dest)
    pages=[p.extract_text() for p in PdfReader(dest).pages]
    return tag,{'url':url,'language':lang,'pages':pages}
results={}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    for tag,result in pool.map(collect,tags):
        results[tag]=result
        print(tag+': '+str(len(result['pages']))+' pages',flush=True)
(out/'expansion-extractions.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
