from distutils.core import setup

install_requires = [
    'docopt',
    'lxml',
    'beautifulsoup4',
    'requests']

setup(name='craigslist2org',
      version='0.0',
      description='Craigslist to Emacs org-mode parser',
      author='Noah Brenowitz',
      author_email='nbren12@gmail.com',
      scripts = ['craigslist2org.py'],
      install_requires=install_requires)
