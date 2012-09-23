Name: burp
Version: 1.3.12
Release: 1%{?dist}
License: AGPLv3
URL: http://burp.grke.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: librsync-devel openssl-devel zlib-devel gcc make gcc-c++ ncurses-devel
Source0: burp-1.3.12.tar.bz2
Source1: burp
Patch0: burp_ca.diff
Summary: BackUp and Restore Program
Group: Applications/Archiving
Requires(post): chkconfig
Requires(preun): chkconfig
# This is for /sbin/service
Requires(preun): initscripts

%description
Burp is a network backup and restore program. It uses librsync in order
to save network traffic and to save on the amount of space that is used
by each backup. It also uses VSS (Volume Shadow Copy Service) to make
snapshots when backing up Windows computers.

%prep
%setup -n burp
%patch0 -p1

%build
export CFLAGS="$RPM_OPT_FLAGS -Wall"

%configure --libdir=%{_libdir} --sysconfdir=%{_sysconfdir}/burp

make %{?_smp_mflags}
%install
# installing binaries ...
make install DESTDIR=$RPM_BUILD_ROOT
install -d -m 0755 %{buildroot}%{_initddir}
install -m 0755 %{SOURCE1} %{buildroot}%{_initddir}

# we don't want to keep the src directory
rm -rf $RPM_BUILD_ROOT/usr/src

%clean
rm -rf $RPM_BUILD_ROOT

%post
# This adds the proper /etc/rc*.d links for the script
/sbin/chkconfig --add /etc/rc.d/init.d/burp

%preun
if [ $1 -eq 0 ] ; then
    /sbin/service /etc/rc.d/init.d/burp stop >/dev/null 2>&1
    /sbin/chkconfig --del /etc/rc.d/init.d/burp
fi


%files
%defattr(-, root, root, -)
%{_sbindir}/burp
%{_sbindir}/burp_ca
%{_sbindir}/bedup
%{_sysconfdir}/burp/autoupgrade/server/win32/script
%{_sysconfdir}/burp/clientconfdir/incexc/example
%{_sysconfdir}/burp/clientconfdir/testclient
%{_sysconfdir}/burp/notify_script
%{_sysconfdir}/burp/ssl_extra_checks_script
%{_sysconfdir}/burp/summary_script
%{_sysconfdir}/burp/timer_script
%{_sysconfdir}/rc.d/init.d/burp
%dir %attr(-, root, root)
%{_localstatedir}/spool/burp
## What macro?
%config(noreplace) %{_sysconfdir}/burp/burp.conf
%config(noreplace) %{_sysconfdir}/burp/burp-server.conf
%config %{_sysconfdir}/burp/autoupgrade/server/win64/script
%config %{_sysconfdir}/burp/CA.cnf
%doc %{_mandir}/man8/*

%changelog
* Sun Sep 16 2012 Gonéri Le Bouder <goneri@rulezlan.org> - 1.3.12-1.el6
- Upgrade to 1.3.12
* Sun Feb 05 2012 Alice Kaerast <alice.kaerast@webanywhere.co.uk> - 1.2.2
- Initial Build
