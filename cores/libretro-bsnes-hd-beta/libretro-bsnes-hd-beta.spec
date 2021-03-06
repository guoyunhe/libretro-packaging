#
# spec file for package libretro-bsnes-hd-beta
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           libretro-bsnes-hd-beta
Version:        1.0
Release:        0
Summary:        bsnes_hd_beta libretro core
License:        GPL-3.0
URL:            http://www.retroarch.com
Source:         %{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  make

%description
bsnes_hd_beta libretro core

%prep
%setup -q

%build
cd bsnes
make -f GNUmakefile compiler=g++-7 target=libretro binary=library local=false platform=linux

%install
mkdir -p %{buildroot}%{_libdir}/libretro
cp bsnes/bsnes_hd_beta_libretro.so %{buildroot}%{_libdir}/libretro

%files
%dir %{_libdir}/libretro
%{_libdir}/libretro/bsnes_hd_beta_libretro.so

%changelog
