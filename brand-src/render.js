const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:1200,height:630}});
for(const f of process.argv.slice(2)){await pg.goto('file://'+__dirname+'/'+f+'.html');await pg.evaluate(()=>document.fonts.ready);
 const fonts=await pg.evaluate(()=>[...document.fonts].filter(x=>x.status==='loaded').map(x=>x.family+x.weight));console.log(f,fonts.join(','));
 await pg.screenshot({path:__dirname+'/'+f+'.png'});}
await b.close();})();
