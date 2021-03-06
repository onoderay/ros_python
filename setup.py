from setuptools import setup

package_name = 'ros2_py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name,],
    py_modules=[
        'python_programs.talker',
        'python_programs.listener',
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='user',
    author_email="onodera@hoge.com",
    maintainer='user',
    maintainer_email="user@hoge.com",
    keywords=['ROS', 'ROS2'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='TODO: Package description.',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_talker= python_programs.talker:main',
            'my_listener= python_programs.listener:main',
        ],
    },
)