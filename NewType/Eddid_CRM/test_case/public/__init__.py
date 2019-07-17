#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import os

modules = glob.glob(os.path.dirname(os.path.abspath(__file__))+"/*.py")
__all__ = [ os.path.basename(f)[:-3] for f in modules]

# print(__all__)