#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : libass
Version  : 0.14.0
Release  : 7
URL      : file:///insilications/build/clearlinux/packages/libass/libass-0.14.0.tar.gz
Source0  : file:///insilications/build/clearlinux/packages/libass/libass-0.14.0.tar.gz
Summary  : LibASS is an SSA/ASS subtitles rendering library
Group    : Development/Tools
License  : BSD-3-Clause
Requires: libass-lib = %{version}-%{release}
BuildRequires : findutils
BuildRequires : fontconfig-dev
BuildRequires : fontconfig-staticdev
BuildRequires : freetype-dev
BuildRequires : freetype-staticdev
BuildRequires : fribidi-dev
BuildRequires : fribidi-staticdev
BuildRequires : harfbuzz-dev
BuildRequires : harfbuzz-staticdev
BuildRequires : libpng-dev
BuildRequires : libpng-staticdev
BuildRequires : nasm-bin
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(freetype2)
BuildRequires : pkgconfig(fribidi)
BuildRequires : pkgconfig(harfbuzz)
BuildRequires : pkgconfig(harfbuzz-gobject)
BuildRequires : pkgconfig(harfbuzz-icu)
BuildRequires : pkgconfig(harfbuzz-subset)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(libpng16)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
[![Build status](https://api.travis-ci.org/libass/libass.png)](https://travis-ci.org/libass/libass)

%package dev
Summary: dev components for the libass package.
Group: Development
Requires: libass-lib = %{version}-%{release}
Provides: libass-devel = %{version}-%{release}
Requires: libass = %{version}-%{release}

%description dev
dev components for the libass package.


%package lib
Summary: lib components for the libass package.
Group: Libraries

%description lib
lib components for the libass package.


%package staticdev
Summary: staticdev components for the libass package.
Group: Default
Requires: libass-dev = %{version}-%{release}

%description staticdev
staticdev components for the libass package.


%prep
%setup -q -n libass
cd %{_builddir}/libass

%build
unset http_proxy
unset https_proxy
unset no_proxy
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1598713587
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags_pgo content
## pgo generate
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage --coverage -fprofile-partial-training"
export CFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -fPIC -ffat-lto-objects -flto=16 $PGO_GEN"
export FCFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -fPIC -ffat-lto-objects -flto=16 $PGO_GEN"
export FFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -fPIC -ffat-lto-objects -flto=16 $PGO_GEN"
export CXXFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -fvisibility-inlines-hidden -pipe -fPIC -ffat-lto-objects -flto=16 $PGO_GEN"
export LDFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -fPIC -ffat-lto-objects -flto=16 $PGO_GEN"
## pgo use
## -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fpic -fvisibility=hidden
## gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common
export PGO_USE="-fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-correction -fprofile-partial-training"
export CFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fPIC -ffat-lto-objects -flto=16 $PGO_USE"
export FCFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fPIC -ffat-lto-objects -flto=16 $PGO_USE"
export FFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fPIC -ffat-lto-objects -flto=16 $PGO_USE"
export CXXFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -fPIC -ffat-lto-objects -flto=16 $PGO_USE"
export LDFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fPIC -ffat-lto-objects -flto=16 $PGO_USE"
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
#export CCACHE_DISABLE=1
## altflags_pgo end
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
%autogen --enable-shared --enable-static
make  %{?_smp_mflags}  V=1 VERBOSE=1

make -j16 VERBOSE=1 V=1 check
make clean
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
%autogen  --enable-shared --enable-static
make  %{?_smp_mflags}  V=1 VERBOSE=1


%check
export LANG=C.UTF-8
unset http_proxy
unset https_proxy
unset no_proxy
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1598713587
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/ass/ass.h
/usr/include/ass/ass_types.h
/usr/lib64/libass.so
/usr/lib64/pkgconfig/libass.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libass.so.9
/usr/lib64/libass.so.9.1.0

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libass.a
