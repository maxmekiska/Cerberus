from setuptools import setup

setup(
    author="Maximilian Mekiska",
    author_email="maxmekiska@gmail.com",
    url="https://github.com/maxmekiska/Cerberus",
    description="Standard and Hybrid Deep Learning Multivariate-Multi-Step & Univariate-Multi-Step Time Series Forecasting.",
    long_description=open("README.txt").read(),
    name="cerberus",
    version="0.1.0",
    install_rquires=[
        "tensorflow==2.9.1",
        "scikit-learn==0.21.3",
        "matplotlib==3.5.2",
        "numpy==1.21.6",
        "pandas==0.25.1",
    ],
    python_rquieres=">=3.7"
)
