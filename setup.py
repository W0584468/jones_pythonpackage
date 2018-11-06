from Bio.Blast import NCBIXML

setup(name='Jones Python Package',
      version='0.1',
      description='Read a matrix and run BLAST searches',
      url='TBD',
      author='April',
      author_email='denzel.jones@selu.edu',
      license='MIT',
      packages=['jones_pythonproject'],
      install_requires=[
          'dendropy',
          'pandas',
          'biopython'
       
      ],
      long_description=open('README.txt').read(),
zip_safe=True)