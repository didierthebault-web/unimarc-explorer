const fs=require('fs'),path=require('path');
const root=path.resolve(__dirname,'..');
const data=JSON.parse(fs.readFileSync(path.join(root,'data/unimarc.json'),'utf8'));
for(const f of data.fields){for(const key of ['title','function','example','errors','practice','source','version','profile'])if(!f[key])throw Error(f.tag+' : '+key+' absent');if(!f.control&&f.indicators.length!==2)throw Error(f.tag+' : indicateurs absents');}
fs.writeFileSync(path.join(root,'data/catalogue.js'),'window.UNIMARC_DATA='+JSON.stringify(data)+';');
fs.writeFileSync(path.join(root,'data/exemples.json'),JSON.stringify({status:'Exemples pédagogiques réduits ; aucune notice complète prête à importer',examples:data.fields.map(f=>({tag:f.tag,raw:f.example,note:f.exampleNote,source:f.source,version:f.version,consulted:f.consulted}))},null,2));
let html=fs.readFileSync(path.join(root,'index.html'),'utf8').replace('<link rel="stylesheet" href="styles.css">',()=>'<style>'+fs.readFileSync(path.join(root,'styles.css'),'utf8')+'</style>');
html=html.replace('<script src="data/catalogue.js"></script>',()=>'<script>'+fs.readFileSync(path.join(root,'data/catalogue.js'),'utf8')+'</script>').replace('<script src="app.js"></script>',()=>'<script>'+fs.readFileSync(path.join(root,'app.js'),'utf8')+'</script>');
fs.writeFileSync(path.join(root,'unimarc-explorer.html'),html);
let inventory='# Inventaire documenté — 23 octobre 2026\n\n'+data.fields.length+' fiches : '+data.fields.filter(f=>f.bnfCoverage).length+' fondées sur le profil de diffusion BnF 11.0 (2023), '+data.fields.filter(f=>!f.bnfCoverage).length+' compléments explicites.\n\n';
for(const b of data.blocks){inventory+='## '+b.id+' — '+b.title+'\n\n';for(const f of data.fields.filter(f=>f.block===b.id))inventory+='- **'+f.tag+' — '+f.title+'** : '+f.profile+'. '+f.version+'. [Source]('+f.sourceLink+').\n';inventory+='\n';}
inventory+='## Enrichissements possibles\n\nAucune des '+data.fields.length+' entrées ne reste vide. Les règles d’obligation et de répétabilité non spécifiées dans le document BnF sont explicitement signalées, sans les inventer. Une comparaison exhaustive avec la dernière édition internationale, une validation professionnelle indépendante et une grille Koha identifiée restent à ajouter.\n';
fs.writeFileSync(path.join(root,'docs/INVENTAIRE.md'),inventory);
console.log('Génération terminée : '+data.fields.length+' fiches documentées ; JSON source conservé.');
