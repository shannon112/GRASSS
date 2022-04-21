tar="*.py src/*.py"
echo "==isort=="
isort --overwrite-in-place $tar
echo "==black=="
black $tar
echo "==pylint=="
pylint $tar
echo "==mypy=="
python3 -m mypy --disallow-untyped-defs --warn-unreachable --warn-redundant-casts --warn-unused-ignores --follow-imports silent --ignore-missing-imports $tar
