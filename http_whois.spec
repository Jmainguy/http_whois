%define _unpackaged_files_terminate_build 0
%define  debug_package %{nil}
Name:	http_whois
Version: 0.1
Release: 1%{?dist}
Summary: golang daemon which servers whois requests over http

License: GPLv2
URL: https://github.com/Jmainguy/http_whois
Source0: http_whois.tar.gz

%description
golang daemon which servers whois requests over http

%prep
%setup -q -n http_whois
%build
export GOPATH=/usr/src/go
/usr/bin/go build
%install
mkdir -p $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT/opt/http_whois
install -m 0755 $RPM_BUILD_DIR/http_whois/http_whois %{buildroot}/usr/sbin
install -m 0644 $RPM_BUILD_DIR/http_whois/favicon.ico %{buildroot}/opt/http_whois/

%files
/usr/sbin/http_whois
/opt/http_whois/favicon.ico
%dir /opt/http_whois
%doc

%pre
getent group http_whois >/dev/null || groupadd -r http_whois
getent passwd http_whois >/dev/null || \
    useradd -r -g http_whois -d /opt/http_whois -s /sbin/nologin \
    -c "User to run http_whois" http_whois
exit 0
%post
chown -R http_whois:http_whois /opt/http_whois

%changelog
* Wed Jun 06 2018 Jonathan Mainguy <jon@soh.re> - 0.1-1
- Initial init

