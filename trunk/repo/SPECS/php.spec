# $Id$
# yum install -y bzip2-devel curl-devel c-ares-devel libidn-devel db4-devel \
#   expat-devel gmp-devel httpd-devel libjpeg-devel libpng-devel pam-devel \
#   libstdc++-devel openssl-devel zlib-devel smtpdaemon fileutils file perl \
#   libtool gcc-c++ libxml2-devel autoconf213 enchant-devel krb5-devel \
#   libc-client-devel libtidy-devel cyrus-sasl-devel openldap-devel \
#   postgresql-devel unixODBC-devel net-snmp-devel readline-devel \
#   freetds-devel libXpm-devel freetype-devel gnutls-devel libicu-devel \
#   libxslt-devel t1lib-devel libmcrypt-devel gettext-devel oracle-instantclient11.1-devel oracle-instantclient11.1-basic
# rpm -Uvh http://s3.killersoft.com/rpms/oracle-instantclient11.1-basic-11.1.0.7.0-1.i386.rpm
# rpm -Uvh http://s3.killersoft.com/rpms/oracle-instantclient11.1-devel-11.1.0.7.0-1.i386.rpm

#  -dbg
# -dbg conflict/opposite of -dbg
#   --enable-debug (or not)

%define contentdir /var/www

Summary: PHP: Hypertext Preprocessor
Name: php
Version: 5.3.0
Release: 4
Group: Development/Languages
BuildRoot: %{_tmppath}/php-%{version}-buildroot
Obsoletes: php-dbg, php3, phpfi, stronghold-php
URL: http://www.php.net/
License: PHP License
Provides: mod_php = %{version}-%{release}
Requires: php-common = %{version}-%{release}
BuildRequires: curl-devel, db4-devel
BuildRequires: expat-devel, gmp-devel, httpd-devel
BuildRequires: pam-devel, libstdc++-devel, openssl-devel, zlib-devel, smtpdaemon
BuildRequires: fileutils, file, perl, libtool, gcc-c++, oracle-instantclient11.1-devel
BuildRequires: autoconf213, krb5-devel, libc-client-devel
Source0: http://www.php.net/distributions/php-%{version}.tar.bz2

%description
PHP is an HTML-embedded scripting language. Much of its syntax is
borrowed from C, Java and Perl with a couple of unique PHP-specific
features thrown in. The goal of the language is to allow web
developers to write dynamically generated pages quickly.

%package cgi
Group: Development/Languages
Summary: CGI/FastCGI interface for PHP
Requires: php-common = %{version}-%{release}
Provides: php-cgi = %{version}-%{release}
Conflicts: php-dbg-cgi

%description cgi
The php-cgi package contains the CGI interface.

%package cli
Group: Development/Languages
Summary: Command-line interface for PHP
Requires: php-common = %{version}-%{release}
Provides: php-cli = %{version}-%{release}
Conflicts: php-dbg-cli

%description cli
The php-cli package contains the command-line interface.

%package common
Group: Development/Languages
Summary: Common files for PHP
Requires: php = %{version}-%{release}
Requires: libxml2 < 2.7.0, curl, openssl, expat
Provides: php-api = %{apiver}, php-zend-api = %{zendver}
Provides: php-ctype, php-curl, php-date
Provides: php-ftp, php-hash, php-iconv, php-libxml
Provides: php-openssl, php-pcre, php-mcrypt, php-pdo
Provides: php-reflection, php-session, php-shmop, php-simplexml
Provides: php-spl, php-sysvsem, php-sysvshm, php-sysvmsg, php-tokenizer
Provides: php-zlib, php-json
Obsoletes: php-openssl, php-curl, php-mhash
Obsoletes: php-pecl-json, php-pecl-fileinfo
Conflicts: php-dbg-common

%description common
The php-common package contains files used by both the php
package and the php-cli package.

%package devel
Group: Development/Libraries
Summary: Files needed for building PHP extensions
Requires: php = %{version}-%{release}, autoconf213, automake
Conflicts: php-dbg-devel

%description devel
The php-devel package contains the files needed for building PHP
extensions. If you need to compile your own PHP extensions, you will
need to install this package.

%package enchant
Group: Development/Languages
Summary: A module for uniformity and conformity of various spelling libraries.
Requires: php-common = %{version}-%{release}, enchant
BuildRequires: enchant-devel
Conflicts: php-dbg-enchant

%description enchant
php-enchant is the PHP binding for the Enchant library. Enchant steps in to 
provide uniformity and conformity on top of all spelling libraries, 
and implement certain features that may be lacking in any individual 
provider library. Everything should "just work" for any and 
every definition of "just working."

%package imap
Group: Development/Languages
Summary: A module for PHP applications that use IMAP, NNTP or POP3.
Requires: php-common = %{version}-%{release}, libc-client, openssl
Obsoletes: mod_php3-imap, stronghold-php-imap
BuildRequires: krb5-devel
BuildRequires: openssl-devel
BuildRequires: libc-client-devel
Conflicts: php-dbg-imap

%description imap
The php-imap package enables functions for the IMAP protocol, as well 
as NNTP, POP3 and local mailbox access methods.

%package mysql
Summary: A module for PHP applications that use MySQL databases.
Group: Development/Languages
Requires: php-common = %{version}-%{release}
Provides: php_database, php-mysqli
Obsoletes: mod_php3-mysql, stronghold-php-mysql
Conflicts: php-dbg-mysql

%description mysql
The php-mysql package contains a dynamic shared object that will add
MySQL database support to PHP. MySQL is an object-relational database
management system. PHP is an HTML-embeddable scripting language. If
you need MySQL support for PHP applications, you will need to install
this package and the php package.

%package tidy
Group: Development/Languages
Summary: A module for cleaning and repairing HTML documents.
Requires: php-common = %{version}-%{release}, libtidy
BuildRequires: libtidy-devel
Conflicts: php-dbg-tidy

%description tidy
php-tidy is a binding for the Tidy HTML clean and repair utility which 
allows you to not only clean and otherwise manipulate HTML documents, 
but also traverse the document tree.

%package ldap
Summary: A module for PHP applications that use LDAP.
Group: Development/Languages
Requires: php-common = %{version}-%{release}, openldap
Obsoletes: mod_php3-ldap, stronghold-php-ldap
BuildRequires: cyrus-sasl-devel, openldap-devel, openssl-devel
Conflicts: php-dbg-ldap

%description ldap
The php-ldap package is a dynamic shared object (DSO) for the Apache
Web server that adds Lightweight Directory Access Protocol (LDAP)
support to PHP. LDAP is a set of protocols for accessing directory
services over the Internet. PHP is an HTML-embedded scripting
language. If you need LDAP support for PHP applications, you will
need to install this package in addition to the php package.

%package oci8
Summary: An Oracle database module for PHP.
Group: Development/Languages
Requires: php-common = %{version}-%{release}, php-pdo, oracle-instantclient11.1-basic
Provides: php_database
BuildRequires: krb5-devel, openssl-devel, oracle-instantclient11.1-devel
Conflicts: php-dbg-oci8

%description oci8
The php-oci8 package includes a dynamic shared object (DSO) that can
be compiled in to the Apache Web server to add Oracle database
support to PHP. If you need back-end support for Oracle, you should 
install this package in addition to the main php package.

%package pgsql
Summary: A PostgreSQL database module for PHP.
Group: Development/Languages
Requires: php-common = %{version}-%{release}, php-pdo, postgresql
Provides: php_database
Obsoletes: mod_php3-pgsql, stronghold-php-pgsql
BuildRequires: krb5-devel, openssl-devel, postgresql-devel
Conflicts: php-dbg-pgsql

%description pgsql
The php-pgsql package includes a dynamic shared object (DSO) that can
be compiled in to the Apache Web server to add PostgreSQL database
support to PHP. PostgreSQL is an object-relational database management
system that supports almost all SQL constructs. PHP is an
HTML-embedded scripting language. If you need back-end support for
PostgreSQL, you should install this package in addition to the main
php package.

