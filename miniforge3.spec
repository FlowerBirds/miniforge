%global version @VERSION@
Name:           miniforge3
Version:        %{version}
Release:        1%{?dist}
Summary:        Minimal installer for conda-forge's Miniforge3
License:        BSD-3-Clause
URL:            https://github.com/conda-forge/miniforge
Source0:        miniforge3-%{version}.tar.gz

%description
Miniforge3 is a minimal installer for conda-forge that provides a lightweight
environment for managing packages and dependencies. It is designed to work
with conda-forge channels and supports multiple CPU architectures.

%global __os_install_post /usr/lib/rpm/brp-compress %{nil}
%global _bytecompile 0
%global __debugedit %{nil}
%global __python_bytecompile %{nil}
%define __objdump /bin/true
%define _without_check 1
%define _binaries_in_noarch_packages_terminate_build 0
%define _use_internal_dependency_generator 0
%define debug_package %{nil}
%define __find_requires %{nil}
%define __find_provides %{nil}

%prep
%setup -q -n miniforge3

%build
# No compile needed

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/miniforge3
cp -r %{_builddir}/miniforge3/* %{buildroot}/usr/local/miniforge3/

%clean
rm -rf %{buildroot}

%files
/usr/local/miniforge3/*

%post
chmod -R 755 /usr/local/miniforge3

%changelog
* Tue Apr 28 2026 Build <build@example.com> %{version}-1
- Auto-built RPM from miniforge %{version}
- Installed to /usr/local/miniforge3
