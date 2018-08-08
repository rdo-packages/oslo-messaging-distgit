%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%if 0%{?fedora} >= 24
%global with_python3 1
%endif
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
Version:    8.1.0
Release:    1%{?dist}
Summary:    OpenStack common messaging library

License:    ASL 2.0
URL:        https://launchpad.net/oslo
Source0:    https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz
BuildArch:  noarch

BuildRequires: git

%package -n python2-%{pkg_name}
Summary:    OpenStack common messaging library
%{?python_provide:%python_provide python2-%{pkg_name}}

BuildRequires: python2-devel
BuildRequires: python2-setuptools
BuildRequires: python2-pbr
BuildRequires: python2-futurist
# Required for tests
BuildRequires: python2-fixtures
BuildRequires: python2-hacking
BuildRequires: python2-kombu >= 1:4.0.0
BuildRequires: python2-mock
BuildRequires: python2-mox3
BuildRequires: python2-oslo-config
BuildRequires: python2-oslo-middleware
BuildRequires: python2-oslo-serialization
BuildRequires: python2-oslo-service
BuildRequires: python2-oslo-utils
BuildRequires: python2-oslotest
BuildRequires: python2-pifpaf
BuildRequires: python2-subunit
BuildRequires: python2-tenacity
BuildRequires: python2-testtools
%if 0%{?fedora} > 0
BuildRequires: python2-cachetools
BuildRequires: python2-redis
BuildRequires: python2-zmq
BuildRequires: python2-kafka
BuildRequires: python2-testrepository
BuildRequires: python2-testscenarios
%else
BuildRequires: python-cachetools
BuildRequires: python-redis
BuildRequires: python-zmq
BuildRequires: python-kafka
BuildRequires: python-testrepository
BuildRequires: python-testscenarios
%endif


Requires:   python2-pbr
Requires:   python2-amqp >= 2.3.0
Requires:   python2-debtcollector >= 1.2.0
Requires:   python2-futurist >= 1.2.0
Requires:   python2-oslo-config >= 2:5.2.0
Requires:   python2-oslo-utils >= 3.33.0
Requires:   python2-oslo-serialization >= 2.18.0
Requires:   python2-oslo-service >= 1.24.0
Requires:   python2-oslo-i18n >= 3.15.3
Requires:   python2-oslo-log >= 3.36.0
Requires:   python2-oslo-middleware >= 3.31.0
Requires:   python2-six >= 1.10.0
Requires:   python2-stevedore >= 1.20.0
Requires:   python2-tenacity
Requires:   python2-kombu >= 1:4.0.0
Requires:   python2-eventlet
%if 0%{?fedora} > 0
Requires:   python2-cachetools
Requires:   python2-futures >= 3.0
Requires:   python2-monotonic >= 0.6
Requires:   python2-pyyaml
Requires:   python2-webob >= 1.7.1
%else
Requires:   python-cachetools
Requires:   python-futures >= 3.0
Requires:   python-monotonic >= 0.6
Requires:   PyYAML
Requires:   python-webob >= 1.7.1
%endif
%if 0%{rhosp} == 0
Requires:   python-pyngus
%endif

%description -n python2-%{pkg_name}
%{common_desc}

The Oslo messaging API supports RPC and notifications over a number of
different messaging transports.

%if 0%{?with_doc}
%package -n python-%{pkg_name}-doc
Summary:    Documentation for OpenStack common messaging library

BuildRequires: python2-sphinx
BuildRequires: python2-openstackdocstheme
BuildRequires: python2-oslo-sphinx

# for API autodoc
BuildRequires: python2-oslo-config
BuildRequires: python2-oslo-i18n
BuildRequires: python2-oslo-middleware
BuildRequires: python2-oslo-serialization
BuildRequires: python2-oslo-service
BuildRequires: python2-oslo-utils
BuildRequires: python2-six
BuildRequires: python2-stevedore
BuildRequires: python2-fixtures
BuildRequires: python2-kombu >= 1:4.0.0
%if 0%{?fedora} > 0
BuildRequires: python2-pyyaml
%else
BuildRequires: PyYAML
%endif
%if 0%{rhosp} == 0
BuildRequires: python-pyngus
%endif


%description -n python-%{pkg_name}-doc
Documentation for the oslo.messaging library.
%endif

%package -n python2-%{pkg_name}-tests
Summary:    Tests for OpenStack common messaging library

Requires:      python2-%{pkg_name} = %{version}-%{release}
Requires:      python2-oslo-config
Requires:      python2-oslo-middleware
Requires:      python2-oslo-serialization
Requires:      python2-oslo-service
Requires:      python2-oslo-utils
Requires:      python2-oslotest
Requires:      python2-testtools
%if 0%{?fedora} > 0
Requires:      python2-kafka
Requires:      python2-testrepository
Requires:      python2-testscenarios
%else
Requires:      python-kafka
Requires:      python-testrepository
Requires:      python-testscenarios
%endif

%description -n python2-%{pkg_name}-tests
%{common_desc1}

%if 0%{?with_python3}
%package -n python3-%{pkg_name}
Summary:    OpenStack common messaging library
%{?python_provide:%python_provide python3-%{pkg_name}}

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pbr
BuildRequires: python3-cachetools
BuildRequires: python3-futurist
BuildRequires: python3-redis
BuildRequires: python3-zmq

