Summary:	recover lost file from ext2 partition
Summary(pl):	program do odzyskiwania plików z ext2
Name:		recover
Version:	1.2
Release:	1
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	http://www.linuxave.net/~recover/download/%{name}-%{version}.tar.gz
URL:		http://www.linuxave.net/~recover/
Requires:	e2fsprogs >= 1.19
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Recover is a utility which automates some steps as described in the
Ext2fs-Undeletion howto in order to recover a lost file.

%description -l pl
Recover jest narzêdziem, które automatyzuje proces odzyskiwania
straconego pliku opisany w dokumencie Ext2fs-Undeletion howto.

%prep
%setup -q

%build
%{__make} CFLAGS="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O -g} -x c"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man1,%{_datadir}/%{name}}

install recover $RPM_BUILD_ROOT%{_sbindir}
install *.1* $RPM_BUILD_ROOT%{_mandir}/man1
install recover_questions $RPM_BUILD_ROOT%{_datadir}/%{name}

gzip -9nf README CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_sbindir}/*
%{_datadir}/%{name}
%{_mandir}/man*/*
