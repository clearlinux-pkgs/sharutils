#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sharutils
Version  : 4.15.2
Release  : 3
URL      : ftp://ftp.gnu.org/gnu/sharutils/sharutils-4.15.2.tar.xz
Source0  : ftp://ftp.gnu.org/gnu/sharutils/sharutils-4.15.2.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.3 GPL-3.0 LGPL-3.0
Requires: sharutils-bin
Requires: sharutils-doc
Requires: sharutils-locales
BuildRequires : bison

%description
This is the set of GNU shar utilities.
"sharutils" is licensed under the terms of the GNU GPL version 3 (or, at your
option, any later version).

%package bin
Summary: bin components for the sharutils package.
Group: Binaries

%description bin
bin components for the sharutils package.


%package doc
Summary: doc components for the sharutils package.
Group: Documentation

%description doc
doc components for the sharutils package.


%package locales
Summary: locales components for the sharutils package.
Group: Default

%description locales
locales components for the sharutils package.


%prep
%setup -q -n sharutils-4.15.2

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
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

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*

%files locales -f sharutils.lang 
%defattr(-,root,root,-)

