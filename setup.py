from setuptools import setup, find_packages

setup(
    name='mlproject1',
    version=0,
    include_package_data=True,
    author='gagankh123',
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=['Flask>=2.3.2'],
    entry_points={
            'console_scripts': [
                'ts_app = ts_app.startup:main',
            ],
        },
    # packages=['ts_app']
)