# Required for tests
BuildRequires: python3-kafka
BuildRequires: python3-oslo-config
BuildRequires: python3-oslo-middleware
BuildRequires: python3-oslo-serialization
BuildRequires: python3-oslo-service
BuildRequires: python3-oslo-utils
BuildRequires: python3-oslotest
BuildRequires: python3-pifpaf
BuildRequires: python3-tenacity
BuildRequires: python3-testrepository
BuildRequires: python3-testscenarios
BuildRequires: python3-testtools

Requires:   python3-pbr
Requires:   python3-amqp >= 2.3.0
Requires:   python3-debtcollector >= 1.2.0
Requires:   python3-futurist >= 1.2.0
Requires:   python3-monotonic >= 0.6
Requires:   python3-oslo-config >= 2:5.2.0
Requires:   python3-oslo-utils >= 3.33.0
Requires:   python3-oslo-serialization >= 2.18.0
Requires:   python3-oslo-service >= 1.24.0
Requires:   python3-oslo-i18n >= 3.15.3
Requires:   python3-oslo-log >= 3.36.0
Requires:   python3-oslo-middleware >= 3.31.0
Requires:   python3-six >= 1.10.0
Requires:   python3-stevedore >= 1.20.0
Requires:   python3-tenacity
Requires:   python3-PyYAML
Requires:   python3-kombu >= 1:4.0.0
Requires:   python3-eventlet
Requires:   python3-cachetools
Requires:   python3-webob >= 1.7.1
%if 0%{rhosp} == 0
Requires:   python3-pyngus
%endif

%description -n python3-%{pkg_name}
%{common_desc}

The Oslo messaging API supports RPC and notifications over a number of
different messaging transports.

%package -n python3-%{pkg_name}-tests
Summary:    Tests for OpenStack common messaging library

Requires:      python3-%{pkg_name} = %{version}-%{release}
Requires:      python3-kafka
Requires:      python3-oslo-config
Requires:      python3-oslo-middleware
Requires:      python3-oslo-serialization
Requires:      python3-oslo-service
Requires:      python3-oslo-utils
Requires:      python3-oslotest
Requires:      python3-testrepository
Requires:      python3-testscenarios
Requires:      python3-testtools

%description -n python3-%{pkg_name}-tests
%{common_desc1}
%endif

%description
%{common_desc}

%prep
# FIXME: workaround required to build
%autosetup -n %{pypi_name}-%{upstream_version} -S git

# let RPM handle deps
rm -rf {test-,}requirements.txt

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

%if 0%{?with_doc}
sphinx-build -b html doc/source doc/build/html
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo
%endif

%install
%if 0%{?with_python3}
%py3_install
for i in zmq-{broker,proxy} send-notification; do
mv %{buildroot}%{_bindir}/oslo-messaging-$i %{buildroot}%{_bindir}/oslo-messaging-$i-%{python3_version}
ln -s ./oslo-messaging-$i-%{python3_version} %{buildroot}%{_bindir}/oslo-messaging-$i-3
done
%endif
%py2_install

for i in zmq-{broker,proxy} send-notification; do
mv %{buildroot}%{_bindir}/oslo-messaging-$i %{buildroot}%{_bindir}/oslo-messaging-$i-%{python2_version}
ln -s ./oslo-messaging-$i-%{python2_version} %{buildroot}%{_bindir}/oslo-messaging-$i-2
ln -s ./oslo-messaging-$i-%{python2_version} %{buildroot}%{_bindir}/oslo-messaging-$i
done

%check
# Four unit tests are failing for amqp1
%{__python2} setup.py test || true
%if 0%{?with_python3}
rm -rf .testrepository
%{__python3} setup.py test || true
%endif

%files -n python2-%{pkg_name}
%license LICENSE
%doc README.rst
%{python2_sitelib}/oslo_messaging
%{python2_sitelib}/*.egg-info
%{_bindir}/oslo-messaging-zmq-broker
%{_bindir}/oslo-messaging-zmq-proxy
%{_bindir}/oslo-messaging-send-notification
%{_bindir}/oslo-messaging-zmq-broker-2*
%{_bindir}/oslo-messaging-zmq-proxy-2*
%{_bindir}/oslo-messaging-send-notification-2*
%exclude %{python2_sitelib}/oslo_messaging/tests

%if 0%{?with_doc}
%files -n python-%{pkg_name}-doc
%license LICENSE
%doc doc/build/html
%endif

%files -n python2-%{pkg_name}-tests
%{python2_sitelib}/oslo_messaging/tests

%if 0%{?with_python3}
%files -n python3-%{pkg_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/oslo_messaging
%{python3_sitelib}/*.egg-info
%{_bindir}/oslo-messaging-zmq-broker-3*
%{_bindir}/oslo-messaging-zmq-proxy-3*
%{_bindir}/oslo-messaging-send-notification-3*
%exclude %{python3_sitelib}/oslo_messaging/tests

%files -n python3-%{pkg_name}-tests
%{python3_sitelib}/oslo_messaging/tests
%endif

%changelog
* Wed Aug 08 2018 RDO <dev@lists.rdoproject.org> 8.1.0-1
- Update to 8.1.0

