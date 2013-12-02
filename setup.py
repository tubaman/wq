from os.path import join, dirname
from setuptools import setup

LONG_DESCRIPTION = """
A modular framework for building custom offline-capable desktop and mobile web apps.
"""


def long_description():
    """Return long description from README.rst if it's present
    because it doesn't get installed."""
    try:
        return open(join(dirname(__file__), 'README.rst')).read()
    except IOError:
        return LONG_DESCRIPTION

setup(
    name='wq',
    version='0.4.0-dev',
    author='S. Andrew Sheppard',
    author_email='andrew@wq.io',
    url='http://wq.io/',
    license='MIT',
    description=LONG_DESCRIPTION.strip(),
    long_description=long_description(),
    install_requires=['wq.app==0.5.0-dev', 'wq.io==0.4.0-dev', 'wq.db==0.4.0-dev'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: JavaScript',
        'Programming Language :: Python :: 2.7',
        'Framework :: Django',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Text Processing :: Markup :: HTML',
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Pre-processors',
        'Topic :: Database :: Database Engines/Servers',
        'Topic :: Text Processing :: Markup :: XML',
    ]
)
