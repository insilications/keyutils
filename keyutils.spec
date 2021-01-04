#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : keyutils
Version  : 1.6.1
Release  : 20
URL      : http://people.redhat.com/~dhowells/keyutils/keyutils-1.6.1.tar.bz2
Source0  : http://people.redhat.com/~dhowells/keyutils/keyutils-1.6.1.tar.bz2
Summary  : Linux Key Management Utilities
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ LGPL-2.0+ LGPL-2.1 LGPL-2.1+
Requires: keyutils-bin = %{version}-%{release}
Requires: keyutils-data = %{version}-%{release}
Requires: keyutils-lib = %{version}-%{release}
Requires: keyutils-license = %{version}-%{release}
Requires: keyutils-man = %{version}-%{release}
BuildRequires : libc-bin
Patch1: 0001-Convert-to-stateless.patch

%description
Utilities to control the kernel key management facility and to provide
a mechanism by which the kernel call back to user space to get a key
instantiated.

%package bin
Summary: bin components for the keyutils package.
Group: Binaries
Requires: keyutils-data = %{version}-%{release}
Requires: keyutils-license = %{version}-%{release}

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
Requires: keyutils-license = %{version}-%{release}

%description lib
lib components for the keyutils package.


%package license
Summary: license components for the keyutils package.
Group: Default

%description license
license components for the keyutils package.


%package man
Summary: man components for the keyutils package.
Group: Default

%description man
man components for the keyutils package.


%prep
%setup -q -n keyutils-1.6.1
cd %{_builddir}/keyutils-1.6.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1609782208
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1609782208
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/keyutils
cp %{_builddir}/keyutils-1.6.1/LICENCE.GPL %{buildroot}/usr/share/package-licenses/keyutils/60a58d43fa778820234a8e9d33a6b58ce8d7fe75
cp %{_builddir}/keyutils-1.6.1/LICENCE.LGPL %{buildroot}/usr/share/package-licenses/keyutils/1c39e1d1004475e1237555e21dc8e0a3b70d3ff1
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

%files lib
%defattr(-,root,root,-)
/usr/lib64/libkeyutils.so.1
/usr/lib64/libkeyutils.so.1.9

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/keyutils/1c39e1d1004475e1237555e21dc8e0a3b70d3ff1
/usr/share/package-licenses/keyutils/60a58d43fa778820234a8e9d33a6b58ce8d7fe75

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/keyctl.1
/usr/share/man/man5/request-key.conf.5
/usr/share/man/man7/asymmetric-key.7
/usr/share/man/man7/keyutils.7
/usr/share/man/man8/key.dns_resolver.8
/usr/share/man/man8/request-key.8
