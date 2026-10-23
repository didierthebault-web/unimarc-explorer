import json,re,pathlib,sys
sys.stdout.reconfigure(encoding='utf-8')
root=pathlib.Path(__file__).resolve().parents[1]
pages=json.loads((root/'docs/bnf-pages.json').read_text(encoding='utf-8'))
lines=[]
for p,t in enumerate(pages[9:60],10):
    for l in t.splitlines():
        if 'Format UNIMARC des notices' in l or re.match(r'^\s*page \d+/66',l):continue
        lines.append((p,l))
starts=[]
for i,(p,l) in enumerate(lines):
    m=re.match(r'^\s{0,6}(\d{3})\s+(\S.*)',l)
    if m and not re.match(r'^\s*\d{3}\s+[A-Z]{2,}\s*$',l):starts.append((i,m[1],m[2]))
fields={}
for k,(i,tag,title) in enumerate(starts):
    if tag in fields:continue
    end=starts[k+1][0] if k+1<len(starts) else len(lines)
    section=lines[i:end]
    # Stop before following numbered section or a footnote; retain page-spanning tables.
    raw='\n'.join(l for p,l in section)
    title=re.sub(r'\d+$','',title).strip()
    subzone=False;subs={};current=None
    for p,l in section[1:]:
        if 'Sous-zone(s)' in l:subzone=True;continue
        m=re.match(r'^\s+\$([a-z0-9])(?:/([ab]))?\s+(.+)',l)
        if m and (subzone or tag in ['100','102']):
            code=m[1];label=m[3].strip();current=code
            if m[2]:label+=' (usage $'+code+'/'+m[2]+')'
            if code in subs:subs[code]+=' / '+label
            else:subs[code]=label
        elif current and l.strip() and not re.match(r'^\s*\$',l):
            # Continuations of labels are substantially indented; omit explanatory footnotes.
            if len(l)-len(l.lstrip())>=19 and not re.match(r'^\s*\d+\s',l):
                subs[current]+=' '+l.strip()
            else:current=None
    fields[tag]={'title':title,'pages':sorted(set(p for p,l in section if l.strip())),'subs':subs,'raw':raw}
(root/'docs/sources/bnf-fields.json').write_text(json.dumps(fields,ensure_ascii=False,indent=2),encoding='utf-8')
selected=json.loads((root/'data/unimarc.json').read_text(encoding='utf-8'))['fields']
for f in selected:
    if f['tag'] in fields:
        x=fields[f['tag']]
        print(f['tag']+' p.'+','.join(map(str,x['pages']))+' '+x['title']+' | '+','.join(x['subs']))
    else:print(f['tag']+' ABSENT BnF')
