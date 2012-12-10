Summary:	Userspace control program for the arptables network filter
Name:		arptables
Version:	0.0.3.4
Release:	%mkrel 1
Group:		System/Kernel and hardware
License:	GPLv2
URL:		http://ebtables.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/ebtables/%{name}-%{version}.tar.gz
BuildRequires:  kernel-source
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The arptables utility controls the arpfilter network packet
filtering code in the Linux kernel. You do not need this program
for normal network firewalling. If you need to manually control
which arp requests and/or replies this machine accepts and sends,
you should install this package.

%prep
%setup -q 

%build
%make COPT_FLAGS="%{optflags}" KERNEL_DIR=/usr/src/linux/include

%install
rm -rf %{buildroot}
install -d %{buildroot}/sbin
install -d %{buildroot}%{_mandir}/man8
install -m755 arptables %{buildroot}/sbin/
install -m644 arptables.8 %{buildroot}%{_mandir}/man8/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
#%doc ChangeLog INSTALL THANKS
%attr(0755,root,root) /sbin/arptables
%attr(0644,root,root) %{_mandir}/man8/arptables.8*


%changelog
* Mon Jul 12 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.0.3.4-1mdv2011.0
+ Revision: 551230
- update to 0.0.3.4 (with a little clean of %%prep)

* Tue Feb 23 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.0.3.3-1mdv2010.1
+ Revision: 509974
- remove old archive
- Fix archive and version
- fix license

* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 0.0.3-10mdv2010.0
+ Revision: 423957
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.0.3-9mdv2009.0
+ Revision: 266182
- rebuild early 2009.0 package (before pixel changes)

* Fri May 16 2008 Oden Eriksson <oeriksson@mandriva.com> 0.0.3-8mdv2009.0
+ Revision: 208135
- 0.0.3-3
- drop the redundant patch

* Wed Jan 16 2008 Thierry Vignaud <tv@mandriva.org> 0.0.3-7mdv2008.1
+ Revision: 153720
- remove useless kernel require
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - try to fix build (try #2)

* Sun Sep 09 2007 Oden Eriksson <oeriksson@mandriva.com> 0.0.3-5mdv2008.0
+ Revision: 83892
- try to fix build (try #1)
- rebuild


* Fri Dec 22 2006 Oden Eriksson <oeriksson@mandriva.com> 0.0.3-4mdv2007.0
+ Revision: 101555
- Import arptables

* Fri Dec 22 2006 Oden Eriksson <oeriksson@mandriva.com> 0.0.3-4
- pre x-mas rebuild :)

* Sun Jan 08 2006 Oden Eriksson <oeriksson@mandriva.com> 0.0.3-3mdk
- rebuild

* Fri Dec 24 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.0.3-2mdk
- x-mas rebuild :)

