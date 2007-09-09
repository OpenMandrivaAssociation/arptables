Summary:	Userspace control program for the arptables network filter
Name:		arptables
Version:	0.0.3
Release:	%mkrel 5
Group:		System/Kernel and hardware
License:	GPL
URL:		http://ebtables.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/ebtables/%{name}-v%{version}-2.tar.bz2
#BuildRequires:  kernel-source >= 2.6.0
Requires:	kernel >= 2.6.0
BuildRoot:	%{_tmppath}/%{name}-v%{version}-root

%description
The arptables utility controls the arpfilter network packet
filtering code in the Linux kernel. You do not need this program
for normal network firewalling. If you need to manually control
which arp requests and/or replies this machine accepts and sends,
you should install this package.

%prep

%setup -q -n %{name}-v%{version}-2

%build

%make COPT_FLAGS="%{optflags}"

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}/sbin
install -d %{buildroot}%{_mandir}/man8

install -m755 arptables %{buildroot}/sbin/
install -m644 arptables.8 %{buildroot}%{_mandir}/man8/

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
#%doc ChangeLog INSTALL THANKS
%attr(0755,root,root) /sbin/arptables
%attr(0644,root,root) %{_mandir}/man8/arptables.8*
