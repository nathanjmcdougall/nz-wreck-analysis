PYTHON_VERSION=$(cat .python-version | sed 's/\r//') &&
pyenv install $PYTHON_VERSION -s &&
pyenv shell $PYTHON_VERSION &&
(
    [[ -d ".venv" ]] ||
    python -m venv .venv
) &&
(
    source .venv/bin/activate || # Linux, MacOS
    .venv/Scripts/activate.bat # Windows
) &&
python -m ensurepip &&
python -m pip install --upgrade pip &&
pip install pip-tools &&
pip-sync requirements/requirements.txt &&
pre-commit install
