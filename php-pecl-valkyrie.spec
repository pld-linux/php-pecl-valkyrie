# TODO
# doesn't build
%define		_modname	valkyrie
%define		_status		alpha
Summary:	%{_modname} - POST and GET validation extension
Summary(pl.UTF-8):	%{_modname} - rozszerzenie kontrolujące poprawność POST i GET
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
BuildRequires:	rpmbuild(macros) >= 1.344
%{?requires_php_extension}
Requires:	php-common >= 4:5.0.4
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This extension makes validating POST and GET parameters easier,
through the use of a single XML file for declaring all parameters to
be received by all files of an application. See
<http://www.xavier-noguer.com/valkyrie.html> for details.

In PECL status of this package is: %{_status}.

%description -l pl.UTF-8
To rozszerzenie ułatwia sprawdzanie poprawności parametrów POST i GET
poprzez użycie pojedynczego pliku XML do deklaracji wszystkich
parametrów, które mają otrzymać wszystkie pliki z aplikacji. Szczegóły
można znaleźć pod adresem <http://www.xavier-noguer.com/valkyrie.html>.

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
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{_modname}.ini
; Enable %{_modname} extension module
extension=%{_modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}/{CREDITS,EXPERIMENTAL}
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{_modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{_modname}.so
