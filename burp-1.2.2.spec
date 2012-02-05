Name: burp
Version: 1.2.2
Release: 1%{?dist}
License: AGPLv3
URL: http://burp.grke.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: librsync-devel openssl-devel zlib-devel gcc make gcc-c++
Source0: http://downloads.sourceforge.net/project/burp/burp-1.2.2%20%28stable%29/burp-1.2.2.tar.bz2
Summary: BackUp and Restore Program
Group: System/Backup
Provides: burp = 1.2.2

%description
Burp is a network backup and restore program. It uses librsync in order to save network traffic and to save on the amount of space that is used by each backup. It also uses VSS (Volume Shadow Copy Service) to make snapshots when backing up Windows computers.

%prep
%setup -n burp-1.2.2

%build
export CFLAGS="$RPM_OPT_FLAGS -Wall"

%configure --libdir=%{_libdir}

make %{?_smp_mflags}
%install
# installing binaries ...
make install DESTDIR=$RPM_BUILD_ROOT

# we don't want to keep the src directory
rm -rf $RPM_BUILD_ROOT/usr/src

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_sbindir}
%{_datadir}
%{_sysconfdir}
%{_localstatedir}

%changelog
* Sun Feb 05 2012 Alice Kaerast <alice.kaerast@webanywhere.co.uk> - 1.2.2
- Initial Build