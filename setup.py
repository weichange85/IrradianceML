import setuptools

REPO_NAME = "IrradianceML"
AUTHOR_USER_NAME = "wei.chang85"
SRC_REPP = "IrRegressionPrediction"
AUTHOR_EMAIL = "wei.chang85@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version="0.1.0",
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small package for IrRegression App",
    long_description=open('README.md').read(),  # Use your README file for a detailed description
    long_description_content_type='text/markdown',
    url=f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")  # Automatically find packages in the project
)