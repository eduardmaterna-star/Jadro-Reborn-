/**
 * JÁDRO REBORN — THE DESCENT, standalone cinematic overlay.
 *
 * Put both this file and preview-earth-12s.html in:
 *   launcher/web/cinematics/
 *
 * In index.html:
 *   <script src="cinematics/intro-integration.js" defer></script>
 *
 * In the existing "New Expedition" click handler, BEFORE changing/saving
 * the current expedition, await:
 *
 *   await window.JadroCinematics.playNewExpeditionIntro();
 *   // Only now run the ORIGINAL, unchanged new-expedition logic.
 *
 * Do NOT invoke this for "Continue" / "Load game". It must not be attached
 * to a global startup event.
 */
(function(){
  'use strict';
  let active=false;
  function playNewExpeditionIntro(){
    if(active)return Promise.reject(new Error('Intro already playing'));
    active=true;
    return new Promise((resolve)=>{
      const overlay=document.createElement('div');
      overlay.id='jadro-cinematic-overlay';
      Object.assign(overlay.style,{
        position:'fixed',inset:'0',zIndex:'2147483647',
        background:'#020611',display:'block',overflow:'hidden'
      });
      const iframe=document.createElement('iframe');
      iframe.title='JÁDRO REBORN — THE DESCENT';
      iframe.src='cinematics/preview-earth-12s.html';
      iframe.allow='autoplay';
      Object.assign(iframe.style,{border:'0',width:'100%',height:'100%',display:'block'});
      overlay.appendChild(iframe);
      let done=false;
      function finish(skipped){
        if(done)return;
        done=true;active=false;
        window.removeEventListener('message',onMessage);
        window.removeEventListener('keydown',onKey,true);
        overlay.remove();
        resolve({skipped:Boolean(skipped)});
      }
      function onMessage(event){
        if(event.source!==iframe.contentWindow)return;
        if(event.origin!==window.location.origin)return;
        if(event.data?.type!=='jadro:intro-finished')return;
        finish(event.data.skipped);
      }
      function onKey(event){
        if(event.key==='Escape'){
          event.preventDefault();
          event.stopImmediatePropagation();
          finish(true);
        }
      }
      window.addEventListener('message',onMessage);
      window.addEventListener('keydown',onKey,true);
      document.body.appendChild(overlay);
    });
  }
  window.JadroCinematics={playNewExpeditionIntro};
})();