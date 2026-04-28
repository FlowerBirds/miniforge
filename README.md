# Miniforge3 RPM Builder

[![GitHub release](https://img.shields.io/github/v/release/conda-forge/miniforge?style=for-the-badge&sort=semver)](https://github.com/conda-forge/miniforge/releases)

基于 GitHub Actions 构建 Miniforge3 RPM 安装包，支持 CentOS 7 / Rocky Linux 8 / ARM64 等平台。

## 支持的平台

| Workflow | 触发名称 | 架构 | 目标系统 | 特点 |
|-----------|----------|------|----------|------|
| Build RPM Package | CentOS 7 | x86_64 | CentOS 7 | 指定版本 |
| Build RPM Package (CentOS 8) | Rocky Linux 8 | x86_64 | Rocky Linux 8 | 指定版本 |
| Build RPM Package (CentOS 8 ARM64) | Rocky Linux 8 ARM64 | aarch64 | Rocky Linux 8 ARM64 | 指定版本 |
| Build RPM Package (Latest) | Latest | x86_64 | Rocky Linux 8 | 自动获取最新版本 + 最新依赖 |

## 安装目录

- 指定版本构建：`/usr/local/miniforge3`
- Latest 构建：`/usr/local/miniforge3-latest`

## 使用方法

### 1. GitHub Actions 构建

1. 进入仓库 **Actions** 页面
2. 选择对应的 Workflow
3. 点击 **Run workflow**
4. （指定版本 workflow）输入 Miniforge 版本（如 `26.1.1-3`）
5. （Latest workflow）自动获取最新版本，无需手动输入
6. 构建完成后 RPM 自动发布到 Release

### 2. 本地安装 RPM

```bash
# CentOS 7
sudo rpm -ivh miniforge3-{version}-1.el7.x86_64.rpm

# Rocky Linux 8
sudo rpm -ivh miniforge3-{version}-1.el8.x86_64.rpm

# Rocky Linux 8 ARM64
sudo rpm -ivh miniforge3-{version}-1.el8.aarch64.rpm
```

或使用 dnf 安装：

```bash
sudo dnf localinstall miniforge3-{version}-1.el8.x86_64.rpm
```

## Miniforge 版本

从 [conda-forge/miniforge releases](https://github.com/conda-forge/miniforge/releases) 获取可用版本。

## Python 依赖

| 文件 | 说明 |
|------|------|
| `requirements.txt` | 固定版本依赖（用于指定版本构建） |
| `requirements-latest.txt` | 最新版本依赖（用于 Latest 构建） |

## 本地构建

```bash
# 安装依赖
yum -y install rpm-build rpmdevtools tar gzip wget

# 下载 Miniforge
MINIFORGE_VERSION="26.1.1-3"
wget "https://github.com/conda-forge/miniforge/releases/download/${MINIFORGE_VERSION}/Miniforge3-${MINIFORGE_VERSION}-Linux-x86_64.sh"

# 安装
bash Miniforge3-${MINIFORGE_VERSION}-Linux-x86_64.sh -b -p /usr/local/miniforge3

# 安装 Python 依赖
/usr/local/miniforge3/bin/pip install -r requirements.txt

# 构建 RPM
rpmdev-setuptree
mkdir -p ~/rpmbuild/SOURCES/miniforge3-${MINIFORGE_VERSION}
cp -r /usr/local/miniforge3/* ~/rpmbuild/SOURCES/miniforge3-${MINIFORGE_VERSION}/
rpmbuild -bb miniforge3.spec --define "_topdir $HOME/rpmbuild" --define "version ${MINIFORGE_VERSION}"
```
