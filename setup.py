from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='regexp_replace_middleware',
      version=version,
      description="Filter http response with regular expression",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Taras Kozlovskyi',
      author_email='ktarasz@quintagroup.com',
      url='http://quintagroup.com',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [paste.filter_app_factory]
      regexp_replace_middleware = regexp_replace_middleware.middleware:make_wsgi_middleware
      """,
      )
