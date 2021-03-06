from setuptools import setup, find_packages

setup(
    author="Maximilian Mekiska",
    author_email="maxmekiska@gmail.com",
    url="https://github.com/maxmekiska/Cerberus",
    description="Standard and Hybrid Deep Learning Multivariate-Multi-Step & Univariate-Multi-Step Time Series Forecasting.",
    name="cerberus",
    version="0.1.0",
    packages = find_packages(include=["cerberus", "cerberus.*"]),
    install_requires=[
        "tensorflow==2.9.1",
        "scikit-learn==0.21.3",
        "matplotlib==3.5.2",
        "numpy==1.21.6",
        "pandas==0.25.1",
    ],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: Microsoft :: Windows 10",
    ],
    keywords = ["machineleaning", "keras", "deeplearning", "timeseries", "forecasting"],
    python_rquieres=">=3.7"
)
