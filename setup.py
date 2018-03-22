from os.path import join
import re
from setuptools import setup, find_packages


# dynamically pull the version from django_ace/__init__.py
version = re.search('^__version__ = "(.+?)"$',
                    open(join('django_rholang_editor', '__init__.py')).read(), re.MULTILINE).group(1)
packages = find_packages(exclude=["rhoeditor_demo.*","rhoeditor_demo"])
setup(
    name='django_rholang_editor',
    version=version,
    description='django rholang editor app based on ace editor',
    long_description=open('README.md').read(),

    author='zsluedem',
    author_email='zsluedem06@gmail.com',
    license="Simplified BSD",
    url='https://github.com/zsluedem/django-rholang-editor',

    packages=packages,
    include_package_data=True,
    install_requires=[
        'Django',
        "django-js-asset==1.0.0"
    ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        ],
    keywords=["rholang"]
    )