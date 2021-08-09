from setuptools import setup

setup(name='bracketpy',
      version='0.0.1',
      description='Domain-agnostic implementation of finite dimensional Lie '
                  'algebras and related algorithms',
      url='https://github.com/Onidsouza/bracketpy',
      author='Henrique Souza',
      author_email='henrique.ams.souza@gmail.com',
      license='GNU General Public License v3.0',
      install_requires=['tqdm']
      packages=['bracketpy'],
      zip_safe=False)