%package odbc
Group: Development/Languages
Requires: php-common = %{version}-%{release}, php-pdo, unixODBC
Summary: A module for PHP applications that use ODBC databases.
Provides: php_database
Obsoletes: stronghold-php-odbc
BuildRequires: unixODBC-devel
Conflicts: php-dbg-odbc

%description odbc
The php-odbc package contains a dynamic shared object that will add
database support through ODBC to PHP. ODBC is an open specification
which provides a consistent API for developers to use for accessing
data sources (which are often, but not always, databases). PHP is an
HTML-embeddable scripting language. If you need ODBC support for PHP
applications, you will need to install this package and the php
package.

%package mssql
Group: Development/Languages
Requires: php-common = %{version}-%{release}, php-pdo, freetds
Summary: A module for PHP applications that use MS SQL databases.
Provides: php_database
BuildRequires: freetds-devel
Conflicts: php-dbg-mssql

%description mssql
The php-mssql package contains a dynamic shared object that will add
database support for MS SQL to PHP. 

%package snmp
Summary: A module for PHP applications that query SNMP-managed devices.
Group: Development/Languages
Requires: php-common = %{version}-%{release}, net-snmp
BuildRequires: net-snmp-devel
Conflicts: php-snmp

%description snmp
The php-snmp package contains a dynamic shared object that will add
support for querying SNMP devices to PHP.  PHP is an HTML-embeddable
scripting language. If you need SNMP support for PHP applications, you
will need to install this package and the php package.

%package dba
Summary: A database abstraction layer module for PHP applications
Group: Development/Languages
Requires: php-common = %{version}-%{release}
Conflicts: php-dbg-dba

%description dba
The php-dba package contains a dynamic shared object that will add
support for using the DBA database abstraction layer to PHP.

%package readline
Summary: A module for PHP applications for using the GNU Readline library
Group: Development/Languages
Requires: php-common = %{version}-%{release}, readline
BuildRequires: readline-devel
Conflicts: php-dbg-readline

%description readline
The php-readline package contains functions that provide editable command 
lines. An example being the way Bash allows you to use the arrow keys to 
insert characters or scroll through command history.

%package soap
Group: Development/Languages
Requires: php-common = %{version}-%{release}
Summary: A module for PHP applications that use the SOAP protocol
BuildRequires: libxml2-devel
Conflicts: php-dbg-soap

%description soap
The php-soap package contains a dynamic shared object that will add
support to PHP for using the SOAP web services protocol.

%package xmlrpc
Summary: A module for PHP applications which use the XML-RPC protocol
Group: Development/Languages
Requires: php-common = %{version}-%{release}
BuildRequires: expat-devel
Conflicts: php-dbg-xmlrpc

%description xmlrpc
The php-xmlrpc package contains a dynamic shared object that will add
support for the XML-RPC protocol to PHP.

%package mbstring
Summary: A module for PHP applications which need multi-byte string handling
Group: Development/Languages
Requires: php-common = %{version}-%{release}
Conflicts: php-dbg-mbstring

%description mbstring
The php-mbstring package contains a dynamic shared object that will add
support for multi-byte string handling to PHP.

%package gd
Summary: A module for PHP applications for using the gd graphics library
Group: Development/Languages
Requires: php-common = %{version}-%{release}
BuildRequires: freetype-devel, t1lib-devel, libjpeg-devel, libpng-devel, libXpm-devel
Conflicts: php-dbg-gd

%description gd
The php-gd package contains a dynamic shared object that will add
support for using the gd graphics library to PHP.

%package bcmath
Summary: A module for PHP applications for using the bcmath library
Group: Development/Languages
Requires: php-common = %{version}-%{release}
Conflicts: php-dbg-bcmath

%description bcmath
The php-bcmath package contains a dynamic shared object that will add
support for using the bcmath library to PHP.

%package mcrypt
Summary: A module for PHP applications for using the mcrypt library
Group: Development/Languages
Requires: php-common = %{version}-%{release}, libmcrypt
BuildRequires: libmcrypt-devel
Conflicts: php-dbg-mcrypt

%description mcrypt
The php-mcrypt package contains a dynamic shared object that will add
support for using the mcrypt library to PHP.

%package exif
Summary: A module for PHP applications for using the EXIF functions
Group: Development/Languages
Requires: php-common = %{version}-%{release}
Conflicts: php-dbg-exif

%description exif
The php-exif package contains a dynamic shared object that will add
support for using the EXIF functions to PHP.

%package bz2
Summary: A module for PHP applications for using the bzip2 functions
Group: Development/Languages
Requires: php-common = %{version}-%{release}, bzip2
BuildRequires: bzip2-devel
Conflicts: php-dbg-bz2

%description bz2
The php-bz2 package contains a dynamic shared object that will add
support for using the bzip2 functions to PHP.

%package gmp
Summary: A module for PHP applications for using the gmp functions
Group: Development/Languages
Requires: php-common = %{version}-%{release}, gmp
BuildRequires: gmp-devel
Conflicts: php-dbg-gmp

%description gmp
The php-gmp package contains a dynamic shared object that will add
support for using the gmp functions to PHP.

%package wddx
Summary: A module for PHP applications for using the WDDX functions
Group: Development/Languages
Requires: php-common = %{version}-%{release}
BuildRequires: expat-devel
Conflicts: php-dbg-wddx

%description wddx
The php-wddx package contains a dynamic shared object that will add
support for using the WDDX functions to PHP.

%package calendar
Summary: A module for PHP applications for using the calendar functions
Group: Development/Languages
Requires: php-common = %{version}-%{release}
Conflicts: php-dbg-calendar

%description calendar
The php-calendar package contains a dynamic shared object that will add
support for using the calendar functions to PHP.

%package gettext
Summary: A module for PHP applications for using the gettext functions
Group: Development/Languages
Requires: php-common = %{version}-%{release}, gettext
BuildRequires: gettext-devel
Conflicts: php-dbg-gettext

%description gettext
The php-gettext package contains a dynamic shared object that will add
support for using the gettext functions to PHP.

%package xsl
Summary: A module for PHP applications for using the xsl functions
Group: Development/Languages
Requires: php-common = %{version}-%{release}, libxslt, libxml2
BuildRequires: libxslt-devel libxml2-devel
Conflicts: php-dbg-xsl

%description xsl
The php-xsl package contains a dynamic shared object that will add
support for using the xsl functions to PHP.

%package zip
Summary: A module for PHP applications for using the Zip functions
Group: Development/Languages
Requires: php-common = %{version}-%{release}, zlib
BuildRequires: zlib-devel
Conflicts: php-dbg-zip

%description zip
The php-zip package contains a dynamic shared object that will add
support for using the zip functions to PHP.

%package intl
Summary: A module for PHP applications for using the intl functions
Group: Development/Languages
Requires: php-common = %{version}-%{release}, libicu
BuildRequires: libicu-devel
Conflicts: php-dbg-intl

%description intl
The php-intl package contains a dynamic shared object that will add
support for using the intl functions to PHP.

%package pcntl
Summary: A module for PHP applications for using the proccess control functions
Group: Development/Languages
Requires: php-common = %{version}-%{release}
Conflicts: php-dbg-pcntl

%description pcntl
The php-pcntl package contains a dynamic shared object that will add
support for using the process control functions to PHP.

%prep
%setup -q -n php-%{version}

