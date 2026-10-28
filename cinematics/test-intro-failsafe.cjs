const assert=require('node:assert/strict');
const fs=require('node:fs');
const vm=require('node:vm');
const code=fs.readFileSync(__dirname+'/intro-integration.js','utf8');
async function scenario(mode){
  let now;
  const listeners={};
  const body={appendChild(node){this.node=node;}};
  const iframe={style:{},contentWindow:{},addEventListener(n,fn){this['on'+n]=fn;}};
  const overlay={style:{},appendChild(node){this.iframe=node;},remove(){this.removed=true;}};
  const document={body,createElement(type){return type==='iframe'?iframe:overlay;}};
  const win={location:{origin:'http://localhost'},addEventListener(n,fn){listeners[n]=fn;},removeEventListener(n){delete listeners[n];}};
  const timers=new Map();let timerId=0;
  const ctx={window:win,document,setTimeout(fn){timers.set(++timerId,fn);return timerId;},clearTimeout(id){timers.delete(id);}};
  vm.runInNewContext(code,ctx);
  const pending=win.JadroCinematics.playNewExpeditionIntro();
  assert.equal(body.node,overlay);
  if(mode==='error')iframe.onerror();
  if(mode==='timeout'){assert.equal(timers.size,1);[...timers.values()][0]();}
  if(mode==='success'){listeners.message({source:iframe.contentWindow,origin:win.location.origin,data:{type:'jadro:intro-finished',skipped:false}});}
  const result=await pending;
  assert.equal(result.skipped,mode!=='success');
  assert.equal(overlay.removed,true);
  assert.equal(timers.size,0);
  assert.equal(Object.keys(listeners).length,0);
}
(async()=>{for(const s of ['error','timeout','success'])await scenario(s);console.log('PASS cinematic: complete, iframe error, and timeout');})().catch(e=>{console.error(e);process.exitCode=1;});
