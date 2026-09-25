/* Перемикач теми макета: пам'ятає вибір між сторінками й ставить data-theme на <html> —
   на це реагують токени ui/kit.css. Єдиний скрипт у вайрфреймах — рев'ю-хром, не поведінка застосунку.
   Підключається одразу після .nw-theme, синхронно, щоб тема стояла до першого малювання.
   localStorage може бути недоступний (приватне вікно) — тоді лишається світла. */
(function () {
  var KEY = 'nw-theme', root = document.documentElement, saved = null;
  try { saved = localStorage.getItem(KEY); } catch (e) {}
  function apply(t) { root.setAttribute('data-theme', t); }
  apply(saved === 'dark' ? 'dark' : 'light');
  if (saved === 'dark') { var d = document.getElementById('nw-dark'); if (d) d.checked = true; }
  document.addEventListener('change', function (e) {
    var t = e.target;
    if (!t || t.name !== 'nw-theme') return;
    var v = t.id === 'nw-dark' ? 'dark' : 'light';
    apply(v);
    try { localStorage.setItem(KEY, v); } catch (e2) {}
  });
})();