%{__cat} <<'EOF' >logrotate.d.php
/var/log/php/*.log {
  daily
  missingok
  rotate 7
  nocompress
  notifempty
  sharedscripts
  postrotate
      /bin/kill -HUP `cat /var/run/syslogd.pid 2> /dev/null` 2> /dev/null || true
  endscript
}
EOF

# Prevent %%doc confusion over LICENSE files
cp Zend/LICENSE Zend/ZEND_LICENSE
cp TSRM/LICENSE TSRM_LICENSE
cp ext/gd/libgd/README gd_README

# fix busted pdo_oci config.m4 for x86_64
%ifarch x86_64
sed -i -e 's|/client|/client64|' ext/pdo_oci/config.m4
PHP_AUTOCONF=/usr/bin/autoconf-2.13
PHP_AUTOHEADER=/usr/bin/autoheader-2.13
export PHP_AUTOCONF PHP_AUTOHEADER
./buildconf --force
%endif

# fix libdir path issues. Thanks, Rob Richards.
sed -i -e 's|(libdir)/build|(libdir)/php/build|' scripts/Makefile.frag
sed -i -e 's|`eval echo @libdir@`/build|`eval echo @libdir@`/php/build|' scripts/phpize.in
sed -i -e 's|EXTENSION_DIR=$libdir/extensions/$extbasedir|EXTENSION_DIR=$libdir/php/extensions/$extbasedir|' configure

# Sources are built a couple times
mkdir build-cli build-cgi build-apache

%build
PHP_AUTOCONF=/usr/bin/autoconf-2.13
PHP_AUTOHEADER=/usr/bin/autoheader-2.13
export PHP_AUTOCONF PHP_AUTOHEADER

if test "x%{dist}" = "x.el5"; then
  CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -Wno-pointer-sign"
else
  CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
fi

CPPFLAGS="-DLDAP_DEPRECATED=1"
export CFLAGS CPPFLAGS

# Set PEAR_INSTALLDIR to ensure that the hard-coded include_path
# includes the PEAR directory even though pear is packaged
# separately.
PEAR_INSTALLDIR=%{_datadir}/pear; export PEAR_INSTALLDIR

# Shell function to configure and build a PHP tree.
build() {
ln -sf ../configure
sh ./configure \
  --prefix=%{_prefix} \
  --sysconfdir=%{_sysconfdir} \
  --libdir=%{_libdir} \
  --with-libdir=%{_lib} \
  --mandir=%{_prefix}/share/man \
  --with-pic \
  --disable-rpath \
  --with-pear \
  --with-curl \
  --with-curlwrappers \
  --with-openssl \
  --with-zlib-dir=/usr \
  --with-zlib \
  --enable-ftp --with-openssl-dir=%{_prefix} \
  --enable-shmop \
  --enable-sysvsem \
  --enable-sysvshm \
  --enable-sysvmsg \
  --enable-sockets \
  --enable-sqlite-utf8 \
  --with-kerberos \
  --with-iconv \
  --enable-gd-jis-conv \
  --enable-gd-native-ttf \
  --with-jpeg-dir=%{_prefix} \
  --with-png-dir=%{_prefix} \
  --with-freetype-dir=%{_prefix} \
  --with-xpm-dir=%{_prefix} \
  --with-libxml-dir=%{_prefix} \
  --with-libexpat-dir=%{_prefix} \
  $*

if test $? != 0; then
  tail -500 config.log
  : configure failed
  exit 1
fi

# fix makefile extensions dir
#sed -i -e 's|%{_prefix}/lib/extensions|%{_libdir}/php/extensions|' Makefile

make %{?_smp_mflags}
}

# all shared extensions here so we don't have to build them every time
pushd build-cli
build --enable-cli --disable-cgi \
    --with-pear \
    --with-config-file-path=%{_sysconfdir}/php.cli.d \
    --with-config-file-scan-dir=%{_sysconfdir}/php.cli.d/extensions \
    --with-unixODBC=shared,%{_prefix} \
    --with-pdo-odbc=shared,unixODBC,%{_prefix} \
    --with-imap=shared --with-imap-ssl \
    --with-tidy=shared \
    --with-enchant=shared \
    --enable-dba=shared --with-db4=%{_prefix} \
    --with-ldap=shared --with-ldap-sasl \
    --with-mysql=shared,mysqlnd \
    --with-mysqli=shared,mysqlnd \
    --with-pdo-mysql=shared,mysqlnd \
    --with-pgsql=shared \
    --with-pdo-pgsql=shared,%{_prefix} \
    --with-oci8=shared,instantclient \
    --with-pdo-oci=shared,instantclient,%{_prefix},11.1 \
    --with-mssql=shared,%{_prefix} \
    --with-pdo-dblib=shared,%{_prefix} \
    --with-snmp=shared,%{_prefix} --enable-ucd-snmp-hack \
    --with-t1lib=shared \
    --with-gd=shared \
    --with-mcrypt=shared \
    --enable-intl=shared \
    --with-xmlrpc=shared \
    --enable-soap=shared \
    --enable-mbregex \
    --enable-mbstring=shared,all \
    --enable-zip=shared \
    --with-xsl=shared,%{_prefix} \
    --enable-calendar=shared \
    --with-gettext=shared \
    --enable-wddx=shared \
    --with-gmp=shared \
    --with-bz2=shared \
    --enable-bcmath=shared \
    --enable-exif=shared \
    --with-readline=shared,%{_prefix} \
    --enable-pcntl=shared
popd

pushd build-cgi
# mysql shared extensions needed to trigger inclusion of mysqlnd internally
build --enable-cgi --disable-cli --without-pear \
      --with-config-file-path=%{_sysconfdir}/php.cgi.d \
      --with-mysql=shared,mysqlnd \
      --with-mysqli=shared,mysqlnd \
      --with-pdo-mysql=shared,mysqlnd \
      --with-config-file-scan-dir=%{_sysconfdir}/php.cgi.d/extensions
popd

pushd build-apache
# mysql shared extensions needed to trigger inclusion of mysqlnd internally
build --with-apxs2=%{_sbindir}/apxs --disable-cli --without-pear \
      --disable-dba --without-unixODBC \
      --with-config-file-path=%{_sysconfdir}/php.mod.d \
      --with-mysql=shared,mysqlnd \
      --with-mysqli=shared,mysqlnd \
      --with-pdo-mysql=shared,mysqlnd \
      --with-config-file-scan-dir=%{_sysconfdir}/php.mod.d/extensions
popd

#%check
#cd build-apache
### Run tests, using the CLI SAPI
#export NO_INTERACTION=1 REPORT_EXIT_STATUS=1 MALLOC_CHECK_=2
#unset TZ LANG LC_ALL
#make test || true

#set +x
#for f in `find .. -name \*.diff -type -f -print`; do
#  echo "TEST FAILURE: $f --"
#  cat "$f"
#  echo -e "
#--$f result ends."
#done
#set -x

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

# Install CLI
pushd build-cli
make install INSTALL_ROOT=$RPM_BUILD_ROOT
make install-pear INSTALL_ROOT=$RPM_BUILD_ROOT
popd

# Install CGI from the CGI SAPI build
pushd build-cgi
make install INSTALL_ROOT=$RPM_BUILD_ROOT
popd

# Install the Apache module
pushd build-apache

# Needed in non-root RPM build because PHP install updates httpd.conf
[ "$RPM_BUILD_ROOT" != "/" ] && {
  mkdir -p $RPM_BUILD_ROOT/etc/httpd/conf;
  cp /etc/httpd/conf/httpd.conf $RPM_BUILD_ROOT/etc/httpd/conf; }

make install-sapi INSTALL_ROOT=$RPM_BUILD_ROOT
make install-headers INSTALL_ROOT=$RPM_BUILD_ROOT
make install-build INSTALL_ROOT=$RPM_BUILD_ROOT
popd

# Install the configuration files and icons
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/php.cgi.d
install -m 644 php.ini-production $RPM_BUILD_ROOT%{_sysconfdir}/php.cgi.d/php.ini
install -m 644 php.ini-development $RPM_BUILD_ROOT%{_sysconfdir}/php.cgi.d/php-dev.ini

install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/php.cli.d
install -m 644 php.ini-production $RPM_BUILD_ROOT%{_sysconfdir}/php.cli.d/php.ini
install -m 644 php.ini-development $RPM_BUILD_ROOT%{_sysconfdir}/php.cli.d/php-dev.ini

install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/php.mod.d
install -m 644 php.ini-production $RPM_BUILD_ROOT%{_sysconfdir}/php.mod.d/php.ini
install -m 644 php.ini-development $RPM_BUILD_ROOT%{_sysconfdir}/php.mod.d/php-dev.ini
install -m 755 -d $RPM_BUILD_ROOT%{contentdir}/icons
install -m 644 *.gif $RPM_BUILD_ROOT%{contentdir}/icons/

# For PEAR packaging:
install -m 755 -d $RPM_BUILD_ROOT%{_libdir}/php/pear

# Use correct libdir
sed -i -e 's|%{_prefix}/lib|%{_libdir}|' $RPM_BUILD_ROOT%{_sysconfdir}/php.cgi.d/php.ini
sed -i -e 's|%{_prefix}/lib|%{_libdir}|' $RPM_BUILD_ROOT%{_sysconfdir}/php.cli.d/php.ini
sed -i -e 's|%{_prefix}/lib|%{_libdir}|' $RPM_BUILD_ROOT%{_sysconfdir}/php.mod.d/php.ini

# install the DSO
install -m 755 -d $RPM_BUILD_ROOT%{_libdir}/httpd/modules
install -m 755 build-apache/libs/libphp5.so $RPM_BUILD_ROOT%{_libdir}/httpd/modules

# Apache config fragment
install -m 755 -d $RPM_BUILD_ROOT/etc/httpd/conf.d
install -m 644 $RPM_SOURCE_DIR/php.conf $RPM_BUILD_ROOT/etc/httpd/conf.d

install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/php.cgi.d/extensions
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/php.cli.d/extensions
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/php.mod.d/extensions

install -m 755 -d $RPM_BUILD_ROOT%{_localstatedir}/%{_lib}/php
install -m 700 -d $RPM_BUILD_ROOT%{_localstatedir}/%{_lib}/php/session



%{__cat} <<'EOF' >$RPM_BUILD_ROOT%{_sysconfdir}/php.cli.d/extensions/pgsql.ini
; Enable pgsql extension
extension=pgsql.so
extension=pdo_pgsql.so
EOF
%{__cat} <<'EOF' >$RPM_BUILD_ROOT%{_sysconfdir}/php.cli.d/extensions/mysql.ini
; Enable MySQL extension
extension=mysql.so
extension=mysqli.so
extension=pdo_mysql.so
EOF
%{__cat} <<'EOF' >$RPM_BUILD_ROOT%{_sysconfdir}/php.cli.d/extensions/mssql.ini
; Enable mssql extension
extension=mssql.so
extension=pdo_dblib.so
EOF
%{__cat} <<'EOF' >$RPM_BUILD_ROOT%{_sysconfdir}/php.cli.d/extensions/odbc.ini
; Enable odbc extension
extension=odbc.so
extension=pdo_odbc.so
EOF
%{__cat} <<'EOF' >$RPM_BUILD_ROOT%{_sysconfdir}/php.cli.d/extensions/oci8.ini
; Enable Oracle extensions
extension=oci8.so
extension=pdo_oci.so
EOF
%{__cat} <<'EOF' >$RPM_BUILD_ROOT%{_sysconfdir}/php.cli.d/extensions/enchant.ini
; Enable enchant extension
extension=enchant.so
EOF
%{__cat} <<'EOF' >$RPM_BUILD_ROOT%{_sysconfdir}/php.cli.d/extensions/ldap.ini
; Enable ldap extension
extension=ldap.so
EOF
%{__cat} <<'EOF' >$RPM_BUILD_ROOT%{_sysconfdir}/php.cli.d/extensions/snmp.ini
; Enable snmp extension
extension=snmp.so
EOF
%{__cat} <<'EOF' >$RPM_BUILD_ROOT%{_sysconfdir}/php.cli.d/extensions/imap.ini
; Enable IMAP extension
extension=imap.so
EOF
%{__cat} <<'EOF' >$RPM_BUILD_ROOT%{_sysconfdir}/php.cli.d/extensions/tidy.ini
; Enable Tidy extension
extension=tidy.so
EOF
%{__cat} <<'EOF' >$RPM_BUILD_ROOT%{_sysconfdir}/php.cli.d/extensions/readline.ini
; Enable readline extension
extension=readline.so
EOF
%{__cat} <<'EOF' >$RPM_BUILD_ROOT%{_sysconfdir}/php.cli.d/extensions/dba.ini
; Enable dba extension
extension=dba.so
EOF
%{__cat} <<'EOF' >$RPM_BUILD_ROOT%{_sysconfdir}/php.cli.d/extensions/soap.ini
; Enable SOAP extension
extension=soap.so
EOF
%{__cat} <<'EOF' >$RPM_BUILD_ROOT%{_sysconfdir}/php.cli.d/extensions/xmlrpc.ini
; Enable XML-RPC extension
extension=xmlrpc.so
EOF
%{__cat} <<'EOF' >$RPM_BUILD_ROOT%{_sysconfdir}/php.cli.d/extensions/mbstring.ini
; Enable mbstring extension
extension=mbstring.so
EOF
%{__cat} <<'EOF' >$RPM_BUILD_ROOT%{_sysconfdir}/php.cli.d/extensions/gd.ini
; Enable gd extension
extension=gd.so
EOF
%{__cat} <<'EOF' >$RPM_BUILD_ROOT%{_sysconfdir}/php.cli.d/extensions/bcmath.ini
; Enable bcmath extension
extension=bcmath.so
EOF
%{__cat} <<'EOF' >$RPM_BUILD_ROOT%{_sysconfdir}/php.cli.d/extensions/mcrypt.ini
; Enable mcrypt extension
extension=mcrypt.so
EOF
%{__cat} <<'EOF' >$RPM_BUILD_ROOT%{_sysconfdir}/php.cli.d/extensions/exif.ini
; Enable exif extension
extension=exif.so
EOF
%{__cat} <<'EOF' >$RPM_BUILD_ROOT%{_sysconfdir}/php.cli.d/extensions/bz2.ini
; Enable bzip2 extension
extension=bz2.so
EOF
%{__cat} <<'EOF' >$RPM_BUILD_ROOT%{_sysconfdir}/php.cli.d/extensions/gmp.ini
; Enable gmp extension
extension=gmp.so
EOF
%{__cat} <<'EOF' >$RPM_BUILD_ROOT%{_sysconfdir}/php.cli.d/extensions/wddx.ini
; Enable WDDX extension
extension=wddx.so
EOF
%{__cat} <<'EOF' >$RPM_BUILD_ROOT%{_sysconfdir}/php.cli.d/extensions/calendar.ini
; Enable calendar extension
extension=calendar.so
EOF
%{__cat} <<'EOF' >$RPM_BUILD_ROOT%{_sysconfdir}/php.cli.d/extensions/gettext.ini
; Enable gettext extension
extension=gettext.so
EOF
%{__cat} <<'EOF' >$RPM_BUILD_ROOT%{_sysconfdir}/php.cli.d/extensions/xsl.ini
; Enable xsl extension
extension=xsl.so
EOF
%{__cat} <<'EOF' >$RPM_BUILD_ROOT%{_sysconfdir}/php.cli.d/extensions/zip.ini
; Enable zip extension
extension=zip.so
EOF
%{__cat} <<'EOF' >$RPM_BUILD_ROOT%{_sysconfdir}/php.cli.d/extensions/intl.ini
; Enable intl extension
extension=intl.so
EOF
%{__cat} <<'EOF' >$RPM_BUILD_ROOT%{_sysconfdir}/php.cli.d/extensions/pcntl.ini
; Enable pcntl extension
extension=pcntl.so
EOF

cp $RPM_BUILD_ROOT%{_sysconfdir}/php.cli.d/extensions/*.ini $RPM_BUILD_ROOT%{_sysconfdir}/php.cgi.d/extensions
cp $RPM_BUILD_ROOT%{_sysconfdir}/php.cli.d/extensions/*.ini $RPM_BUILD_ROOT%{_sysconfdir}/php.mod.d/extensions


# Remove temporarily added conf file and the backup the PHP install created.
[ "$RPM_BUILD_ROOT" != "/" ] && rm -f $RPM_BUILD_ROOT/etc/httpd/conf/httpd.conf $RPM_BUILD_ROOT/etc/httpd/conf/httpd.conf.bak

# Remove unpackaged files
rm -rf $RPM_BUILD_ROOT%{_libdir}/php/extensions/no-debug-non-zts-20090626/*.a

# Remove irrelevant docs
rm -f README.{Zeus,QNX,CVS-RULES,WIN32-BUILD-SYSTEM}

# Remove errant PEAR files
rm -rf $RPM_BUILD_ROOT/.channels $RPM_BUILD_ROOT/.depdb $RPM_BUILD_ROOT/.depdblock $RPM_BUILD_ROOT/.filemap $RPM_BUILD_ROOT/.lock

# fix symlink
pushd $RPM_BUILD_ROOT/usr/bin
rm -f phar
ln -s phar.phar phar
popd

%files
%defattr(-,root,root)
%{_libdir}/httpd/modules/libphp5.so
%attr(0770,root,apache) %dir %{_localstatedir}/%{_lib}/php/session
%config %{_sysconfdir}/httpd/conf.d/php.conf
%{contentdir}/icons/php.gif

%files common
%defattr(-,root,root)
%doc CODING_STANDARDS CREDITS EXTENSIONS INSTALL LICENSE NEWS README*
%doc Zend/ZEND_* gd_README TSRM_LICENSE
%config(noreplace) %{_sysconfdir}/php.mod.d/php.ini
%config(noreplace) %{_sysconfdir}/php.mod.d/php-dev.ini
%dir %{_sysconfdir}/php.mod.d
%dir %{_localstatedir}/%{_lib}/php
#%dir %{_libdir}/php

%files cli
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/pear.conf
%config(noreplace) %{_sysconfdir}/php.cli.d/php.ini
%config(noreplace) %{_sysconfdir}/php.cli.d/php-dev.ini
%dir %{_sysconfdir}/php.cli.d
%{_bindir}/php
%{_bindir}/pear
%{_bindir}/peardev
%{_bindir}/pecl
%{_bindir}/phar
%{_bindir}/phar.phar
%{_libdir}/php/*.php
%{_libdir}/php/doc
%{_libdir}/php/data
%{_libdir}/php/test
%{_libdir}/php/PEAR
%{_libdir}/php/Structures
%{_libdir}/php/XML
%{_libdir}/php/OS
%{_libdir}/php/Archive
%{_libdir}/php/Console
%{_libdir}/php/.channels
%{_libdir}/php/.depdb
%{_libdir}/php/.depdblock
%{_libdir}/php/.filemap
%{_libdir}/php/.lock
%{_libdir}/php/.registry
%{_mandir}/man1/php.1*


%files cgi
%defattr(-,root,root)
%{_bindir}/php-cgi
%config(noreplace) %{_sysconfdir}/php.cgi.d/php.ini
%config(noreplace) %{_sysconfdir}/php.cgi.d/php-dev.ini
%dir %{_sysconfdir}/php.cgi.d

%files devel
%defattr(-,root,root)
%{_bindir}/php-config
%{_bindir}/phpize
%{_includedir}/php
%{_libdir}/php/build
%{_mandir}/man1/php-config.1*
%{_mandir}/man1/phpize.1*


%files enchant
%attr(755,root,root) %{_libdir}/php/extensions/no-debug-non-zts-20090626/enchant.so
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cli.d/extensions/enchant.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cgi.d/extensions/enchant.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.mod.d/extensions/enchant.ini

%files imap
%attr(755,root,root) %{_libdir}/php/extensions/no-debug-non-zts-20090626/imap.so
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cli.d/extensions/imap.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cgi.d/extensions/imap.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.mod.d/extensions/imap.ini

%files oci8
%attr(755,root,root) %{_libdir}/php/extensions/no-debug-non-zts-20090626/oci8.so
%attr(755,root,root) %{_libdir}/php/extensions/no-debug-non-zts-20090626/pdo_oci.so
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cli.d/extensions/oci8.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cgi.d/extensions/oci8.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.mod.d/extensions/oci8.ini

%files pgsql
%attr(755,root,root) %{_libdir}/php/extensions/no-debug-non-zts-20090626/pgsql.so
%attr(755,root,root) %{_libdir}/php/extensions/no-debug-non-zts-20090626/pdo_pgsql.so
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cli.d/extensions/pgsql.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cgi.d/extensions/pgsql.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.mod.d/extensions/pgsql.ini

%files mysql
%attr(755,root,root) %{_libdir}/php/extensions/no-debug-non-zts-20090626/mysql.so
%attr(755,root,root) %{_libdir}/php/extensions/no-debug-non-zts-20090626/mysqli.so
%attr(755,root,root) %{_libdir}/php/extensions/no-debug-non-zts-20090626/pdo_mysql.so
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cli.d/extensions/mysql.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cgi.d/extensions/mysql.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.mod.d/extensions/mysql.ini

%files odbc
%attr(755,root,root) %{_libdir}/php/extensions/no-debug-non-zts-20090626/odbc.so
%attr(755,root,root) %{_libdir}/php/extensions/no-debug-non-zts-20090626/pdo_odbc.so
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cli.d/extensions/odbc.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cgi.d/extensions/odbc.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.mod.d/extensions/odbc.ini

%files tidy
%attr(755,root,root) %{_libdir}/php/extensions/no-debug-non-zts-20090626/tidy.so
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cli.d/extensions/tidy.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cgi.d/extensions/tidy.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.mod.d/extensions/tidy.ini

%files mssql
%attr(755,root,root) %{_libdir}/php/extensions/no-debug-non-zts-20090626/mssql.so
%attr(755,root,root) %{_libdir}/php/extensions/no-debug-non-zts-20090626/pdo_dblib.so
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cli.d/extensions/mssql.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cgi.d/extensions/mssql.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.mod.d/extensions/mssql.ini

%files readline
%attr(755,root,root) %{_libdir}/php/extensions/no-debug-non-zts-20090626/readline.so
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cli.d/extensions/readline.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cgi.d/extensions/readline.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.mod.d/extensions/readline.ini

%files ldap
%attr(755,root,root) %{_libdir}/php/extensions/no-debug-non-zts-20090626/ldap.so
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cli.d/extensions/ldap.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cgi.d/extensions/ldap.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.mod.d/extensions/ldap.ini

%files snmp
%attr(755,root,root) %{_libdir}/php/extensions/no-debug-non-zts-20090626/snmp.so
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cli.d/extensions/snmp.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cgi.d/extensions/snmp.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.mod.d/extensions/snmp.ini

%files dba
%attr(755,root,root) %{_libdir}/php/extensions/no-debug-non-zts-20090626/dba.so
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cli.d/extensions/dba.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cgi.d/extensions/dba.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.mod.d/extensions/dba.ini

%files soap
%attr(755,root,root) %{_libdir}/php/extensions/no-debug-non-zts-20090626/soap.so
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cli.d/extensions/soap.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cgi.d/extensions/soap.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.mod.d/extensions/soap.ini

%files xmlrpc
%attr(755,root,root) %{_libdir}/php/extensions/no-debug-non-zts-20090626/xmlrpc.so
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cli.d/extensions/xmlrpc.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cgi.d/extensions/xmlrpc.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.mod.d/extensions/xmlrpc.ini

%files mbstring
%attr(755,root,root) %{_libdir}/php/extensions/no-debug-non-zts-20090626/mbstring.so
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cli.d/extensions/mbstring.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cgi.d/extensions/mbstring.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.mod.d/extensions/mbstring.ini

%files gd
%attr(755,root,root) %{_libdir}/php/extensions/no-debug-non-zts-20090626/gd.so
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cli.d/extensions/gd.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cgi.d/extensions/gd.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.mod.d/extensions/gd.ini

%files bcmath
%attr(755,root,root) %{_libdir}/php/extensions/no-debug-non-zts-20090626/bcmath.so
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cli.d/extensions/bcmath.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cgi.d/extensions/bcmath.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.mod.d/extensions/bcmath.ini

%files mcrypt
%attr(755,root,root) %{_libdir}/php/extensions/no-debug-non-zts-20090626/mcrypt.so
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cli.d/extensions/mcrypt.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cgi.d/extensions/mcrypt.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.mod.d/extensions/mcrypt.ini

%files exif
%attr(755,root,root) %{_libdir}/php/extensions/no-debug-non-zts-20090626/exif.so
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cli.d/extensions/exif.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cgi.d/extensions/exif.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.mod.d/extensions/exif.ini

%files bz2
%attr(755,root,root) %{_libdir}/php/extensions/no-debug-non-zts-20090626/bz2.so
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cli.d/extensions/bz2.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cgi.d/extensions/bz2.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.mod.d/extensions/bz2.ini

%files gmp
%attr(755,root,root) %{_libdir}/php/extensions/no-debug-non-zts-20090626/gmp.so
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cli.d/extensions/gmp.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cgi.d/extensions/gmp.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.mod.d/extensions/gmp.ini

%files wddx
%attr(755,root,root) %{_libdir}/php/extensions/no-debug-non-zts-20090626/wddx.so
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cli.d/extensions/wddx.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cgi.d/extensions/wddx.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.mod.d/extensions/wddx.ini

%files calendar
%attr(755,root,root) %{_libdir}/php/extensions/no-debug-non-zts-20090626/calendar.so
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cli.d/extensions/calendar.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cgi.d/extensions/calendar.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.mod.d/extensions/calendar.ini

%files gettext
%attr(755,root,root) %{_libdir}/php/extensions/no-debug-non-zts-20090626/gettext.so
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cli.d/extensions/gettext.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cgi.d/extensions/gettext.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.mod.d/extensions/gettext.ini

%files xsl
%attr(755,root,root) %{_libdir}/php/extensions/no-debug-non-zts-20090626/xsl.so
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cli.d/extensions/xsl.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cgi.d/extensions/xsl.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.mod.d/extensions/xsl.ini

%files zip
%attr(755,root,root) %{_libdir}/php/extensions/no-debug-non-zts-20090626/zip.so
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cli.d/extensions/zip.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cgi.d/extensions/zip.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.mod.d/extensions/zip.ini

%files intl
%attr(755,root,root) %{_libdir}/php/extensions/no-debug-non-zts-20090626/intl.so
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cli.d/extensions/intl.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cgi.d/extensions/intl.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.mod.d/extensions/intl.ini

%files pcntl
%attr(755,root,root) %{_libdir}/php/extensions/no-debug-non-zts-20090626/pcntl.so
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cli.d/extensions/pcntl.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.cgi.d/extensions/pcntl.ini
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.mod.d/extensions/pcntl.ini

%changelog
* Wed Aug 12 2009 Clay Loveless <clay@killersoft.com> 5.3.0-4
- Fixed paths for libs in x86_64 build
- Fixed pdo_oci config for x86_64
- Made sure php.ini files don't get overwritten.

* Tue Jul  7 2009 Clay Loveless <clay@killersoft.com> 5.3.0-2, 5.3.0-3
- Fixed paths for extension inclusion
- Fixed builds for cli, cgi, mod_php so that mysqlnd is enabled inside each.
- Fixed bogus obsoletes setting for php-mysql in php-common

* Fri Jul  3 2009 Clay Loveless <clay@killersoft.com> 5.3.0-1
- Updated to PHP 5.3.0
- Restored shared builds for subpackages of most extensions
  bundled with PHP.
- Added dbg build
- Split out config support for mod_php, cli, and cgi sapis

* Mon Mar 16 2009 Christopher Jones <christopher.jones@oracle.com> 5.2.9
- Use PHP 5.29
- Don't overwrite FCGI binary with CLI

* Wed Dec 17 2008 Chris Jones <christopher.jones@oracle.com> 5.2.8
- Use PHP 5.2.8
- Merge EL 5.3 php.spec changes
- Move OCI8 to external spec file

* Mon Jun 11 2007 Chris Jones <christopher.jones@oracle.com> 5.2.3
- Use PHP 5.2.3
- Remove OCI8 runtime dependency on Instant Client SDK

* Mon May 21 2007 Chris Jones <christopher.jones@oracle.com> 5.2.2
- Use PHP 5.2.2. Add OCI8/PDO_OCI package.
- Use EL 4 compile flag.
- Use PHP's PCRE

* Tue Dec 19 2006 Joe Orton <jorton@redhat.com> 5.1.6
- fix version for php-zend-abi (#218758)

* Thu Nov 23 2006 Joe Orton <jorton@redhat.com> 5.1.6-4.el5
- php-xml provides php-domxml (#215656)
- fix php-pdo-abi provide (#214281)
- provide php-zend-abi (#212804)
- don't Obsolete mod_php
- fix PDO sqlite TEXT extraction truncate-by-one (#217033)
- package php{ize,-config} man pages in -devel (#199382)
- change module subpackages to require php-common not php (#177821)
- add security fix for CVE-2006-5465 (#216114)

* Wed Oct  4 2006 Joe Orton <jorton@redhat.com> 5.1.6-3
- from upstream: add safety checks against integer overflow in _ecalloc

* Tue Aug 29 2006 Joe Orton <jorton@redhat.com> 5.1.6-2
- update to 5.1.6 (security fixes)
- bump default memory_limit to 16M (#196802)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 5.1.4-8.1
- rebuild

* Fri Jun  9 2006 Joe Orton <jorton@redhat.com> 5.1.4-8
- Provide php-posix (#194583)
- only provide php-pcntl from -cli subpackage
- add missing defattr's (thanks to Matthias Saou)

* Fri Jun  9 2006 Joe Orton <jorton@redhat.com> 5.1.4-7
- move Obsoletes for php-openssl to -common (#194501)
- Provide: php-cgi from -cli subpackage

* Fri Jun  2 2006 Joe Orton <jorton@redhat.com> 5.1.4-6
- split out php-cli, php-common subpackages (#177821)
- add php-pdo-abi version export (#193202)

* Wed May 24 2006 Radek Vokal <rvokal@redhat.com> 5.1.4-5.1
- rebuilt for new libnetsnmp

* Thu May 18 2006 Joe Orton <jorton@redhat.com> 5.1.4-5
- provide mod_php (#187891)
- provide php-cli (#192196)
- use correct LDAP fix (#181518)
- define _GNU_SOURCE in php_config.h and leave it defined
- drop (circular) dependency on php-pear

* Mon May  8 2006 Joe Orton <jorton@redhat.com> 5.1.4-3
- update to 5.1.4

* Wed May  3 2006 Joe Orton <jorton@redhat.com> 5.1.3-3
- update to 5.1.3

* Tue Feb 28 2006 Joe Orton <jorton@redhat.com> 5.1.2-5
- provide php-api (#183227)
- add provides for all builtin modules (Tim Jackson, #173804)
- own %%{_libdir}/php/pear for PEAR packages (per #176733)
- add obsoletes to allow upgrade from FE4 PDO packages (#181863)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 5.1.2-4.3
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 5.1.2-4.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Jan 31 2006 Joe Orton <jorton@redhat.com> 5.1.2-4
- rebuild for new libc-client soname

* Mon Jan 16 2006 Joe Orton <jorton@redhat.com> 5.1.2-3
- only build xmlreader and xmlwriter shared (#177810)

* Fri Jan 13 2006 Joe Orton <jorton@redhat.com> 5.1.2-2
- update to 5.1.2

* Thu Jan  5 2006 Joe Orton <jorton@redhat.com> 5.1.1-8
- rebuild again

* Mon Jan  2 2006 Joe Orton <jorton@redhat.com> 5.1.1-7
- rebuild for new net-snmp

* Mon Dec 12 2005 Joe Orton <jorton@redhat.com> 5.1.1-6
- enable short_open_tag in default php.ini again (#175381)

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Dec  8 2005 Joe Orton <jorton@redhat.com> 5.1.1-5
- require net-snmp for php-snmp (#174800)

* Sun Dec  4 2005 Joe Orton <jorton@redhat.com> 5.1.1-4
- add /usr/share/pear back to hard-coded include_path (#174885)

* Fri Dec  2 2005 Joe Orton <jorton@redhat.com> 5.1.1-3
- rebuild for httpd 2.2

* Mon Nov 28 2005 Joe Orton <jorton@redhat.com> 5.1.1-2
- update to 5.1.1
- remove pear subpackage
- enable pdo extensions (php-pdo subpackage)
- remove non-standard conditional module builds
- enable xmlreader extension

* Thu Nov 10 2005 Tomas Mraz <tmraz@redhat.com> 5.0.5-6
- rebuilt against new openssl

* Mon Nov  7 2005 Joe Orton <jorton@redhat.com> 5.0.5-5
- pear: update to XML_RPC 1.4.4, XML_Parser 1.2.7, Mail 1.1.9 (#172528)

* Tue Nov  1 2005 Joe Orton <jorton@redhat.com> 5.0.5-4
- rebuild for new libnetsnmp

* Wed Sep 14 2005 Joe Orton <jorton@redhat.com> 5.0.5-3
- update to 5.0.5
- add fix for upstream #34435
- devel: require autoconf, automake (#159283)
- pear: update to HTTP-1.3.6, Mail-1.1.8, Net_SMTP-1.2.7, XML_RPC-1.4.1
- fix imagettftext et al (upstream, #161001)

* Thu Jun 16 2005 Joe Orton <jorton@redhat.com> 5.0.4-11
- ldap: restore ldap_start_tls() function

* Fri May  6 2005 Joe Orton <jorton@redhat.com> 5.0.4-10
- disable RPATHs in shared extensions (#156974)

* Tue May  3 2005 Joe Orton <jorton@redhat.com> 5.0.4-9
- build simplexml_import_dom even with shared dom (#156434)
- prevent truncation of copied files to ~2Mb (#155916)
- install /usr/bin/php from CLI build alongside CGI
- enable sysvmsg extension (#142988)

* Mon Apr 25 2005 Joe Orton <jorton@redhat.com> 5.0.4-8
- prevent build of builtin dba as well as shared extension

* Wed Apr 13 2005 Joe Orton <jorton@redhat.com> 5.0.4-7
- split out dba and bcmath extensions into subpackages
- BuildRequire gcc-c++ to avoid AC_PROG_CXX{,CPP} failure (#155221)
- pear: update to DB-1.7.6
- enable FastCGI support in /usr/bin/php-cgi (#149596)

* Wed Apr 13 2005 Joe Orton <jorton@redhat.com> 5.0.4-6
- build /usr/bin/php with the CLI SAPI, and add /usr/bin/php-cgi,
  built with the CGI SAPI (thanks to Edward Rudd, #137704)
- add php(1) man page for CLI
- fix more test cases to use -n when invoking php

* Wed Apr 13 2005 Joe Orton <jorton@redhat.com> 5.0.4-5
- rebuild for new libpq soname

* Tue Apr 12 2005 Joe Orton <jorton@redhat.com> 5.0.4-4
- bundle from PEAR: HTTP, Mail, XML_Parser, Net_Socket, Net_SMTP
- snmp: disable MSHUTDOWN function to prevent error_log noise (#153988)
- mysqli: add fix for crash on x86_64 (Georg Richter, upstream #32282)

* Mon Apr 11 2005 Joe Orton <jorton@redhat.com> 5.0.4-3
- build shared objects as PIC (#154195)

* Mon Apr  4 2005 Joe Orton <jorton@redhat.com> 5.0.4-2
- fix PEAR installation and bundle PEAR DB-1.7.5 package

* Fri Apr  1 2005 Joe Orton <jorton@redhat.com> 5.0.4-1
- update to 5.0.4 (#153068)
- add .phps AddType to php.conf (#152973)
- better gcc4 fix for libxmlrpc

* Wed Mar 30 2005 Joe Orton <jorton@redhat.com> 5.0.3-5
- BuildRequire mysql-devel >= 4.1
- don't mark php.ini as noreplace to make upgrades work (#152171)
- fix subpackage descriptions (#152628)
- fix memset(,,0) in Zend (thanks to Dave Jones)
- fix various compiler warnings in Zend

* Thu Mar 24 2005 Joe Orton <jorton@redhat.com> 5.0.3-4
- package mysqli extension in php-mysql
- really enable pcntl (#142903)
- don't build with --enable-safe-mode (#148969)
- use "Instant Client" libraries for oci8 module (Kai Bolay, #149873)

* Fri Feb 18 2005 Joe Orton <jorton@redhat.com> 5.0.3-3
- fix build with GCC 4

* Wed Feb  9 2005 Joe Orton <jorton@redhat.com> 5.0.3-2
- install the ext/gd headers (#145891)
- enable pcntl extension in /usr/bin/php (#142903)
- add libmbfl array arithmetic fix (dcb314@hotmail.com, #143795)
- add BuildRequire for recent pcre-devel (#147448)

* Wed Jan 12 2005 Joe Orton <jorton@redhat.com> 5.0.3-1
- update to 5.0.3 (thanks to Robert Scheck et al, #143101)
- enable xsl extension (#142174)
- package both the xsl and dom extensions in php-xml
- enable soap extension, shared (php-soap package) (#142901)
- add patches from upstream 5.0 branch:
 * Zend_strtod.c compile fixes
 * correct php_sprintf return value usage

* Mon Nov 22 2004 Joe Orton <jorton@redhat.com> 5.0.2-8
- update for db4-4.3 (Robert Scheck, #140167)
- build against mysql-devel
- run tests in %%check

* Wed Nov 10 2004 Joe Orton <jorton@redhat.com> 5.0.2-7
- truncate changelog at 4.3.1-1
- merge from 4.3.x package:
 - enable mime_magic extension and Require: file (#130276)

* Mon Nov  8 2004 Joe Orton <jorton@redhat.com> 5.0.2-6
- fix dom/sqlite enable/without confusion

* Mon Nov  8 2004 Joe Orton <jorton@redhat.com> 5.0.2-5
- fix phpize installation for lib64 platforms
- add fix for segfault in variable parsing introduced in 5.0.2

* Mon Nov  8 2004 Joe Orton <jorton@redhat.com> 5.0.2-4
- update to 5.0.2 (#127980)
- build against mysqlclient10-devel
- use new RTLD_DEEPBIND to load extension modules
- drop explicit requirement for elfutils-devel
- use AddHandler in default conf.d/php.conf (#135664)
- "fix" round() fudging for recent gcc on x86
- disable sqlite pending audit of warnings and subpackage split

* Fri Sep 17 2004 Joe Orton <jorton@redhat.com> 5.0.1-4
- don't build dom extension into 2.0 SAPI

* Fri Sep 17 2004 Joe Orton <jorton@redhat.com> 5.0.1-3
- ExclusiveArch: x86 ppc x86_64 for the moment

* Fri Sep 17 2004 Joe Orton <jorton@redhat.com> 5.0.1-2
- fix default extension_dir and conf.d/php.conf

* Thu Sep  9 2004 Joe Orton <jorton@redhat.com> 5.0.1-1
- update to 5.0.1
- only build shared modules once
- put dom extension in php-dom subpackage again
- move extension modules into %%{_libdir}/php/modules
- don't use --with-regex=system, it's ignored for the apache* SAPIs

* Wed Aug 11 2004 Tom Callaway <tcallawa@redhat.com>
- Merge in some spec file changes from Jeff Stern (jastern@uci.edu)

* Mon Aug 09 2004 Tom Callaway <tcallawa@redhat.com>
- bump to 5.0.0
- add patch to prevent clobbering struct re_registers from regex.h
- remove domxml references, replaced with dom now built-in
- fix php.ini to refer to php5 not php4

* Wed Aug 04 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- rebuild

* Wed Jul 14 2004 Joe Orton <jorton@redhat.com> 4.3.8-3
- update to 4.3.8
- catch some fd > FD_SETSIZE vs select() issues (#125258)

* Mon Jun 21 2004 Joe Orton <jorton@redhat.com> 4.3.7-4
- pick up test failures again
- have -devel require php of same release

* Thu Jun 17 2004 Joe Orton <jorton@redhat.com> 4.3.7-3
- add gmp_powm fix (Oskari Saarenmaa, #124318)
- split mbstring, ncurses, gd, openssl extns into subpackages
- fix memory leak in apache2handler; use ap_r{write,flush}
  rather than brigade interfaces

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Jun  3 2004 Joe Orton <jorton@redhat.com> 4.3.7-1
- update to 4.3.7
- have -pear subpackage require php of same VR

* Wed May 26 2004 Joe Orton <jorton@redhat.com> 4.3.6-6
- buildrequire smtpdaemon (#124430)
- try switching to system libgd again (prevent symbol conflicts
  when e.g. mod_perl loads the system libgd library.)

* Wed May 19 2004 Joe Orton <jorton@redhat.com> 4.3.6-5
- don't obsolete php-imap (#123580)
- unconditionally build -imap subpackage

* Thu May 13 2004 Joe Orton <jorton@redhat.com> 4.3.6-4
- remove trigger

* Thu Apr 22 2004 Joe Orton <jorton@redhat.com> 4.3.6-3
- fix umask reset "feature" (#121454)
- don't use DL_GLOBAL when dlopen'ing extension modules

* Sun Apr 18 2004 Joe Orton <jorton@redhat.com> 4.3.6-2
- fix segfault on httpd SIGHUP (upstream #27810)

* Fri Apr 16 2004 Joe Orton <jorton@redhat.com> 4.3.6-1
- update to 4.3.6 (Robert Scheck, #121011)

* Wed Apr  7 2004 Joe Orton <jorton@redhat.com> 4.3.4-11
- add back imap subpackage, using libc-client (#115535)

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb 18 2004 Joe Orton <jorton@redhat.com> 4.3.4-10
- eliminate /usr/local/lib RPATH in odbc.so
- really use system pcre library

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com> 4.3.4-9
- rebuilt

* Mon Feb  2 2004 Bill Nottingham <notting@redhat.com> 4.3.4-8
- obsolete php-imap if we're not building it

* Wed Jan 28 2004 Joe Orton <jorton@redhat.com> 4.3.4-7
- gd fix for build with recent Freetype2 (from upstream)
- remove easter egg (Oden Eriksson, Mandrake)

* Wed Jan 21 2004 Joe Orton <jorton@redhat.com> 4.3.4-6
- php-pear requires php
- also remove extension=imap from php.ini in upgrade trigger
- merge from Taroon: allow upgrade from Stronghold 4.0

* Wed Jan 21 2004 Joe Orton <jorton@redhat.com> 4.3.4-5
- add defattr for php-pear subpackage
- restore defaults: output_buffering=Off, register_argc_argv=On
- add trigger to handle php.ini upgrades smoothly (#112470)

* Tue Jan 13 2004 Joe Orton <jorton@redhat.com> 4.3.4-4
- conditionalize support for imap extension for the time being
- switch /etc/php.ini to use php.ini-recommended (but leave
  variables_order as EGPCS) (#97765)
- set session.path to /var/lib/php/session by default (#89975)
- own /var/lib/php{,/session} and have apache own the latter
- split off php-pear subpackage (#83771)

* Sat Dec 13 2003 Jeff Johnson <jbj@jbj.org> 4.3.4-3
- rebuild against db-4.2.52.

* Mon Dec  1 2003 Joe Orton <jorton@redhat.com> 4.3.4-2
- rebuild for new libxslt (#110658)
- use --with-{mssql,oci8} for enabling extensions (#110482)
- fix rebuild issues (Jan Visser, #110274)
- remove hard-coded LIBS
- conditional support for mhash (Aleksander Adamowski, #111251)

* Mon Nov 10 2003 Joe Orton <jorton@redhat.com> 4.3.4-1.1
- rebuild for FC1 updates

* Mon Nov 10 2003 Joe Orton <jorton@redhat.com> 4.3.4-1
- update to 4.3.4
- include all licence files
- libxmlrpc fixes

* Mon Oct 20 2003 Joe Orton <jorton@redhat.com> 4.3.3-6
- use bundled libgd (#107407)
- remove manual: up-to-date manual sources are no longer DFSG-free;
  it's too big; it's on the web anyway; #91292, #105804, #107384

* Wed Oct 15 2003 Joe Orton <jorton@redhat.com> 4.3.3-5
- add php-xmlrpc subpackage (#107138)

* Mon Oct 13 2003 Joe Orton <jorton@redhat.com> 4.3.3-4
- drop recode support, symbols collide with MySQL

* Sun Oct 12 2003 Joe Orton <jorton@redhat.com> 4.3.3-3
- split domxml extension into php-domxml subpackage
- enable xslt and xml support in domxml extension (#106042)
- fix httpd-devel build requirement (#104341)
- enable recode extension (#106755)
- add workaround for #103982

* Thu Sep 25 2003 Jeff Johnson <jbj@jbj.org> 4.3.3-3
- rebuild against db-4.2.42.

* Sun Sep  7 2003 Joe Orton <jorton@redhat.com> 4.3.3-2
- don't use --enable-versioning, it depends on libtool being
 broken (#103690)

* Sun Sep  7 2003 Joe Orton <jorton@redhat.com> 4.3.3-1
- update to 4.3.3
- add libtool build prereq (#103388)
- switch to apache2handler

* Mon Jul 28 2003 Joe Orton <jorton@redhat.com> 4.3.2-8
- rebuild

* Tue Jul 22 2003 Nalin Dahyabhai <nalin@redhat.com> 4.3.2-7
- rebuild

* Tue Jul  8 2003 Joe Orton <jorton@redhat.com> 4.3.2-6
- use system pcre library

* Mon Jun  9 2003 Joe Orton <jorton@redhat.com> 4.3.2-5
- enable mbstring and mbregex (#81336)
- fix use of libtool 1.5

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun  3 2003 Joe Orton <jorton@redhat.com> 4.3.2-3
- add lib64 and domxml fixes

* Tue Jun  3 2003 Frank Dauer <f@paf.net>
- added conditional support for mssql module (#92149)

* Fri May 30 2003 Joe Orton <jorton@redhat.com> 4.3.2-2
- update the -tests and -lib64 patches
- fixes for db4 detection
- require aspell-devel >= 0.50.0 for pspell compatibility

* Thu May 29 2003 Joe Orton <jorton@redhat.com> 4.3.2-1
- update to 4.3.2

* Fri May 16 2003 Joe Orton <jorton@redhat.com> 4.3.1-3
- link odbc module correctly
- patch so that php -n doesn't scan inidir
- run tests using php -n, avoid loading system modules

* Wed May 14 2003 Joe Orton <jorton@redhat.com> 4.3.1-2
- workaround broken parser produced by bison-1.875

* Tue May  6 2003 Joe Orton <jorton@redhat.com> 4.3.1-1
- update to 4.3.1; run test suite
- open extension modules with RTLD_NOW rather than _LAZY