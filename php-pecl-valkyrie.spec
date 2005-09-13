%define		_modname	valkyrie
%define		_status		alpha

Summary:	%{_modname} - POST and GET validation extension
Summary(pl):	%{_modname} - rozszerzenie kontroluj±ce poprawno¶æ POST i GET
Name:		php-pecl-%{_modname}
Version:	0.1
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	787621389178eec3d70ee61f22e22722
URL:		http://pecl.php.net/package/valkyrie/
BuildRequires:	libxml2-devel
BuildRequires:	php-devel
Requires:	php-common
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php

%description
This extension makes validating POST and GET parameters easier,
through the use of a single XML file for declaring all parameters to
be received by all files of an application. See
http://www.xavier-noguer.com/valkyrie.html for details.

In PECL status of this package is: %{_status}.

%description -l pl
To rozszerzenie u³atwia sprawdzanie poprawno¶ci parametrów POST i GET
poprzez u¿ycie pojedynczego pliku XML do deklaracji wszystkich
parametrów, które maj± otrzymaæ wszystkie pliki z aplikacji. Szczegó³y
mo¿na znale¼æ pod adresem http://www.xavier-noguer.com/valkyrie.html .

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{extensionsdir}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php-module-install install %{_modname} %{_sysconfdir}/php-cgi.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove %{_modname} %{_sysconfdir}/php-cgi.ini
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}/{CREDITS,EXPERIMENTAL}
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
