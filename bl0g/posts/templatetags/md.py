from markdown import Markdown
from django import template

register = template.Library()

_md = Markdown(
    extensions=[
        'md_mermaid',
        'meta',
        'extra',
        'admonition',
        'codehilite',
        'attr_list',
        'def_list',
        # 'nl2br',
        # 'mdx_math',
        'pymdownx.arithmatex',
        'pymdownx.tabbed',
        'pymdownx.emoji',
        'pymdownx.magiclink',
        'toc'
    ]
)


@register.filter
def brief(txt, size=1024):
    res = ''
    for line in txt.splitlines():
        if len(res) + len(line) > size:
            break
        res += line + '\n'
    return res


@register.filter
def md(txt):
    return _md.convert(txt)
