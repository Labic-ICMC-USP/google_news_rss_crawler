from setuptools import setup, find_packages

setup(
    name="google-news-rss-crawler",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "feedparser",
        "pandas",
        "tqdm",
        "python-dateutil",
        "pyarrow"
    ],
    entry_points={
        "console_scripts": [
            "google-news-crawler = scripts.run_crawler:main"
        ]
    }
)
