from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='hashchain',
    version='1.0.0',
    description='Helper to certify database entries, using hashchains and blockchains',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/svandegar/hashchain',
    author='Seraphin Vandegar',
    author_email='svandegar@hotmail.com',
    license='MIT',
    packages=['hashchain','hashchain.ethereum'],
    zip_safe=False,
    download_url='',
    install_requires=[
        'web3',
        'pysha3'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5'
    ]
)
