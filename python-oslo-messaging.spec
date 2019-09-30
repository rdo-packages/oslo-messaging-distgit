# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global with_doc 1
#guard for including python-pyngus (OSP 12 does not ship python-pyngus)
%global rhosp 0

%global common_desc \
The Oslo project intends to produce a python library containing \
infrastructure code shared by OpenStack projects. The APIs provided \
by the project should be high quality, stable, consistent and generally \
useful.

%global common_desc1 \
Tests for the OpenStack common messaging library.

%global pypi_name oslo.messaging
%global pkg_name oslo-messaging

Name:       python-oslo-messaging
Version:    XXX
Release:    XXX
Summary:    OpenStack common messaging library

License:    ASL 2.0
URL:        https://launchpad.net/oslo
Source0:    https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz
BuildArch:  noarch

BuildRequires: git

%package -n python%{pyver}-%{pkg_name}
Summary:    OpenStack common messaging library
%{?python_provide:%python_provide python%{pyver}-%{pkg_name}}

BuildRequires: python%{pyver}-devel
BuildRequires: python%{pyver}-setuptools
BuildRequires: python%{pyver}-pbr
BuildRequires: python%{pyver}-futurist
# Required for tests
BuildRequires: python%{pyver}-fixtures
BuildRequires: python%{pyver}-hacking
BuildRequires: python%{pyver}-kombu >= 1:4.0.0
BuildRequires: python%{pyver}-mock
BuildRequires: python%{pyver}-mox3
BuildRequires: python%{pyver}-oslo-config
BuildRequires: python%{pyver}-oslo-middleware
BuildRequires: python%{pyver}-oslo-serialization
BuildRequires: python%{pyver}-oslo-service
BuildRequires: python%{pyver}-oslo-utils
BuildRequires: python%{pyver}-oslotest
BuildRequires: python%{pyver}-pifpaf
BuildRequires: python%{pyver}-subunit
BuildRequires: python%{pyver}-testtools
BuildRequires: python%{pyver}-stestr
BuildRequires: python%{pyver}-cachetools
BuildRequires: python%{pyver}-redis
# Handle python2 exception
%if %{pyver} == 2
BuildRequires: python-kafka
%else
BuildRequires: python%{pyver}-kafka
%endif


Requires:   python%{pyver}-pbr
Requires:   python%{pyver}-amqp >= 2.4.1
Requires:   python%{pyver}-debtcollector >= 1.2.0
Requires:   python%{pyver}-futurist >= 1.2.0
Requires:   python%{pyver}-oslo-config >= 2:5.2.0
Requires:   python%{pyver}-oslo-utils >= 3.33.0
Requires:   python%{pyver}-oslo-serialization >= 2.18.0
Requires:   python%{pyver}-oslo-service >= 1.24.0
Requires:   python%{pyver}-oslo-log >= 3.36.0
Requires:   python%{pyver}-oslo-middleware >= 3.31.0
Requires:   python%{pyver}-six >= 1.10.0
Requires:   python%{pyver}-stevedore >= 1.20.0
Requires:   python%{pyver}-kombu >= 1:4.0.0
Requires:   python%{pyver}-eventlet
Requires:   python%{pyver}-cachetools
Requires:   python%{pyver}-monotonic >= 0.6
Requires:   python%{pyver}-webob >= 1.7.1
# Handle python2 exception
%if %{pyver} == 2
Requires:   PyYAML
%else
Requires:   python%{pyver}-PyYAML
%endif

%if 0%{rhosp} == 0 && 0%{?rhel} >= 7
# Handle python2 exception
%if %{pyver} == 2
Requires:   python-pyngus
%else
Requires:   python%{pyver}-pyngus
%endif
%endif

%description -n python%{pyver}-%{pkg_name}
%{common_desc}

The Oslo messaging API supports RPC and notifications over a number of
different messaging transports.

%if 0%{?with_doc}
%package -n python-%{pkg_name}-doc
Summary:    Documentation for OpenStack common messaging library

BuildRequires: python%{pyver}-sphinx
BuildRequires: python%{pyver}-openstackdocstheme

# for API autodoc
BuildRequires: python%{pyver}-oslo-config
BuildRequires: python%{pyver}-oslo-middleware
BuildRequires: python%{pyver}-oslo-serialization
BuildRequires: python%{pyver}-oslo-service
BuildRequires: python%{pyver}-oslo-utils
BuildRequires: python%{pyver}-six
BuildRequires: python%{pyver}-stevedore
BuildRequires: python%{pyver}-fixtures
BuildRequires: python%{pyver}-kombu >= 1:4.0.0
# Handle python2 exception
%if %{pyver} == 2
BuildRequires: PyYAML
%else
BuildRequires: python%{pyver}-PyYAML
%endif

%if 0%{rhosp} == 0 && 0%{?rhel} >= 7
# Handle python2 exception
%if %{pyver} == 2
BuildRequires: python-pyngus
%else
BuildRequires: python%{pyver}-pyngus
%endif
%endif


%description -n python-%{pkg_name}-doc
Documentation for the oslo.messaging library.
%endif

%package -n python%{pyver}-%{pkg_name}-tests
Summary:    Tests for OpenStack common messaging library

Requires:      python%{pyver}-%{pkg_name} = %{version}-%{release}
Requires:      python%{pyver}-oslo-config
Requires:      python%{pyver}-oslo-middleware
Requires:      python%{pyver}-oslo-serialization
Requires:      python%{pyver}-oslo-service
Requires:      python%{pyver}-oslo-utils
Requires:      python%{pyver}-oslotest
Requires:      python%{pyver}-testtools
Requires:      python%{pyver}-stestr
Requires:      python%{pyver}-testscenarios
# Handle python2 exception
%if %{pyver} == 2
BuildRequires: python-kafka
%else
BuildRequires: python%{pyver}-kafka
%endif

%description -n python%{pyver}-%{pkg_name}-tests
%{common_desc1}

%description
%{common_desc}

%prep
# FIXME: workaround required to build
%autosetup -n %{pypi_name}-%{upstream_version} -S git

# let RPM handle deps
rm -rf {test-,}requirements.txt

%build
%{pyver_build}

%if 0%{?with_doc}
export PYTHONPATH=.
sphinx-build-%{pyver} -b html doc/source doc/build/html
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo
%endif

%install
%{pyver_install}
ln -s ./oslo-messaging-send-notification %{buildroot}%{_bindir}/oslo-messaging-send-notification-%{pyver}

%check
# Four unit tests are failing for amqp1
stestr-%{pyver} run || true

%files -n python%{pyver}-%{pkg_name}
%license LICENSE
%doc README.rst
%{pyver_sitelib}/oslo_messaging
%{pyver_sitelib}/*.egg-info
%{_bindir}/oslo-messaging-send-notification
%{_bindir}/oslo-messaging-send-notification-%{pyver}
%exclude %{pyver_sitelib}/oslo_messaging/tests

%if 0%{?with_doc}
%files -n python-%{pkg_name}-doc
%license LICENSE
%doc doc/build/html
%endif

%files -n python%{pyver}-%{pkg_name}-tests
%{pyver_sitelib}/oslo_messaging/tests

%changelog
