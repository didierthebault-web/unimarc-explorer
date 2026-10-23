const fs=require('fs'),path=require('path');
const root=path.resolve(__dirname,'..'),out=path.join(root,'_site');
fs.mkdirSync(out,{recursive:true});
for(const file of ['index.html','styles.css','app.js','unimarc-explorer.html'])fs.copyFileSync(path.join(root,file),path.join(out,file));
fs.mkdirSync(path.join(out,'data'),{recursive:true});
for(const file of ['catalogue.js','unimarc.json','exemples.json'])fs.copyFileSync(path.join(root,'data',file),path.join(out,'data',file));
fs.writeFileSync(path.join(out,'.nojekyll'),'');
console.log('GitHub Pages : fichiers statiques préparés dans _site/.');
