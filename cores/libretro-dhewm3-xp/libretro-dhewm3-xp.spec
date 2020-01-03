#
# spec file for package libretro-dhewm3-xp
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


Name:           libretro-dhewm3-xp
Version:        1.0
Release:        0
Summary:        dhewm3_xp libretro core
License:        GPL-3.0
URL:            http://www.retroarch.com
Source:         %{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  make

%description
dhewm3_xp libretro core

%prep
%setup -q

%build
cd neo
make D3XP=ON

%install
mkdir -p %{buildroot}%{_libdir}/libretro
cp neo/dhewm3_xp_libretro.so %{buildroot}%{_libdir}/libretro

%files
%dir %{_libdir}/libretro
%{_libdir}/libretro/dhewm3_xp_libretro.so

%changelog
