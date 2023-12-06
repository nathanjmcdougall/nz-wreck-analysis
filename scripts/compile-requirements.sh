# Development
pip-compile \
    --extra dev \
    --extra check \
    --extra test \
    --extra doc \
    --extra notebook \
    --extra profile \
    --extra viz \
    --unsafe-package=pywin32 \
    --unsafe-package=pip \
    --unsafe-package=distribute \
    --unsafe-package=setuptools \
    --output-file="requirements/requirements.txt" \
    --resolver=backtracking \
    --quiet \
    --strip-extras \
    "pyproject.toml"

# CI
pip-compile \
    --extra check \
    --extra test \
    --unsafe-package=pywin32 \
    --unsafe-package=pip \
    --unsafe-package=distribute \
    --unsafe-package=setuptools \
    --output-file="requirements/ci-requirements.txt" \
    --resolver=backtracking \
    --quiet \
    --strip-extras \
    "pyproject.toml"
