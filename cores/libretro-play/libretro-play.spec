#
# spec file for package libretro-play
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


Name:           libretro-play
Version:        1.0
Release:        0
Summary:        play libretro core
License:        GPL-3.0
URL:            http://www.retroarch.com
Source:         %{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
play libretro core

%prep
%setup -q

%build
cd build
mkdir build
 cd build
cmake .. -DBUILD_LIBRETRO_CORE=yes -DBUILD_PLAY=off -DBUILD_TESTS=no -DENABLE_AMAZON_S3=no -DCMAKE_BUILD_TYPE="Release" --target play_libretro
make

%install
mkdir -p %{buildroot}%{_libdir}/libretro
cp build/build/play_libretro.so %{buildroot}%{_libdir}/libretro

%files
%dir %{_libdir}/libretro
%{_libdir}/libretro/play_libretro.so

%changelog
