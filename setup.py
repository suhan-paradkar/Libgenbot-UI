import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
  name = 'Libgenbot-UI',
  packages = ['LibgenUI'],
  version = '1.0.0-alpha-02',
  license='GPL-3.0',
  description = 'Libgenbot-UI is a UI version for Libgenbot',
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'Suhan G Paradkar',
  author_email = 'suhangp2002@gmail.com',
  url = 'https://github.com/suhan-paradkar/Libgenbot',
  download_url = 'https://github.com/suhan-paradkar/Libgenot/archive/v1.0.0-alpha.tar.gz',
  keywords = ['download-papers','google-scholar', 'libgen', 'scihub', 'scholar', 'crossref', 'papers'],
  install_requires=[
        'Libgenbot',
        'guizero',
        'pillow',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Science/Research',
    'Topic :: Scientific/Engineering',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
  package_data={
    'LibgenUI': ['img/*.png',
                'img/*.gif',],
  },
  entry_points={
    'console_scripts': ["LibgenUI=LibgenUI.UI:main"],
  },
)
