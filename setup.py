try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

config = {
  "description": "",
  "author": "Chad Chabot",
  "url": "http://github.com/chadchabot/Boogle",
  "download_url": "https://github.com/chadchabot/Boogle.git",
  "author_email": "chadchabot@gmail.com",
  "version": "0.1",
  "install_requires": ["nose"],
  "packages": ["Boogle"],
  "scripts": [],
  "name": "Boogle"
}

setup(**config)
