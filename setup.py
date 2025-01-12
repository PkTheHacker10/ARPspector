"""
    setup file for the ARPspector tool.
"""

from setuptools import find_packages,setup

with open("README.md","r",encoding="utf-8") as file:
    tool_description=file.read()
    
setup(
    name="ARPspector",
    version='1.0.0',
    author="pk_the_hacker",
    author_email="pevinbalaji@gmail.com",
    description=tool_description,
    packages=find_packages(),
    install_requires=[
        'art==6.4',
        'colorama==0.4.6',
        'scapy>=2.6.1',
        'requests>=2.32.3',
        'logging>=0.4.9.6'
    ],
    entry_points={
        "console_scripts":[
            "arpspector=ARPspector.arpspector:main"
        ],
    }

)