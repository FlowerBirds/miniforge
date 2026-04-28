# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This repository builds an RPM package that installs Miniforge3 (conda-forge's minimal Python installer) with pre-installed Python dependencies. The package is target for **CentOS 7** compatibility.

## Repository Structure

- `.github/workflows/build-rpm.yml` - GitHub Actions workflow for RPM building
- `miniforge3.spec` - RPM spec file, installs to `/usr/local/miniforge3`
- `requirements.txt` - Python dependencies to install into the Miniforge environment

## Building RPM

### Manual Build (local)

```bash
# Install dependencies
yum -y install rpm-build rpmdevtools tar gzip wget

# Setup RPM build tree
rpmdev-setuptree

# Download and extract miniforge
MINIFORGE_VERSION="24.7.1-0"
wget "https://github.com/conda-forge/miniforge/releases/download/${MINIFORGE_VERSION}/Miniforge3-${MINIFORGE_VERSION}-Linux-x86_64.sh"
bash Miniforge3-${MINIFORGE_VERSION}-Linux-x86_64.sh -b -p /usr/local/miniforge3

# Install Python dependencies
/usr/local/miniforge3/bin/pip install -r requirements.txt

# Copy to RPM build root
mkdir -p ~/rpmbuild/SOURCES/miniforge3-${MINIFORGE_VERSION}
cp -r /usr/local/miniforge3/* ~/rpmbuild/SOURCES/miniforge3-${MINIFORGE_VERSION}/

# Build RPM
rpmbuild -bb miniforge3.spec --define "_topdir $HOME/rpmbuild" --define "version ${MINIFORGE_VERSION}"
```

### GitHub Actions Build

1. Go to Actions tab → "Build RPM Package" → "Run workflow"
2. Enter `miniforge_version` (e.g., `24.7.1-0`)
3. RPM is published to GitHub Release automatically

## Notes

- Build runs in `centos:7` container for CentOS 7 compatibility
- Spec file uses `%{version}` macro - passed via `--define "version X"`
- Python dependencies are installed into Miniforge **before** packaging
- Commit messages must NOT include `Co-Authored-By` trailers
