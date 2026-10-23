import json,re,sys,pathlib,urllib.request
from pypdf import PdfReader
sys.stdout.reconfigure(encoding='utf-8')
root=pathlib.Path(__file__).resolve().parents[1]
out=root/'docs'/'sources'
out.mkdir(exist_ok=True)
sources={}
for tag in ['017','317','320','359','830','850','852']:
    url='https://www.transition-bibliographique.fr/B'+tag+'_fre'
    dest=out/('CfU-'+tag+'.pdf')
    if not dest.exists():
        urllib.request.urlretrieve(url,dest)
    pages=[p.extract_text() for p in PdfReader(dest).pages]
    sources[tag]={'url':url,'pages':pages}
    print(tag+': '+str(len(pages))+' pages')
(out/'cfu-extractions.json').write_text(json.dumps(sources,ensure_ascii=False,indent=2),encoding='utf-8')
