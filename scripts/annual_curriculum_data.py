#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Target International School — Yillik Taqvim-Mavzu Rejasi (36 Hafta / 4 Chorak)
Rasmiy yagona ma'lumotlar bazasi (annual_curriculum_data.py).
"""

import json
import os

_DATA_FILE = os.path.join(os.path.dirname(__file__), 'annual_curriculum_data.json')
with open(_DATA_FILE, 'r', encoding='utf-8') as f:
    _d = json.load(f)

QUARTERS_INFO = _d['quarters']
VIBECODING_108_MASTER = _d['vibecoding_108']
ANNUAL_COHORTS_DATA = _d['cohorts']
