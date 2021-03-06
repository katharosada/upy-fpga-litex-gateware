#!/bin/bash

# Settings for the download-env.sh and setup-env.sh scripts

PLATFORM=${PLATFORM:-opsis}

BUILD_DIR=$TOP_DIR/build
THIRD_DIR=$TOP_DIR/third_party
CONDA_DIR=$BUILD_DIR/conda

# Python module versions
HDMI2USB_MODESWITCH_VERSION=0.0.0
HEXFILE_VERSION=0.1

# Conda package versions
BINUTILS_VERSION=2.26
GCC_VERSION=4.9.3
SDCC_VERSION=3.5.0
OPENOCD_VERSION=0.10.0-dev

# lite modules
LITE_REPOS="
	litex
	litedram
	liteeth
	litepcie
	litesata
	litescope
	liteusb
	litevideo
	"
