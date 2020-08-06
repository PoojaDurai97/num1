from setuptools import setup

setup(
    name='num1',
    version='0.0.1',
    description='My private package from private github repo',
    url='https://github.com/PoojaDurai97/num1',
    author='Pooja Durai',
    author_email='poojadurai1997@gmail.com',
    license='unlicense',
    packages=['num1'],
    install_requires=[
       
        'pandas==0.23.3',
        'numpy>=1.14.5',
        
    ]
    zip_safe=False
)