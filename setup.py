# coding: utf-8
from setuptools import setup, find_packages
import pathlib
from djangocms_mdeditor import (__VERSION__, __AUTHOR__, __AUTHOR_EMAIL__)


here = pathlib.Path(__file__).parent.resolve()

setup(
    name='djangocms-mdeditor',
    version=__VERSION__,
    description='Text Plugin for django CMS using Martor for Markdown-enabled text-editing.',
    long_description=(here / 'README.md').read_text(encoding='utf-8'),
    long_description_content_type='text/markdown',
    keywords=['python', 'markdown', 'django', 'addon', 'django-cms'],
    url='https://github.com/danniranderis/djangocms-mdeditor',
    download_url='https://github.com/danniranderis/djangocms-mdeditor'
                 '/tarball/v%s' % __VERSION__,
    license='MIT',
    author=__AUTHOR__,
    author_email=__AUTHOR_EMAIL__,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.7',
        # 'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Framework :: Django CMS',
        # 'Framework :: Django CMS 3.9',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
    ],
    python_requires='>=3.9',
    install_requires=[
        'django-cms>=3.9',
        'martor>=1.6.4',
    ],
    packages=find_packages(),
    include_package_data=True,
    # package_data={
    #     'ff': ['f']
    # },
)
