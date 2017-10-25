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
Version:    XXX
Release:    XXX
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
BuildRequires: python-setuptools
BuildRequires: python-pbr
BuildRequires: python-cachetools
BuildRequires: python-futurist
BuildRequires: python-redis
BuildRequires: python-zmq
# Required for tests
BuildRequires: python-fixtures
BuildRequires: python-hacking
BuildRequires: python-kafka
BuildRequires: python-kombu >= 1:4.0.0
BuildRequires: python-mock
BuildRequires: python-mox3
BuildRequires: python-oslo-config
BuildRequires: python-oslo-context
BuildRequires: python-oslo-middleware
BuildRequires: python-oslo-serialization
BuildRequires: python-oslo-service
BuildRequires: python-oslo-utils
BuildRequires: python-oslotest
BuildRequires: python-pifpaf
BuildRequires: python-subunit
BuildRequires: python-tenacity
BuildRequires: python-testrepository
BuildRequires: python-testscenarios
BuildRequires: python-testtools


Requires:   python-amqp >= 2.1.0
Requires:   python-debtcollector >= 1.2.0
Requires:   python-setuptools
Requires:   python-iso8601
Requires:   python-futures >= 3.0
Requires:   python-futurist >= 0.11.0
Requires:   python-monotonic >= 0.6
Requires:   python-oslo-config >= 2:4.0.0
Requires:   python-oslo-context >= 2.9.0
Requires:   python-oslo-utils >= 3.20.0
Requires:   python-oslo-serialization >= 1.10.0
Requires:   python-oslo-service >= 1.10.0
Requires:   python-oslo-i18n >= 2.1.0
Requires:   python-oslo-log >= 3.22.0
Requires:   python-oslo-middleware >= 3.27.0
Requires:   python-six >= 1.9.0
Requires:   python-stevedore >= 1.20.0
Requires:   python-tenacity
Requires:   PyYAML
Requires:   python-kombu >= 1:4.0.0
Requires:   python-babel
Requires:   python-eventlet
Requires:   python-cachetools
Requires:   python-pika >= 0.10.0
Requires:   python-pika_pool
Requires:   python-webob >= 1.7.1
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

BuildRequires: python-sphinx
BuildRequires: python-openstackdocstheme
BuildRequires: python-oslo-sphinx

# for API autodoc
BuildRequires: python-iso8601
BuildRequires: python-oslo-config
BuildRequires: python-oslo-context
BuildRequires: python-oslo-i18n
BuildRequires: python-oslo-middleware
BuildRequires: python-oslo-serialization
BuildRequires: python-oslo-service
BuildRequires: python-oslo-utils
BuildRequires: python-six
BuildRequires: python-stevedore
BuildRequires: PyYAML
BuildRequires: python-babel
BuildRequires: python-fixtures
BuildRequires: python-kombu >= 1:4.0.0
BuildRequires: python-pika_pool
%if 0%{rhosp} == 0
BuildRequires: python-pyngus
%endif


%description -n python-%{pkg_name}-doc
Documentation for the oslo.messaging library.
%endif

%package -n python2-%{pkg_name}-tests
Summary:    Tests for OpenStack common messaging library

Requires:      python-%{pkg_name} = %{version}-%{release}
Requires:      python-kafka
Requires:      python-oslo-config
Requires:      python-oslo-context
Requires:      python-oslo-middleware
Requires:      python-oslo-serialization
Requires:      python-oslo-service
Requires:      python-oslo-utils
Requires:      python-oslotest
Requires:      python-testrepository
Requires:      python-testscenarios
Requires:      python-testtools

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
BuildRequires: python3-oslo-context
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

Requires:   python3-amqp >= 2.1.0
Requires:   python3-debtcollector >= 1.2.0
Requires:   python3-setuptools
Requires:   python3-iso8601
Requires:   python3-futurist >= 0.11.0
Requires:   python3-monotonic >= 0.6
Requires:   python3-oslo-config >= 2:4.0.0
Requires:   python3-oslo-context >= 2.9.0
Requires:   python3-oslo-utils >= 3.20.0
Requires:   python3-oslo-serialization >= 1.10.0
Requires:   python3-oslo-service >= 1.10.0
Requires:   python3-oslo-i18n >= 2.1.0
Requires:   python3-oslo-log >= 3.22.0
Requires:   python3-oslo-middleware >= 3.27.0
Requires:   python3-six >= 1.9.0
Requires:   python3-stevedore >= 1.20.0
Requires:   python3-tenacity
Requires:   python3-PyYAML
Requires:   python3-kombu >= 1:4.0.0
Requires:   python3-babel
Requires:   python3-eventlet
Requires:   python3-cachetools
Requires:   python3-pika >= 0.10.0
Requires:   python3-pika_pool
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
Requires:      python3-oslo-context
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
%{__python2} setup.py build_sphinx -b html
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
