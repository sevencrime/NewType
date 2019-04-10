#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-10 17:14:54
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

import os
import glob
modules = glob.glob(os.path.dirname(os.path.abspath(__file__))+"/*.py")
__all__ = [ os.path.basename(f)[:-3] for f in modules]

