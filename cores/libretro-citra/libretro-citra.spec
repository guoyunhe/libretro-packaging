#
# spec file for package libretro-citra
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


Name:           libretro-citra
Version:        1.0
Release:        0
Summary:        citra libretro core
License:        GPL-3.0
URL:            http://www.retroarch.com
Source:         %{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
citra libretro core

%prep
%setup -q

%build
cd build
mkdir build
 cd build
cmake .. -DCMAKE_CXX_COMPILER=g++-7 -DCMAKE_C_COMPILER=gcc-7 -DENABLE_LIBRETRO=1 -DLIBRETRO_STATIC=1 -DENABLE_SDL2=0 -DENABLE_QT=0 -DCMAKE_BUILD_TYPE="Release" -DENABLE_WEB_SERVICE=0 --target citra_libretro
make

%install
mkdir -p %{buildroot}%{_libdir}/libretro
cp build/build/citra_libretro.so %{buildroot}%{_libdir}/libretro

%files
%dir %{_libdir}/libretro
%{_libdir}/libretro/citra_libretro.so

%changelog
