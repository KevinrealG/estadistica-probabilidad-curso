document.addEventListener("DOMContentLoaded", () => {

const accordions=document.querySelectorAll(".accordion button");
accordions.forEach(btn=>{
  btn.addEventListener("click",()=>{
    const panel=btn.nextElementSibling;
    const open=panel.style.display==="block";
    document.querySelectorAll(".accordion-content").forEach(p=>p.style.display="none");
    panel.style.display=open?"none":"block";
  });
});

const progress=document.createElement("div");
progress.id="progress-bar";
progress.style.cssText="position:fixed;top:0;left:0;height:4px;background:#38bdf8;width:0%;z-index:9999;";
document.body.appendChild(progress);

window.addEventListener("scroll",()=>{
 const h=document.documentElement;
 const sc=(h.scrollTop)/(h.scrollHeight-h.clientHeight)*100;
 progress.style.width=sc+"%";
});

const topBtn=document.createElement("button");
topBtn.innerHTML="↑";
topBtn.id="topBtn";
topBtn.style.cssText="position:fixed;right:20px;bottom:20px;width:50px;height:50px;border:none;border-radius:50%;background:#2563eb;color:#fff;font-size:22px;cursor:pointer;display:none;z-index:999;";
document.body.appendChild(topBtn);

window.addEventListener("scroll",()=>{
 topBtn.style.display=window.scrollY>300?"block":"none";
});

topBtn.onclick=()=>window.scrollTo({top:0,behavior:"smooth"});

const observer=new IntersectionObserver(entries=>{
 entries.forEach(e=>{
   if(e.isIntersecting){
     e.target.animate([
      {opacity:0,transform:"translateY(30px)"},
      {opacity:1,transform:"translateY(0px)"}
     ],{duration:600,fill:"forwards"});
   }
 });
},{threshold:.15});

document.querySelectorAll(".card,.section,.hero-content").forEach(el=>observer.observe(el));

document.querySelectorAll("pre code").forEach(code=>{
 const btn=document.createElement("button");
 btn.textContent="Copiar";
 btn.style.cssText="float:right;margin:5px;padding:6px 10px;cursor:pointer;";
 btn.onclick=()=>{
   navigator.clipboard.writeText(code.innerText);
   btn.textContent="Copiado";
   setTimeout(()=>btn.textContent="Copiar",1500);
 };
 code.parentElement.insertBefore(btn,code);
});

const toggle=document.createElement("button");
toggle.innerHTML="🌙";
toggle.style.cssText="position:fixed;left:20px;bottom:20px;width:50px;height:50px;border:none;border-radius:50%;cursor:pointer;z-index:999;";
document.body.appendChild(toggle);

toggle.onclick=()=>{
 document.body.classList.toggle("light");
 if(document.body.classList.contains("light")){
   document.body.style.background="#f8fafc";
   document.body.style.color="#111";
   toggle.innerHTML="☀";
 }else{
   document.body.style.background="";
   document.body.style.color="";
   toggle.innerHTML="🌙";
 }
};

});

