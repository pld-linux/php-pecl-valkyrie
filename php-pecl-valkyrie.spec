# TODO
# doesn't build
%define		_modname	valkyrie
%define		_status		alpha
%define		_sysconfdir	/etc/php
%define		extensionsdir	%(php-config --extension-dir 2>/dev/null)
Summary:	%{_modname} - POST and GET validation extension
Summary(pl):	%{_modname} - rozszerzenie kontroluj±ce poprawno¶æ POST i GET
Name:		php-pecl-%{_modname}
Version:	0.1
Release:	1.1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	787621389178eec3d70ee61f22e22722
URL:		http://pecl.php.net/package/valkyrie/
BuildRequires:	libxml2-devel
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.254
%{?requires_php_extension}
Requires:	%{_sysconfdir}/conf.d
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This extension makes validating POST and GET parameters easier,
through the use of a single XML file for declaring all parameters to
be received by all files of an application. See
<http://www.xavier-noguer.com/valkyrie.html> for details.

In PECL status of this package is: %{_status}.

%description -l pl
To rozszerzenie u³atwia sprawdzanie poprawno¶ci parametrów POST i GET
poprzez u¿ycie pojedynczego pliku XML do deklaracji wszystkich
parametrów, które maj± otrzymaæ wszystkie pliki z aplikacji. Szczegó³y
mo¿na znale¼æ pod adresem <http://www.xavier-noguer.com/valkyrie.html>.

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
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/conf.d,%{extensionsdir}}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}
cat <<'EOF' > $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/%{_modname}.ini
; Enable %{_modname} extension module
extension=%{_modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -f /etc/apache/conf.d/??_mod_php.conf ] || %service -q apache restart
[ ! -f /etc/httpd/httpd.conf/??_mod_php.conf ] || %service -q httpd restart

%postun
if [ "$1" = 0 ]; then
	[ ! -f /etc/apache/conf.d/??_mod_php.conf ] || %service -q apache restart
	[ ! -f /etc/httpd/httpd.conf/??_mod_php.conf ] || %service -q httpd restart
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}/{CREDITS,EXPERIMENTAL}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/%{_modname}.ini
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
