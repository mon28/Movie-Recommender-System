import setuptools

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

__version__ = "0.0.1"

REPO_NAME = "Movie-Recommender-System"
AUTHOR_USER_NAME = "mon28"
SRC_REPO = "movieRecommenderSystem"
AUTHOR_EMAIL = "monicatare28@gmail.com"
LIST_OF_REQUIREMENTS = ['streamlit']

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Movie Recommender System: a small python package for recommending movies based on search query.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires='>=3.8',
    install_requires=LIST_OF_REQUIREMENTS
)