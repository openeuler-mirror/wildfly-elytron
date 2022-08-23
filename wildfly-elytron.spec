%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:                wildfly-elytron
Version:             1.2.0
Release:             2
Summary:             Security, Authentication, and Authorization SPIs for the WildFly project
License:             ASL 2.0 and LGPLv2+
URL:                 http://wildfly.org/
Source0:             https://github.com/wildfly-security/wildfly-elytron/archive/refs/tags/%{namedversion}.tar.gz
Source1:             xmvn-reactor
Source2:             maven-enforcer-plugin-3.0.0-M1.tar.gz
Patch0:              0001-ignore-crlBlank-test.patch
Patch1:              increase_timeout.patch
BuildRequires:       maven-local java-1.8.0-openjdk-devel maven
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
%patch0 -p1
%patch1 -p1

cp %{SOURCE1} ./.xmvn-reactor
echo `pwd` > absolute_prefix.log
sed -i 's/\//\\\//g' absolute_prefix.log
absolute_prefix=`head -n 1 absolute_prefix.log`
sed -i 's/absolute-prefix/'"$absolute_prefix"'/g' .xmvn-reactor

%pom_remove_plugin :maven-checkstyle-plugin
%mvn_file org.wildfly.security:%{name} %{name}

mkdir -p /home/abuild/.m2/repository/org/apache/maven/plugins/maven-enforcer-plugin
tar -mxf %{SOURCE2} -C /home/abuild/.m2/repository/org/apache/maven/plugins/maven-enforcer-plugin/

%build
mvn package verify org.apache.maven.plugins:maven-javadoc-plugin:aggregate

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE.txt

%files javadoc 
/usr/share/javadoc/wildfly-elytron
%license LICENSE.txt

%changelog
* Fri Sep 9 2022 lvxiaoqian<xiaoqian@nj.iscas.ac.cn> - 1.2.0-2
- increase test timeout

* Fri Jun 24 2022 Ge Wang <wangge20@h-partners.com> - 1.2.0-1
- upgrade to version 1.2.0

* Mon Aug 17 2020 maminjie <maminjie1@huawei.com> - 1.0.2-1
- package init
