import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
        name="rock_paper_scissors",
        version="0.0.2",
        author="Rahul Bawa",
        author_email="hi.rahulbawa@gmail.com",
        description="A RL environment for rock paper scissors(deterministic)  based on openai",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/raul1991/rock-paper-scissors-RL",
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent"
        ],
        install_requires=['gym', 'numpy']
)
