%{?scl:%scl_package maven-jar-plugin}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}maven-jar-plugin
Version:        3.0.2
Release:        3.1%{?dist}
Summary:        Maven JAR Plugin

License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-jar-plugin/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{pkg_name}/%{version}/%{pkg_name}-%{version}-source-release.zip

BuildArch: noarch

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-archiver)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-artifact)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-core)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-utils)

%description
Builds a Java Archive (JAR) file from the compiled
project classes and resources.

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
API documentation for %{pkg_name}.

%prep
%setup -n %{pkg_name}-%{version} -q

%build
# Test class MockArtifact doesn't override method getMetadata
%mvn_build -f -- -DmavenVersion=3.1.1

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{pkg_name}
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 3.0.2-3.1
- Automated package import and SCL-ization

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.2-2
- Add missing BR on maven-plugin-plugin

* Thu Jun 23 2016 Michael Simacek <msimacek@redhat.com> - 3.0.2-1
- Update to upstream version 3.0.2

* Mon Jun 13 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.1-1
- Update to upstream version 3.0.1

* Mon May  9 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.0-1
- Update to upstream version 3.0.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 10 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-1
- Update to upstream version 2.6

* Tue Oct 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5-2
- Remove legacy Obsoletes/Provides for maven2 plugin

* Mon Jun 30 2014 Michal Srb <msrb@redhat.com> - 2.5-1
- Update to upstream version 2.5

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.4-9
- Use Requires: java-headless rebuild (#1067528)

* Fri Jan 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-8
- Update to Maven 3.x

* Mon Sep 23 2013 Michal Srb <msrb@redhat.com> - 2.4-7
- Migrate to XMvn
- Remove unneeded patch

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.4-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Nov 13 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.4-3
- Install license files
- Use generated maven file lists

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 15 2012 Alexander Kurtakov <akurtako@redhat.com> 2.4-1
- Update to 2.4.0.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 19 2011 Tomas Radej <tradej@redhat.com> - 2.3.2-1
- Updated to 2.3.2

* Fri Jun 17 2011 Alexander Kurtakov <akurtako@redhat.com> 2.3.1-3
- Build with maven 3.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Sep 10 2010 Alexander Kurtakov <akurtako@redhat.com> 2.3.1-1
- Update to 2.3.1.
- Keep plexus-container-default on the dependency tree.
- Drop depmap - not needed now.

* Wed May 19 2010 Alexander Kurtakov <akurtako@redhat.com> 2.3-3
- Add depmap.

* Wed May 19 2010 Alexander Kurtakov <akurtako@redhat.com> 2.3-2
- Requires maven-shared-archiver.

* Thu May 13 2010 Alexander Kurtakov <akurtako@redhat.com> 2.3-1
- Initial package
