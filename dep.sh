rm -rfdv dist/* # remove existing builds
python3 -m build
python3 -m twine upload --repository pypi dist/*