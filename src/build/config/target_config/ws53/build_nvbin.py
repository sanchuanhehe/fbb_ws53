#!/usr/bin/env python3
# encoding=utf-8
# ============================================================================
# @brief    Build nvbin
# Copyright HiSilicon (Shanghai) Technologies Co., Ltd. 2023-2023. All rights reserved.
# ============================================================================

import os
import sys
file_dir = os.path.dirname(os.path.realpath(__file__))
g_root = os.path.realpath(os.path.join(file_dir, "..", "..", "..", ".."))
sys.path.append(os.path.join(g_root, 'build', 'script', 'nv'))
from nv_binary import nv_begin


if __name__ == '__main__':
    #配置文件路径
    nv_config_json = os.path.join(g_root, "build", "config", "target_config", "ws53", "nv_bin_cfg", "mk_nv_bin_cfg.json")
    #输出路径
    build_root = os.path.abspath(os.environ.get("FBB_BUILD_ROOT_PATH", g_root))
    nv_output_path = os.path.join(build_root, "output", "ws53", "acore", "nv_bin")

    if not os.path.exists(nv_output_path):
        os.makedirs(nv_output_path)

    targets = ["acore"]
    nv_begin(nv_config_json, targets, 1, True, root=build_root, source_root=g_root)
