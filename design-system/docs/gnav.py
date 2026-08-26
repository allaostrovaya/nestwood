# -*- coding: utf-8 -*-
"""Глобальна навігація по документах — один рендерер на всі сторінки."""

DOCS = [
 ('research',   'research/research.html',  'Ресерч',          'ринок, конкуренти, джерела даних'),
 ('personas',   'concept/personas.html',   'Персони & JTBD',  'хто це і які в них jobs'),
 ('ia',         'wireframes/ia.html',      'Архітектура',     'екрани, потоки, трасування'),
 ('wireframes', 'wireframes/plan.html',    'Вайрфрейми',      '48 сторінок, дерево праворуч'),
]

def gnav(active, prefix, home='wireframes/plan.html'):
    """active — ключ поточного документа; prefix — шлях до кореня репо ('../' або './')."""
    out = ['<nav class="gnav" aria-label="Документи проєкту">',
           f'  <a class="gnav-brand" href="{prefix}{home}">Nestwood<span>ДОКУМЕНТИ</span></a>',
           '  <p class="gnav-label">Проєкт</p>',
           '  <ul>']
    for i, (key, href, name, sub) in enumerate(DOCS, 1):
        cur = ' aria-current="page"' if key == active else ''
        out.append(f'    <li><a class="gnav-item" href="{prefix}{href}"{cur}>'
                   f'<span class="n">0{i}</span>'
                   f'<span><b>{name}</b><small>{sub}</small></span></a></li>')
    out += ['  </ul>', '</nav>']
    return '\n'.join(out)
