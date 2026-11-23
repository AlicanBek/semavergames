/* @ds-bundle: {"format":4,"namespace":"Semaver","components":[]} */
/* Draws the pointed (hexagonal) outline behind every .sg-btn--hex and .sg-play.
   Proportions (tip depth, lip height) are taken from the Yanık Masası build.
   Two layers: a lip polygon and the gradient face with the shared 2px gold border.
   Colours come from the same --btn-* custom properties as the rounded button. */
(function () {
  var NS = 'http://www.w3.org/2000/svg';
  var count = 0;

  function pts(list) {
    return list.map(function (p) { return p[0].toFixed(1) + ',' + p[1].toFixed(1); }).join(' ');
  }

  function draw(el) {
    var w = el.offsetWidth, h = el.offsetHeight;
    if (!w || !h) return;
    var lip = h * 0.0816;          // 5.8 of 71.04
    var f = h - lip;               // face height
    var t = f * 0.294;             // tip depth, 19.2 of 65.3
    function hex(y) {
      return pts([[t, y], [w - t, y], [w, y + f / 2], [w - t, y + f], [t, y + f], [0, y + f / 2]]);
    }

    var svg = el.querySelector(':scope > svg.sg-facet');
    if (!svg) {
      svg = document.createElementNS(NS, 'svg');
      svg.setAttribute('class', 'sg-facet');
      svg.setAttribute('aria-hidden', 'true');
      svg.setAttribute('focusable', 'false');
      svg.dataset.id = 'sg-facet-' + (++count);
      el.insertBefore(svg, el.firstChild);
      el.classList.add('is-drawn');
    }
    var id = svg.dataset.id;
    svg.setAttribute('width', w);
    svg.setAttribute('height', h);
    svg.innerHTML =
      '<defs>' +
      '<linearGradient id="' + id + '" x1="0" y1="0" x2="0" y2="1">' +
      '<stop offset="0" style="stop-color:var(--btn-a)"/>' +
      '<stop offset="0.55" style="stop-color:var(--btn-b)"/>' +
      '<stop offset="1" style="stop-color:var(--btn-c)"/>' +
      '</linearGradient>' +
      '</defs>' +
      '<polygon class="sg-facet__lip" points="' + hex(lip) + '"/>' +
      '<polygon class="sg-facet__face" points="' + hex(0) + '" fill="url(#' + id + ')"/>';
  }

  var ro = typeof ResizeObserver === 'function'
    ? new ResizeObserver(function (entries) { entries.forEach(function (e) { draw(e.target); }); })
    : null;

  function init(root) {
    (root || document).querySelectorAll('.sg-btn--hex, .sg-play').forEach(function (el) {
      draw(el);
      if (ro) ro.observe(el);
    });
  }

  window.Semaver = { facet: draw, init: init };
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () { init(); });
  } else {
    init();
  }
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(function () { init(); });
})();
