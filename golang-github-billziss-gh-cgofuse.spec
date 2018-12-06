# Run tests in check section
# Deactivating test: tests depends on fuse being present and fuse.ko being 
# loaded but the chroot doesn't allow to insert module.
%bcond_with check

%global goipath         github.com/billziss-gh/cgofuse
Version:                1.1.0

%global common_description %{expand:
Cross-platform FUSE library for Go.}

%gometa

Name:    %{goname}
Release: 4%{?dist}
Summary: Cross-platform FUSE library for Go
License: MIT
URL:     %{gourl}
Source:  %{gosource}

%description
%{common_description}


%package    devel
Summary:    %{summary}
BuildArch:  noarch
 
%description devel
%{common_description}
 
This package contains the source code needed for building packages that import
the %{goipath} Go namespace.


%prep
%forgesetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license License.txt
%doc README.md Changelog.md


%changelog
* Mon Nov 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.0-4
- SPEC refresh

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 1.1.0-3
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.0-1
- Upstream release 1.1.0

* Thu Mar 08 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.4-2
- Update with the new Go packaging

* Thu Dec 07 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.4-1
- Upstream release 1.0.4

* Mon Jul 24 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.2-1
- First package for Fedora
