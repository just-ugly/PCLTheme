from setuptools import setup, find_packages

setup(
    name="PCLTheme",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    author="just-ugly",
    author_email="just_ugly@163.com",
    description="""
    该项目可以让你方便的使用 python 语言设计 PCL 主页。
    """,
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="",
    classifiers=[
        "Programming language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ]
)