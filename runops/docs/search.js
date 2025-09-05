
// Simple client-side search for RunOps docs
(async function(){
  async function fetchPage(path){
    try {
      const r = await fetch(path);
      return await r.text();
    } catch(e){ return ""; }
  }

  const pages = [
    {title:"Overview", path:"index.html"},
    {title:"Common Role", path:"common.html"},
    {title:"Linux Role", path:"linux.html"},
    {title:"Windows Role", path:"windows.html"},
    {title:"Cheat Sheet", path:"cheatsheet.html"}
  ];

  // Build index
  const index = [];
  for (const p of pages){
    const html = await fetchPage(p.path);
    const text = html.replace(/<[^>]+>/g, " ");
    index.push({title: p.title, path: p.path, text: text.toLowerCase()});
  }

  const input = document.getElementById("search-input");
  const results = document.getElementById("search-results");
  if (!input || !results) return;

  function render(items){
    results.innerHTML = "";
    if (!items.length){
      results.innerHTML = "<div class='muted'>No matches.</div>";
      return;
    }
    for (const it of items.slice(0, 20)){
      const a = document.createElement("a");
      a.href = it.path;
      a.textContent = it.title;
      const div = document.createElement("div");
      div.className = "result";
      div.appendChild(a);
      results.appendChild(div);
    }
  }

  input.addEventListener("input", () => {
    const q = input.value.trim().toLowerCase();
    if (!q){ results.innerHTML = ""; return; }
    const items = index.filter(it => it.text.includes(q));
    render(items);
  });
})();
