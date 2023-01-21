from setuptools import setup


def read_requires(file_path: str):
    with open(file_path, "r") as file:
        return file.read().splitlines()



setup(
    name='Crop Fragment',
    version='1.0.0',
    description='Cuts off the selected fragment from the image',
    author='NBuhsx',
    author_email='sergey33sergey@yandex.com',
    url="https://notabug.org/NBuhsx/Crop Fragment",
    packages=["cropp_fragment"],
    install_requires=read_requires("requirements.txt")
)