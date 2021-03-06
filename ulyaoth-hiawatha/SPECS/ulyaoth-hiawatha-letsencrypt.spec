%define debug_package %{nil}

Summary: Hiawatha is an open source webserver with a focus on security.
Name: ulyaoth-hiawatha-letsencrypt
Version: 10.3
Release: 2%{?dist}
BuildArch: x86_64
Vendor: Hiawatha.
URL: https://www.hiawatha-webserver.org/
Packager: Sjir Bagmeijer <sbagmeijer@ulyaoth.net>

Source0: https://www.hiawatha-webserver.org/files/hiawatha-%{version}.tar.gz

License: GPLv2

BuildRoot: %{_tmppath}/hiawatha-%{version}-%{release}-root

Requires: ulyaoth-hiawatha = %{version}

Provides: hiawatha-letsencrypt
Provides: ulyaoth-hiawatha-letsencrypt

%description
Hiawatha is an open source webserver with a focus on security. I started Hiawatha in January 2002. Before that time, I had used several webservers, but I didn't like them. They had unlogical, almost cryptic configuration syntax and none of them gave me a good feeling about their security and robustness. So, I decided it was time to write my own webserver. I never thought that my webserver would become what it is today, but I enjoyed working on it and liked to have my own open source project. In the years that followed, Hiawatha became a fully functional webserver.

%prep
%setup -q -n hiawatha-%{version}

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT

%{__mkdir} -p $RPM_BUILD_ROOT%{_sysconfdir}/hiawatha/extra

cp -rf %{_builddir}/hiawatha-%{version}/extra/letsencrypt $RPM_BUILD_ROOT%{_sysconfdir}/hiawatha/extra/

%files
%defattr(-,root,root)
%dir %{_sysconfdir}/hiawatha
%dir %{_sysconfdir}/hiawatha/extra
%dir %{_sysconfdir}/hiawatha/extra/letsencrypt
%dir %{_sysconfdir}/hiawatha/extra/letsencrypt/libraries

%attr(0755,root,root) %{_sysconfdir}/hiawatha/extra/letsencrypt/letsencrypt
%attr(0644,root,root) %{_sysconfdir}/hiawatha/extra/letsencrypt/letsencrypt.conf
%attr(0644,root,root) %{_sysconfdir}/hiawatha/extra/letsencrypt/README.txt

%attr(0644,root,root) %{_sysconfdir}/hiawatha/extra/letsencrypt/libraries/acme.php
%attr(0644,root,root) %{_sysconfdir}/hiawatha/extra/letsencrypt/libraries/config.php
%attr(0644,root,root) %{_sysconfdir}/hiawatha/extra/letsencrypt/libraries/hiawatha_config.php
%attr(0644,root,root) %{_sysconfdir}/hiawatha/extra/letsencrypt/libraries/http.php
%attr(0644,root,root) %{_sysconfdir}/hiawatha/extra/letsencrypt/libraries/https.php
%attr(0644,root,root) %{_sysconfdir}/hiawatha/extra/letsencrypt/libraries/letsencrypt.php
%attr(0644,root,root) %{_sysconfdir}/hiawatha/extra/letsencrypt/libraries/openssl.conf
%attr(0644,root,root) %{_sysconfdir}/hiawatha/extra/letsencrypt/libraries/rsa.php

%pre

%post
    # print site info
    cat <<BANNER
----------------------------------------------------------------------

Thank you for using ulyaoth-hiawatha-letsencrypt!

Please find the official documentation for hiawatha here:
* https://www.hiawatha-webserver.org

For any additional help please visit my forum at:
* https://www.ulyaoth.net

----------------------------------------------------------------------
BANNER

%preun

%postun

%changelog
* Sat Jul 2 2016 Sjir Bagmeijer <sbagmeijer@ulyaoth.net> 10.3-2
- Updated to mbedTLS 2.3.

* Mon Jun 6 2016 Sjir Bagmeijer <sbagmeijer@ulyaoth.net> 10.3-1
- Updated to Hiawatha 10.3.

* Tue May 3 2016 Sjir Bagmeijer <sbagmeijer@ulyaoth.net> 10.2-1
- Initial release with Hiawatha 10.2.
