%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?pyver: %define pyver %(%{__python} -c "import sys ; print sys.version[:3]")}

%define module turbocheetah

Name:           python-turbocheetah
Version:        1.0
Release:        5.1%{?dist}
Summary:        TurboGears plugin to support use of Cheetah templates

Group:          Development/Languages
License:        MIT
URL:            http://pypi.python.org/pypi/TurboCheetah
Source0:        http://cheeseshop.python.org/packages/source/T/TurboCheetah/TurboCheetah-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python-devel python-setuptools-devel
Requires:       python-cheetah >= 2.0.1

%description
This package provides a template engine plugin, allowing you
to easily use Cheetah with TurboGears, Buffet and other tools that
support the python.templating.engines entry point.


%prep
%setup -q -n TurboCheetah-%{version}


%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
rm -fr %{buildroot}/%{python_sitelib}/%{module}/tests


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README.txt
%{python_sitelib}/%{module}/
%{python_sitelib}/TurboCheetah-%{version}-py%{pyver}.egg-info


%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.0-5.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.0-3
- Rebuild for Python 2.6

* Sat Dec 15 2007 Luke Macken <lmacken@redhat.com> - 1.0-2
- Require python-cheetah >= 2.0.1

* Tue Dec  4 2007 Luke Macken <lmacken@redhat.com> - 1.0-1
- 1.0

* Fri Oct 26 2007 Luke Macken <lmacken@redhat.com> - 0.9.5-9
- Fix broken URL (#353951)

* Sun Sep  2 2007 Luke Macken <lmacken@redhat.com> - 0.9.5-8
- Update for python-setuptools changes in rawhide

* Sat Dec  9 2006 Luke Macken <lmacken@redhat.com> - 0.9.5-7
- Add python-devel to BuildRequires

* Fri Dec  8 2006 Luke Macken <lmacken@redhat.com> - 0.9.5-6
- Rebuild for new python

* Tue Oct 17 2006 Luke Macken <lmacken@redhat.com> - 0.9.5-5
- python-turbocheetah-0.9.5-setuptools.patch

* Tue Oct 10 2006 Luke Macken <lmacken@redhat.com> - 0.9.5-4
- Fix Source0
- Own %%{python_sitelib}/turbocheetah

* Fri Oct  6 2006 Luke Macken <lmacken@redhat.com> - 0.9.5-3
- Add python-setuptools to BuildRequires
- Remove tests directory

* Sat Sep 30 2006 Luke Macken <lmacken@redhat.com> - 0.9.5-2
- Rename to python-turbocheetah
- Install egg-info
- Add README

* Sat Sep 16 2006 Luke Macken <lmacken@redhat.com> - 0.9.5-1
- Initial creation
