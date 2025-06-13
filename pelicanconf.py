#!/usr/bin/env python
# -*- coding: utf-8 -*-

AUTHOR = 'Gerardo Rocha Benigno'
SITENAME = 'Multiplataforma'
SITEURL = ''
SITESUBTITLE = 'Un blog sobre ML y Sistemas de Pago'

PATH = 'content'
TIMEZONE = 'America/Mexico_City'
DEFAULT_LANG = 'es'

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Widget de redes sociales
SOCIAL = (
    ('github', 'https://github.com/gerardorochabenigno'),
    ('linkedin', 'https://www.linkedin.com/in/gerardorochabenigno'),
)

DEFAULT_PAGINATION = 10

THEME = 'themes/monospace'
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

# Comenta los plugins por ahora
# PLUGIN_PATHS = ['plugins']
# PLUGINS = ['sitemap', 'neighbors']
# SITEMAP = {
#     'format': 'xml',
#     'priorities': {
#         'articles': 0.5,
#         'indexes': 0.5,
#         'pages': 0.5
#     },
#     'changefreqs': {
#         'articles': 'monthly',
#         'indexes': 'daily',
#         'pages': 'monthly'
#     }
# }

STATIC_PATHS = ['images', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

DISPLAY_PAGES_ON_MENU = True