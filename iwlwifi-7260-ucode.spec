%define	_fname	7260
%define	_module	7260
Summary:	Microcode image for Intel Wireless 7260
Name:		iwlwifi-%{_module}-ucode
Version:	25.228.9.0
Release:	1
License:	distributable
Group:		Base/Kernel
Source0:	http://wireless.kernel.org/en/users/Drivers/iwlwifi?action=AttachFile&do=get&target=iwlwifi-7260-ucode-22.1.7.0.tgz
# Source0-md5:	676447d12fe373d97b2db2b9849d297b
Source1:	http://wireless.kernel.org/en/users/Drivers/iwlwifi?action=AttachFile&do=get&target=iwlwifi-7260-ucode-22.24.8.0.tgz
# Source1-md5:	6ac0a3fc936acdd2351866a7af2fe9f7
Source2:	http://wireless.kernel.org/en/users/Drivers/iwlwifi?action=AttachFile&do=get&target=iwlwifi-7260-ucode-%{version}.tgz
# Source2-md5:	1bccc66bd8d641c9de05c2c5846c23ee
Source3:	http://wireless.kernel.org/en/users/Drivers/iwlwifi?action=AttachFile&do=get&target=iwlwifi-7260-ucode-23.11.10.0.tgz
# Source3-md5:	c59aa3f5395ccba356c2b09a38d21801
URL:		http://www.intellinuxwireless.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The file provided in this package must be present on your system in
order for the Intel Wireless 7260 driver for Linux
(iwlwifi-%{_module}) to operate on your system.

On adapter initialization, and at varying times during the uptime of
the adapter, the microcode is loaded into the RAM on the network
adapter. The microcode provides the low level MAC features including
radio control and high precision timing events (backoff, transmit,
etc.) while also providing varying levels of packet filtering which
can be used to keep the host from having to handle packets that are
not of interest given the current operating mode of the device.

%description -l pl.UTF-8
Plik dostarczany przez ten pakiet jest wymagany w systemie do
działania linuksowego sterownika dla układów bezprzewodowych Intel
Wireless 7260 (iwlwifi-%{_module}).

Przy inicjalizacji układu i w różnych chwilach w trakcie jego
działania mikrokod jest wczytywany do pamięci RAM układu. Mikrokod
udostępnia funkcje niskopoziomowe MAC, w tym sterowanie częścią
radiową i zdarzeniami wymagającymi dużej dokładności czasowej
(oczekiwania, transmisja itp.), a także różne poziomy filtrowania
pakietów, zapobiegające docieraniu do komputera pakietów
niepotrzebnych w danym trybie pracy urządzenia.

%prep
%setup -q -c -a0 -a1 -a2 -a3

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware

cp -p */iwlwifi-%{_fname}-*.ucode $RPM_BUILD_ROOT/lib/firmware
cp -p *%{version}/*LICENSE.* $RPM_BUILD_ROOT/lib/firmware/%{name}-LICENSE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *%{version}*/README.*
/lib/firmware/%{name}-LICENSE
/lib/firmware/*.ucode
