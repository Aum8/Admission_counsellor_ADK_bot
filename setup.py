from setuptools import setup, find_packages

setup(
    name="admission_counselor",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "google-adk",
        "pandas",
        "openpyxl",
        "cloudpickle",
        "pydantic",
        "google-cloud-aiplatform",
        "google-cloud-aiplatform-aiplatform",
        "google-cloud-aiplatform-aiplatform-aiplatform",
        "google-cloud-aiplatform-aiplatform-aiplatform",
    ],
)