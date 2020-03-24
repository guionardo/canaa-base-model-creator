#!/bin/bash
rm -r ./dist
rm -r ./build
rm -r ./canaa_model_furlan.egg-info
rm -r /home/guionardo/.local/share/virtualenvs/canaa-base-model-creator-1Ro1u9l0/lib/python3.6/site-packages/canaa_base_model_creator-0.0.1-py3.6.egg
python setup.py install
