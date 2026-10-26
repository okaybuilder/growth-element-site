const {chromium}=require('playwright');const fs=require('fs');
const dir=process.argv[2];const svg=fs.readFileSync(dir+'/favicon.svg','utf8');
(async()=>{const b=await chromium.launch();
for(const s of [16,32,48,180,192,512]){const pg=await b.newPage({viewport:{width:s,height:s}});
 // Apple touch icons get a full-bleed square (iOS rounds corners itself)
 const art=s===180?svg.replace('rx="6"','rx="0"'):svg;
 await pg.setContent(`<html><body style="margin:0;background:transparent">${art.replace('<svg ','<svg width="'+s+'" height="'+s+'" ')}</body></html>`);
 await pg.screenshot({path:`${dir}/icon-${s}.png`,omitBackground:true,clip:{x:0,y:0,width:s,height:s}});await pg.close();}
await b.close();})();
