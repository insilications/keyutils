#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : keyutils
Version  : 1.6.1
Release  : 21
URL      : http://people.redhat.com/~dhowells/keyutils/keyutils-1.6.1.tar.bz2
Source0  : http://people.redhat.com/~dhowells/keyutils/keyutils-1.6.1.tar.bz2
Summary  : Linux Key Management Utilities
Group    : Development/Tools
License  : GPL-2.0+ LGPL-2.0+ LGPL-2.1+
Requires: keyutils-bin = %{version}-%{release}
Requires: keyutils-data = %{version}-%{release}
Requires: keyutils-lib = %{version}-%{release}
Requires: keyutils-man = %{version}-%{release}
BuildRequires : libc-bin
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Convert-to-stateless.patch

%description
Utilities to control the kernel key management facility and to provide
a mechanism by which the kernel call back to user space to get a key
instantiated.

%package bin
Summary: bin components for the keyutils package.
Group: Binaries
Requires: keyutils-data = %{version}-%{release}

%description bin
bin components for the keyutils package.


%package data
Summary: data components for the keyutils package.
Group: Data

%description data
data components for the keyutils package.


%package dev
Summary: dev components for the keyutils package.
Group: Development
Requires: keyutils-lib = %{version}-%{release}
Requires: keyutils-bin = %{version}-%{release}
Requires: keyutils-data = %{version}-%{release}
Provides: keyutils-devel = %{version}-%{release}
Requires: keyutils = %{version}-%{release}

%description dev
dev components for the keyutils package.


%package lib
Summary: lib components for the keyutils package.
Group: Libraries
Requires: keyutils-data = %{version}-%{release}

%description lib
lib components for the keyutils package.


%package man
Summary: man components for the keyutils package.
Group: Default

%description man
man components for the keyutils package.


%package staticdev
Summary: staticdev components for the keyutils package.
Group: Default
Requires: keyutils-dev = %{version}-%{release}

%description staticdev
staticdev components for the keyutils package.


%prep
%setup -q -n keyutils-1.6.1
cd %{_builddir}/keyutils-1.6.1
%patch1 -p1

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1630130904
export GCC_IGNORE_WERROR=1
## altflags1 content
export CFLAGS="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
## -fno-tree-vectorize: disable -ftree-vectorize thus disable -ftree-loop-vectorize and -ftree-slp-vectorize
## -Ofast -ffast-math
## -funroll-loops maybe dangerous
## -Wl,-z,max-page-size=0x1000
## -pthread -lpthread
## -Wl,-Bsymbolic-functions
export CXXFLAGS="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
#
export FCFLAGS="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
export FFLAGS="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
export CFFLAGS="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
#
export LDFLAGS="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
#%global _disable_maintainer_mode %{nil}
#
export CCACHE_DISABLE=true
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
#
export LD_LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/haswell/pulseaudio:/usr/lib64/haswell/alsa-lib:/usr/lib64/haswell/gstreamer-1.0:/usr/lib64/haswell/pipewire-0.3:/usr/lib64/haswell/spa-0.2:/usr/lib64/dri:/usr/lib64/chromium:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/haswell/pulseaudio:/usr/lib64/haswell/alsa-lib:/usr/lib64/haswell/gstreamer-1.0:/usr/lib64/haswell/pipewire-0.3:/usr/lib64/haswell/spa-0.2:/usr/lib64/dri:/usr/lib64/chromium:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export PATH="/usr/lib64/ccache/bin:/usr/local/cuda/bin:/usr/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
#
export CPATH="/usr/local/cuda/include"
#
export DISPLAY=:0
export __GL_SYNC_TO_VBLANK=0
export __GL_SYNC_DISPLAY_DEVICE=DFP-1
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=DFP-1
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH=/usr/share/defaults/fonts
## altflags1 end
make  %{?_smp_mflags}    V=1 VERBOSE=1 CFLAGS="${CFLAGS}" CXXFLAGS="${CXXFLAGS}" FFLAGS="${FFLAGS}" FCFLAGS="${FCFLAGS}" LDFLAGS="${LDFLAGS}" LIBS="${LIBS}"


%install
export SOURCE_DATE_EPOCH=1630130904
rm -rf %{buildroot}
%make_install LIBDIR=%{_libdir} USRLIBDIR=%{_libdir}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/key.dns_resolver
/usr/bin/keyctl
/usr/bin/request-key

%files data
%defattr(-,root,root,-)
/usr/share/keyutils/request-key-debug.sh
/usr/share/keyutils/request-key.conf

%files dev
%defattr(-,root,root,-)
/usr/include/keyutils.h
/usr/lib64/libkeyutils.so
/usr/lib64/pkgconfig/libkeyutils.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libkeyutils.so.1
/usr/lib64/libkeyutils.so.1.9

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/keyctl.1
/usr/share/man/man3/find_key_by_type_and_name.3
/usr/share/man/man3/keyctl.3
/usr/share/man/man3/keyctl_assume_authority.3
/usr/share/man/man3/keyctl_capabilities.3
/usr/share/man/man3/keyctl_chown.3
/usr/share/man/man3/keyctl_clear.3
/usr/share/man/man3/keyctl_describe.3
/usr/share/man/man3/keyctl_describe_alloc.3
/usr/share/man/man3/keyctl_dh_compute.3
/usr/share/man/man3/keyctl_dh_compute_alloc.3
/usr/share/man/man3/keyctl_dh_compute_kdf.3
/usr/share/man/man3/keyctl_get_keyring_ID.3
/usr/share/man/man3/keyctl_get_persistent.3
/usr/share/man/man3/keyctl_get_security.3
/usr/share/man/man3/keyctl_get_security_alloc.3
/usr/share/man/man3/keyctl_instantiate.3
/usr/share/man/man3/keyctl_instantiate_iov.3
/usr/share/man/man3/keyctl_invalidate.3
/usr/share/man/man3/keyctl_join_session_keyring.3
/usr/share/man/man3/keyctl_link.3
/usr/share/man/man3/keyctl_move.3
/usr/share/man/man3/keyctl_negate.3
/usr/share/man/man3/keyctl_pkey_decrypt.3
/usr/share/man/man3/keyctl_pkey_encrypt.3
/usr/share/man/man3/keyctl_pkey_query.3
/usr/share/man/man3/keyctl_pkey_sign.3
/usr/share/man/man3/keyctl_pkey_verify.3
/usr/share/man/man3/keyctl_read.3
/usr/share/man/man3/keyctl_read_alloc.3
/usr/share/man/man3/keyctl_reject.3
/usr/share/man/man3/keyctl_restrict_keyring.3
/usr/share/man/man3/keyctl_revoke.3
/usr/share/man/man3/keyctl_search.3
/usr/share/man/man3/keyctl_session_to_parent.3
/usr/share/man/man3/keyctl_set_reqkey_keyring.3
/usr/share/man/man3/keyctl_set_timeout.3
/usr/share/man/man3/keyctl_setperm.3
/usr/share/man/man3/keyctl_unlink.3
/usr/share/man/man3/keyctl_update.3
/usr/share/man/man3/recursive_key_scan.3
/usr/share/man/man3/recursive_session_key_scan.3
/usr/share/man/man5/request-key.conf.5
/usr/share/man/man7/asymmetric-key.7
/usr/share/man/man7/keyutils.7
/usr/share/man/man8/key.dns_resolver.8
/usr/share/man/man8/request-key.8

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libkeyutils.a
