import setuptools
with open("README.md", 'r', encoding='utf-8') as f:
    long_description = f.read()

__version__ = '0.0.0'

REPO_NAME= "text-summarization-project"
AUTHOR_USER_NAME = "nakibworkspace"
SRC_REPO= "TextSummarizer"
AUTHOR_EMAIL = "rajnakib2003@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A text summarization project using BERT and Hugging Face Transformers",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/" + AUTHOR_USER_NAME + "/" + REPO_NAME,
    project_url={
        "BugTracker": "https://github.com/" + AUTHOR_USER_NAME + "/" + REPO_NAME + "/"+ "issues",
    },
    package_dir= {"": "src"},
    packages= setuptools.find_packages(where="src")
)