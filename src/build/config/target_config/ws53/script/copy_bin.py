#!/usr/bin/env python3
# coding=utf-8

import subprocess
import os
import sys
import shutil
import platform
import tarfile
import subprocess


root_dir = sys.argv[1]
target_name = sys.argv[2]
output_root = os.path.abspath(sys.argv[3]) if len(sys.argv) > 3 else os.path.join(root_dir, 'output')

ws53_output = os.path.join(output_root, 'ws53')
ssb=os.path.join(ws53_output, 'acore', 'ws53-ssb', 'ssb_sign.bin')
ssb_bin=os.path.join(ws53_output, 'acore', 'ws53-ssb', 'ssb.bin')
flashboot_a=os.path.join(ws53_output, 'acore', 'ws53-flashboot', 'flashboot_sign.bin')
flashboot_bin=os.path.join(ws53_output, 'acore', 'ws53-flashboot', 'flashboot.bin')
flashboot_b=os.path.join(ws53_output, 'acore', 'ws53-flashboot', 'flashboot_backup_sign.bin')
loaderboot=os.path.join(ws53_output, 'acore', 'ws53-loaderboot', 'loaderboot_sign.bin')
loaderboot_bin=os.path.join(ws53_output, 'acore', 'ws53-loaderboot', 'loaderboot.bin')
param_bin=os.path.join(ws53_output, 'acore', 'param_bin', 'root_params_sign.bin')
pke_rom=os.path.join(ws53_output, 'acore', 'pke_rom', 'pke_rom.bin')
romboot=os.path.join(ws53_output, 'acore', 'ws53-romboot', 'romboot.bin')
sdk_ccore_app=os.path.join(ws53_output, 'control_core', 'ws53_control_app', 'control_ws53.bin')
sdk_ccore_app_lite=os.path.join(ws53_output, 'control_core', 'ws53_control_app_lite', 'control_ws53_lite.bin')
efuse_bin=os.path.join(ws53_output, 'acore', 'ws53_liteos_app', 'efuse_cfg.bin')
bootbin=os.path.join(root_dir, 'interim_binary', 'ws53', 'bin', 'boot_bin')
ccore_src_hdb=os.path.join(ws53_output, 'build_hso_cfg', 'hso_database', 'xml', 'base', 'control_core')
ccore_dst_hdb=os.path.join(root_dir, 'interim_binary', 'ws53', 'ccore', 'build_hso_cfg', 'hso_database', 'xml', 'base')

current_path = os.getcwd()

print(f"==========1target:{current_path}")
cwd_path = os.path.split(os.path.realpath(__file__))[0]
os.chdir(cwd_path)

if not os.path.exists(bootbin):
    os.mkdir(bootbin)

if os.path.isfile(ssb) and os.path.isfile(os.path.join(bootbin, "ssb_sign.bin")):
    shutil.copy(ssb, bootbin)

if os.path.isfile(ssb_bin) and os.path.isfile(os.path.join(bootbin, "ssb.bin")):
    shutil.copy(ssb_bin, bootbin)

if os.path.isfile(flashboot_bin) and os.path.isfile(os.path.join(bootbin, "flashboot.bin")):
    shutil.copy(flashboot_bin, bootbin)

if os.path.isfile(loaderboot_bin) and os.path.isfile(os.path.join(bootbin, "loaderboot.bin")):
    shutil.copy(loaderboot_bin, bootbin)

if os.path.isfile(flashboot_a) and os.path.isfile(os.path.join(bootbin, "flashboot_sign.bin")):
    shutil.copy(flashboot_a, bootbin)

if os.path.isfile(flashboot_b) and os.path.isfile(os.path.join(bootbin, "flashboot_backup_sign.bin")):
    shutil.copy(flashboot_b, bootbin)

if os.path.isfile(loaderboot) and os.path.isfile(os.path.join(bootbin, "loaderboot_sign.bin")):
    shutil.copy(loaderboot, bootbin)

if os.path.isfile(param_bin) and os.path.isfile(os.path.join(bootbin, "root_params_sign.bin")):
    shutil.copy(param_bin, bootbin)

if os.path.isfile(sdk_ccore_app_lite) and os.path.isfile(os.path.join(bootbin, "control_ws53_lite.bin")):
    shutil.copy(sdk_ccore_app_lite, bootbin)
