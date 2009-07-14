# $Id$
%define php_extdir %(php-config --extension-dir 2>/dev/null || echo %{_libdir}/php4)
%define php_config_opts %(php-config --configuration-options 2>/dev/null)
%define _dbg %{nil}
%define peclname %{lua:

name = "php-pecl-geoip"

php_config_opts = rpm.expand("%{php_config_opts}")
if (string.find(php_config_opts, "--enable-debug", 1, true)) then
  name = "php-dbg" .. string.sub(name, 4)
end
print(name)
}
%{lua: 
current_name = rpm.expand("%{peclname}")
if (string.find(current_name, "-dbg", 1, true)) then
  rpm.define("_dbg -dbg")
end
}

Summary: PECL package for working with geoip
Name: %{peclname}
Version: 1.0.7
Release: 1
License: PHP
Group: Development/Languages
URL: http://pecl.php.net/package/geoip
Source: http://pecl.php.net/get/geoip-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: php%{_dbg}, GeoIP
BuildRequires: php%{_dbg}, php%{_dbg}-devel, GeoIP-devel
# Required by phpize
BuildRequires: autoconf213, automake, libtool, gcc-c++

%description
This PHP extension allows you to find the location of an IP address 
- City, State, Country, Longitude, Latitude, and other information as all, 
such as ISP and connection type. For more info, please visit Maxmind's website.

%prep
%setup -n geoip-%{version}


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
%{__mkdir_p} %{buildroot}%{_sysconfdir}/php.cli.d/extensions
%{__mkdir_p} %{buildroot}%{_sysconfdir}/php.cgi.d/extensions

%{__cat} > %{buildroot}%{_sysconfdir}/php.mod.d/extensions/geoip.ini << 'EOF'
; Enable geoip extension module
extension=geoip.so
EOF
%{__cat} > %{buildroot}%{_sysconfdir}/php.cli.d/extensions/geoip.ini << 'EOF'
; Enable geoip extension module
extension=geoip.so
EOF
%{__cat} > %{buildroot}%{_sysconfdir}/php.cgi.d/extensions/geoip.ini << 'EOF'
; Enable geoip extension module
extension=geoip.so
EOF

%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc README ChangeLog
%config(noreplace) %{_sysconfdir}/php.mod.d/extensions/geoip.ini
%config(noreplace) %{_sysconfdir}/php.cli.d/extensions/geoip.ini
%config(noreplace) %{_sysconfdir}/php.cgi.d/extensions/geoip.ini
%{php_extdir}/geoip.so


%changelog
* Thu Jul  9 2009 Clay Loveless <clay@killersoft.com>
- Initial 1.0.7 build w/multi-sapi configs.
