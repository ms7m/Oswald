NAME = "oswald"
VERSION = "0.0.1"
DESCRIPTION = "Organize and rapidly/easily create endpoints for an API. Built on top of Falcon."
AUTHOR = "Mustafa Mohamed"
AUTHOR_EMAIL = "mustafa@ms7m.me"
REQUIRES_PYTHON = '>=3.6.0'
URL = 'https://github.com/ms7m/oswald'

from setuptools import find_packages, setup, Command

REQUIRED = [
    'falcon',
    'loguru'
]

setup(
    name="oswald",
    version="0.0.3",
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    #packages=find_packages(exclude=["testing", "*.testing", "*.testing.*", "testing.*"]),
    # If your package is a single module, use this instead of 'packages':
    py_modules=['oswald'],

    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    #install_requires=REQUIRED,
    #extras_require=EXTRAS,
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)