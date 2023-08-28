import setuptools

description = open("./README.md", "r", encoding="utf-8")

setuptools.setup(
    name="apiperu",
    version="0.0.1",
    description="API de los 24 departamentos del Perú",
    long_description=description,
    long_description_content_type='text/markdown',
    url='https://github.com/brianinhu/apiperu',
    download_url='https://github.com/brianinhu/apiperu/releases/tag/0.0.1',
    keywords=['testing', 'logging', 'example'],
    classifiers=[ ],
    include_package_data=True
)
