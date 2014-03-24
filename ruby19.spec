%define rubyver 1.9.3
%define rubyminorver p545
%define prefix /opt/ruby/ruby-%{rubyver}-%{rubyminorver}

Name: ruby19
Version: %{rubyver}%{rubyminorver}
Release: 1%{?dist}
License: Ruby License/GPL - see COPYING
URL: http://www.ruby-lang.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: automake zlib zlib-devel readline libyaml libyaml-devel readline-devel ncurses ncurses-devel gdbm gdbm-devel glibc-devel tcl-devel gcc unzip openssl-devel db4-devel byacc make libffi-devel
Requires: libyaml
Source0: ftp://ftp.ruby-lang.org/pub/ruby/ruby-%{rubyver}-%{rubyminorver}.tar.gz
Summary: An interpreter of object-oriented scripting language
Group: Development/Languages

%description
Ruby is the interpreted scripting language for quick and easy
object-oriented programming. It has many features to process text
files and to do system management tasks (as in Perl). It is simple,
straight-forward, and extensible.

%prep
%setup -n ruby-%{rubyver}-%{rubyminorver}

%build
export CFLAGS="$RPM_OPT_FLAGS -Wall -fno-strict-aliasing"

#./configure --prefix=/opt/ruby/ruby-%{rubyver}-%{rubyminorver}
./configure --prefix=%{prefix} --disable-rpath --without-X11 --without-tk

make %{?_smp_mflags}

%install
# installing binaries ...
make install DESTDIR=$RPM_BUILD_ROOT

#we don't want to keep the src directory
rm -rf $RPM_BUILD_ROOT/usr/src

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{prefix}

%changelog
* Wed Dec 11 2013 Eugene Vilensky <evilensky@gmail.com>
- Modified paths
