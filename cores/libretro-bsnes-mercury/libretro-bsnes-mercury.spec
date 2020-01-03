#
# spec file for package libretro-bsnes-mercury
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


Name:           libretro-bsnes-mercury
Version:        1.0
Release:        0
Summary:        bsnes_mercury libretro core
License:        GPL-3.0
URL:            http://www.retroarch.com
Source:         %{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  make

%description
bsnes_mercury libretro core

%prep
%setup -q

%build
make | bsnes_mercury_accuracy:profile=accuracy bsnes_mercury_balanced:profile=balanced bsnes_mercury_performance:profile=performance

%install
mkdir -p %{buildroot}%{_libdir}/libretro
cp bsnes_mercury_libretro.so %{buildroot}%{_libdir}/libretro

%files
%dir %{_libdir}/libretro
%{_libdir}/libretro/bsnes_mercury_libretro.so

%changelog
