from setuptools import setup

setup(name='DJonesPythonPackage',
      version='0.1',
      description='Read a matrix and run BLAST searches',
      url='TBD',
      author='Denzel Jones',
      author_email='denzel.jones@selu.edu',
      license='MIT',
      packages=['djonespythonpackage'],
      install_requires=[
          'dendropy',
          'pandas',
          'biopython'
          
       
      ],
      long_description=open('README.txt').read(),
zip_safe=True)
