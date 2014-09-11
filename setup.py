from setuptools import setup, find_packages

setup(
    name='Arbitrary File Protocol',
    version='0.1.0',
    packages=find_packages(),
    zip_safe=False,
    author="Santiago Torres",
    author_email="santiago@nyu.edu",
    install_requires=[
        ""
    ],
    classifiers=['Development Status :: 3 - Alpha',
                 'Intended Audience :: Developers',
                 'Intended Audience :: Science/Research',
                 'Intended Audience :: System Administrators',
                 'Environment :: Web Environment',
                 'License :: OSI Approved :: GPLv3 License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 3',
                 'Topic :: Utilities'],
)
