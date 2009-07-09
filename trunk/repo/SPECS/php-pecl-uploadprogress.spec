# $Id$
%define php_extdir %(php-config --extension-dir 2>/dev/null || echo %{_libdir}/php4)

Summary: PECL package to track progress of a file upload
Name: php-pecl-uploadprogress
Version: 1.0.1
Release: 1
License: PHP
Group: Development/Languages
URL: http://pecl.php.net/package/uploadprogress/
Source: http://pecl.php.net/get/uploadprogress-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: php
BuildRequires: php, php-devel
# Required by phpize
BuildRequires: autoconf213, automake, libtool, gcc-c++

%description
Allows tracking of progress of an uploaded file. Known issues with 
SAPIs other than Apache mod_php, so only mod_php configuration is
enabled in this package.


%prep
%setup -n uploadprogress-%{version}


%build
# Workaround for broken old phpize on 64 bits
%{__cat} %{_bindir}/phpize | sed 's|/lib/|/%{_lib}/|g' > phpize && sh phpize
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install INSTALL_ROOT=%{buildroot}

# Drop in the bit of configuration
%{__mkdir_p} %{buildroot}%{_sysconfdir}/php.mod.d/extensions
%{__cat} > %{buildroot}%{_sysconfdir}/php.mod.d/extensions/uploadprogress.ini << 'EOF'
; Enable uploadprogress extension module
extension=uploadprogress.so
EOF


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%config(noreplace) %{_sysconfdir}/php.mod.d/extensions/uploadprogress.ini
%{php_extdir}/uploadprogress.so


%changelog
* Thu Jul  9 2009 Clay Loveless <clay@killersoft.com>
- Initial 1.0.1 release
