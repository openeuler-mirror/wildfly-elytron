%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:                wildfly-elytron
Version:             1.0.2
Release:             3
Summary:             Security, Authentication, and Authorization SPIs for the WildFly project
License:             ASL 2.0 and LGPLv2+
URL:                 http://wildfly.org/
Source0:             https://github.com/wildfly-security/wildfly-elytron/archive/%{namedversion}.tar.gz

BuildRequires:       graphviz maven-local mvn(jdepend:jdepend) mvn(junit:junit)
BuildRequires:       mvn(org.jboss:jboss-parent:pom:) mvn(org.jboss.apiviz:apiviz)
BuildRequires:       mvn(org.jboss.logging:jboss-logging)
BuildRequires:       mvn(org.jboss.logging:jboss-logging-annotations)
BuildRequires:       mvn(org.jboss.logging:jboss-logging-processor)
BuildRequires:       mvn(org.jboss.logmanager:jboss-logmanager)
BuildRequires:       mvn(org.jboss.logmanager:log4j-jboss-logmanager)
BuildRequires:       mvn(org.jboss.modules:jboss-modules)
BuildRequires:       mvn(org.jboss.slf4j:slf4j-jboss-logmanager)
BuildRequires:       mvn(org.kohsuke.metainf-services:metainf-services)
BuildRequires:       mvn(org.wildfly.common:wildfly-common)
BuildArch:           noarch

%description
WildFly Elytron is a new WildFly sub-project which
is completely replacing the combination of PicketBox and
JAAS as the WildFly client and server security mechanism.
An "elytron" (ĕl´·ĭ·trŏn, plural "elytra") is the hard,
protective casing over a wing of certain flying insects
(e.g. beetles).

%package javadoc
Summary:             Javadoc for %{name}
%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
%pom_remove_plugin :maven-checkstyle-plugin
%mvn_file org.wildfly.security:%{name} %{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Wed Dec 29 2021 wangkai <wangkai385@huawei.com> - 1.0.2-3
- This package depends on log4j.After the log4j vulnerability CVE-2021-44832 is fixed,the version needs to be rebuild.

* Fri Dec 24 2021 wangkai <wangkai385@huawei.com> - 1.0.2-2
- This package depends on log4j.After the log4j vulnerability CVE-2021-45105 is fixed,the version needs to be rebuild.

* Mon Aug 17 2020 maminjie <maminjie1@huawei.com> - 1.0.2-1
- package init
