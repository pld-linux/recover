Summary:	recover lost file from ext2 partition
Summary(pl.UTF-8):	program do odzyskiwania plików z ext2
Name:		recover
Version:	1.3c
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://recover.sourceforge.net/linux/recover/download/%{name}-%{version}.tar.gz
# Source0-md5:	34112eaeec1f60cec6cd296e1bafe311
URL:		http://recover.sourceforge.net/linux/recover/
Requires:	e2fsprogs >= 1.19
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Recover is a utility which automates some steps as described in the
Ext2fs-Undeletion howto in order to recover a lost file.

%description -l pl.UTF-8
Recover jest narzędziem, które automatyzuje proces odzyskiwania
straconego pliku opisany w dokumencie Ext2fs-Undeletion howto.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -x c"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man1,%{_datadir}/%{name}}

install recover $RPM_BUILD_ROOT%{_sbindir}
install *.1* $RPM_BUILD_ROOT%{_mandir}/man1
install recover_questions $RPM_BUILD_ROOT%{_datadir}/%{name}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
%attr(755,root,root) %{_sbindir}/*
%{_datadir}/%{name}
%{_mandir}/man*/*
