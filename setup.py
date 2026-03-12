from setuptools import setup, find_packages

setup(
    name="queryRouter",
    version="0.6.3",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "fastapi",
        "uvicorn",
        "typer",
        "pyyaml",
        "pydantic",
    ],
    entry_points={
        "console_scripts": [
            "qr=queryRouter.cli:app",
        ],
    },
)