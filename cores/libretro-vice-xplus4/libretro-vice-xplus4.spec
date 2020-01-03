#
# spec file for package libretro-vice-xplus4
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


Name:           libretro-vice-xplus4
Version:        1.0
Release:        0
Summary:        vice_xplus4 libretro core
License:        GPL-3.0
URL:            http://www.retroarch.com
Source:         %{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  make

%description
vice_xplus4 libretro core

%prep
%setup -q

%build
make EMUTYPE=xplus4

%install
mkdir -p %{buildroot}%{_libdir}/libretro
cp vice_xplus4_libretro.so %{buildroot}%{_libdir}/libretro

%files
%dir %{_libdir}/libretro
%{_libdir}/libretro/vice_xplus4_libretro.so

%changelog
