Summary:	Userspace control program for the arptables network filter
Name:		arptables
Version:	0.0.4
Release:	2
Group:		System/Kernel and hardware
License:	GPLv2
URL:		http://ebtables.sourceforge.net/
Source0:	https://sourceforge.net/projects/ebtables/files/arptables/arptables-v0.0.4/%{name}-v%{version}.tar.gz
BuildRequires:  kernel-source

%description
The arptables utility controls the arpfilter network packet
filtering code in the Linux kernel. You do not need this program
for normal network firewalling. If you need to manually control
which arp requests and/or replies this machine accepts and sends,
you should install this package.

%prep
%setup -qn %{name}-v%{version}

%build
%make COPT_FLAGS="%{optflags}" KERNEL_DIR=/usr/src/linux/include

%install
install -d %{buildroot}/sbin
install -d %{buildroot}%{_mandir}/man8
install -m755 arptables %{buildroot}/sbin/
install -m644 arptables.8 %{buildroot}%{_mandir}/man8/

%clean

%files
%defattr(-,root,root,0755)
#%doc ChangeLog INSTALL THANKS
%attr(0755,root,root) /sbin/arptables
%attr(0644,root,root) %{_mandir}/man8/arptables.8*
