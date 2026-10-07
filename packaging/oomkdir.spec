Name:           oomkdir
Version:        0.1.0
Release:        1%{?dist}
Summary:        Atomic multi-level directory creator with explicit permission mask enforcement.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oomkdir
Source0:        oomkdir-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oomkdir is a sovereign, capability-bounded DIRECTORY MAKER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oomkdir
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oomkdir-uninstall

%files
/usr/bin/oomkdir
/usr/bin/oomkdir-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
