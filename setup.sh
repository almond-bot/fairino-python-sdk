#!/bin/bash

INSTALL_PATH=$1

pip3 install cython setuptools

python3 setup.py build_ext --inplace

if [ -n "$INSTALL_PATH" ]; then
    BUILD_ARTIFACT=$(find . -name "*.so" | head -n 1)
    mv "$BUILD_ARTIFACT" "$INSTALL_PATH"
fi

