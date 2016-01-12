%define	_fname	7260
%define	_module	7260
Summary:	Microcode image for Intel Wireless 7260
Name:		iwlwifi-%{_module}-ucode
Version:	25.228.9.0
Release:	7
License:	distributable
Group:		Base/Kernel
Source0:	https://wireless.wiki.kernel.org/_media/en/users/drivers/iwlwifi-7260-ucode-22.1.7.0.tgz
# Source0-md5:	676447d12fe373d97b2db2b9849d297b
Source1:	https://wireless.wiki.kernel.org/_media/en/users/drivers/iwlwifi-7260-ucode-22.24.8.0.tgz
# Source1-md5:	6ac0a3fc936acdd2351866a7af2fe9f7
Source2:	https://wireless.wiki.kernel.org/_media/en/users/drivers/iwlwifi-7260-ucode-25.228.9.0.tgz
# Source2-md5:	1bccc66bd8d641c9de05c2c5846c23ee
Source3:	https://wireless.wiki.kernel.org/_media/en/users/drivers/iwlwifi-7260-ucode-23.15.10.0.tgz
# Source3-md5:	b0b5e10eefd366b5b93da00657cb173c
Source4:	https://wireless.wiki.kernel.org/_media/en/users/drivers/iwlwifi-7260-ucode-25.17.12.0.tgz
# Source4-md5:	74a0f71b1ede12a0aed3149068e87acf
Source5:	https://wireless.wiki.kernel.org/_media/en/users/drivers/iwlwifi-7260-ucode-25.30.13.0.tgz
# Source5-md5:	892d1de0d2b597da2238922b7f53a24e
Source6:	https://wireless.wiki.kernel.org/_media/en/users/drivers/iwlwifi-7260-ucode-25.30.14.0.tgz
# Source6-md5:	00be8ebbc9165469560aeef1c8a9b35d
Source7:	https://wireless.wiki.kernel.org/_media/en/users/drivers/iwlwifi-7260-ucode-15.227938.0.tgz
# Source7-md5:	1ff0821014d87268d067c82680c107a7
Source8:	https://wireless.wiki.kernel.org/_media/en/users/drivers/iwlwifi-7260-ucode-16.242414.0.tgz
# Source8-md5:	6e3da0eb88c0f343ceb01a82ad7138eb
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
%setup -q -c -a0 -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8

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
