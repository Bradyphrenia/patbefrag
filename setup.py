from setuptools import find_packages, setup
from setuptools.extension import Extension

from Cython.Build import cythonize
from Cython.Distutils import build_ext

setup(
    name='patbefrag',
    version='0.12',
    packages=['window', 'ui_form', 'database', 'checkboxdict'],
    ext_modules=cythonize(
        [
            Extension("checkboxdict",
                      ["checkboxdict/checkboxdict.py"]),
            Extension("database",
                      ["database/database.py"]),
            Extension("datadict",
                      ["datadict/datadict.py"]),
            Extension("datafielddict",
                      ["datafielddict/datafielddict.py"]),
            Extension("ui_form",
                      ["ui_form/ui_form.py"]),
            Extension("window",
                      ["window/window.py"]),
        ],
        build_dir="build_cythonize",
        compiler_directives={
            'language_level': "3",
            'always_allow_keywords': True,
        }
    ),
    cmdclass=dict(
        build_ext=build_ext
    ),
    url='',
    license='',
    author='Steffen Troeger',
    author_email='bradyphrenia@icloud.com',
    description=''
)
