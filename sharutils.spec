#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD9204CB5BFBF0221 (bkorb@gnu.org)
#
Name     : sharutils
Version  : 4.15.2
Release  : 15
URL      : https://mirrors.kernel.org/gnu/sharutils/sharutils-4.15.2.tar.xz
Source0  : https://mirrors.kernel.org/gnu/sharutils/sharutils-4.15.2.tar.xz
Source1  : https://mirrors.kernel.org/gnu/sharutils/sharutils-4.15.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-3.0 LGPL-3.0
Requires: sharutils-bin = %{version}-%{release}
Requires: sharutils-info = %{version}-%{release}
Requires: sharutils-license = %{version}-%{release}
Requires: sharutils-locales = %{version}-%{release}
Requires: sharutils-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : glibc-locale
BuildRequires : intltool-dev
Patch1: cve-2018-1000097.patch
Patch2: 0001-Porting-fseeko.c-from-gnulib.patch

%description
This is the set of GNU shar utilities.
"sharutils" is licensed under the terms of the GNU GPL version 3 (or, at your
option, any later version).

%package bin
Summary: bin components for the sharutils package.
Group: Binaries
Requires: sharutils-license = %{version}-%{release}

%description bin
bin components for the sharutils package.


%package info
Summary: info components for the sharutils package.
Group: Default

%description info
info components for the sharutils package.


%package license
Summary: license components for the sharutils package.
Group: Default

%description license
license components for the sharutils package.


%package locales
Summary: locales components for the sharutils package.
Group: Default

%description locales
locales components for the sharutils package.


%package man
Summary: man components for the sharutils package.
Group: Default

%description man
man components for the sharutils package.


%prep
%setup -q -n sharutils-4.15.2
cd %{_builddir}/sharutils-4.15.2
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664907328
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
%configure --disable-static CFLAGS="$CFLAGS -fcommon"
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1664907328
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sharutils
cp %{_builddir}/sharutils-%{version}/COPYING %{buildroot}/usr/share/package-licenses/sharutils/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/sharutils-%{version}/libopts/COPYING.gplv3 %{buildroot}/usr/share/package-licenses/sharutils/e8353ab286a6bcbb218d9df15d8aa68346ef5cf0 || :
cp %{_builddir}/sharutils-%{version}/libopts/COPYING.lgplv3 %{buildroot}/usr/share/package-licenses/sharutils/8ca3cbd336e9a13d5ee05753567d9261af4066a3 || :
cp %{_builddir}/sharutils-%{version}/libopts/COPYING.mbsd %{buildroot}/usr/share/package-licenses/sharutils/76f15ccf78ed039d563200c8db64f85d17c3d7cb || :
%make_install
%find_lang sharutils

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/shar
/usr/bin/unshar
/usr/bin/uudecode
/usr/bin/uuencode

%files info
%defattr(0644,root,root,0755)
/usr/share/info/sharutils.info

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sharutils/76f15ccf78ed039d563200c8db64f85d17c3d7cb
/usr/share/package-licenses/sharutils/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/sharutils/8ca3cbd336e9a13d5ee05753567d9261af4066a3
/usr/share/package-licenses/sharutils/e8353ab286a6bcbb218d9df15d8aa68346ef5cf0

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/shar.1
/usr/share/man/man1/unshar.1
/usr/share/man/man1/uudecode.1
/usr/share/man/man1/uuencode.1
/usr/share/man/man5/uuencode.5

%files locales -f sharutils.lang
%defattr(-,root,root,-)

