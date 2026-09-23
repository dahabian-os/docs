// Tiny helper for the Issues page: text search + module / priority / category filters.
// The site works without JavaScript; this only adds filtering.
(function () {
  var table = document.querySelector('table.issues');
  if (!table) return;
  var rows = Array.prototype.slice.call(table.tBodies[0].rows);
  var q = document.getElementById('f-q');
  var mod = document.getElementById('f-mod');
  var prio = document.getElementById('f-prio');
  var cat = document.getElementById('f-cat');
  var count = document.getElementById('f-count');

  function apply() {
    var text = (q.value || '').toLowerCase().trim();
    var shown = 0;
    rows.forEach(function (r) {
      var ok = (!text || r.textContent.toLowerCase().indexOf(text) !== -1) &&
        (!mod.value || r.dataset.mod === mod.value) &&
        (!prio.value || r.dataset.prio === prio.value) &&
        (!cat.value || r.dataset.cat === cat.value);
      r.hidden = !ok;
      if (ok) shown++;
    });
    count.textContent = shown + ' of ' + rows.length + ' issues';
  }
  [q, mod, prio, cat].forEach(function (el) { el.addEventListener('input', apply); });
  apply();
})();
