# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This repository builds Miniforge3 RPM packages with pre-installed Python dependencies. Four workflows target different platforms.

## Workflows

| File | Trigger Name | Container | Target |
|------|--------------|------------|--------|
| `build-rpm.yml` | CentOS 7 | centos:7 | CentOS 7 x86_64 |
| `build-rpm-rocky8.yml` | Rocky Linux 8 | rockylinux:8 | Rocky Linux 8 x86_64 |
| `build-rpm-rocky8-arm64.yml` | Rocky Linux 8 ARM64 | rockylinux:8 | Rocky Linux 8 aarch64 |
| `build-rpm-latest.yml` | Latest | rockylinux:8 | Rocky Linux 8, auto-latest miniforge |

## Key Points

- **Installation path:** `/usr/local/miniforge3` for all workflows
- **RPM build directory:** `/github/home/.rpmbuild` (GitHub Actions container)
- **Important:** When passing `--define "_topdir"` to rpmbuild, do NOT use `~`. Use absolute path instead (e.g., `/github/home/.rpmbuild`). The `~` tilde does not expand inside `--define` arguments.
- **Version naming:** RPM Version field uses `_` instead of `-` (e.g., `26.1.1-3` → `26.1.1_3`)
- **Spec files:** `miniforge3.spec` for versioned builds, `miniforge3-latest.spec` for Latest workflow
- **Commit messages:** Must NOT include `Co-Authored-By` trailers

## Requirements Files

| File | Purpose |
|------|---------|
| `requirements.txt` | Fixed versions for versioned builds |
| `requirements-latest.txt` | Latest versions for Latest workflow |

## Local Build (if applicable)

```bash
# Setup RPM build directory
mkdir -p ~/.rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS,BUILDROOT}

# Build RPM
rpmbuild -bb miniforge3.spec --define "_topdir ~/.rpmbuild" --define "version 26.1.1_3"
```