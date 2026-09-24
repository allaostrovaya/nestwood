/* Перемикач теми макета: пам'ятає вибір між сторінками. Єдиний скрипт у вайрфреймах —
   рев'ю-хром, не поведінка застосунку. Підключається одразу після .nw-theme, синхронно,
   щоб потрібна тема стояла до першого малювання. localStorage може бути недоступний
   (приватне вікно, заблоковані дані) — тоді просто лишається світла. */
(function () {
  var KEY = 'nw-theme';
  var saved = null;
  try { saved = localStorage.getItem(KEY); } catch (e) {}
  if (saved === 'dark') { var d = document.getElementById('nw-dark'); if (d) d.checked = true; }
  document.addEventListener('change', function (e) {
    var t = e.target;
    if (!t || t.name !== 'nw-theme') return;
    try { localStorage.setItem(KEY, t.id === 'nw-dark' ? 'dark' : 'light'); } catch (e2) {}
  });
})();
