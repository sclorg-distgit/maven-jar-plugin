%global pkg_name maven-jar-plugin
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        2.4
Release:        8.12%{?dist}
Summary:        Maven JAR Plugin

License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-jar-plugin/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{pkg_name}/%{version}/%{pkg_name}-%{version}-source-release.zip

# Some classes from maven-artifact come in maven-core, added a dep in pom.xml
Patch0:         %{pkg_name}-maven-core-dep.patch

BuildArch: noarch

BuildRequires: %{?scl_prefix_java_common}javapackages-tools >= 0.7.0
BuildRequires: %{?scl_prefix_java_common}maven-local
BuildRequires: %{?scl_prefix}maven-plugin-plugin
BuildRequires: %{?scl_prefix}maven-resources-plugin
BuildRequires: %{?scl_prefix}maven-doxia-sitetools
BuildRequires: %{?scl_prefix}maven-plugin-testing-harness
BuildRequires: %{?scl_prefix}maven-archiver
BuildRequires: %{?scl_prefix}plexus-archiver
BuildRequires: %{?scl_prefix_java_common}apache-commons-lang
BuildRequires: %{?scl_prefix}plexus-utils
BuildRequires: %{?scl_prefix_java_common}junit

%description
Builds a Java Archive (JAR) file from the compiled
project classes and resources.

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
API documentation for %{pkg_name}.


%prep
%setup -q -n %{pkg_name}-%{version}
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%patch0 -p1

#let plexus-container-default be retrieved as a dependency
sed -i -e "s|plexus-container-default|plexus-container|g" pom.xml
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
# Test class MockArtifact doesn't override method getMetadata
%mvn_build -f
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%{_javadir}/%{pkg_name}
%dir %{_mavenpomdir}/%{pkg_name}
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Mon Jan 11 2016 Michal Srb <msrb@redhat.com> - 2.4-8.12
- maven33 rebuild #2

* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 2.4-8.11
- maven33 rebuild

* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-8.10
- Add directory ownership on %%{_mavenpomdir} subdir

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 2.4-8.9
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 2.4-8.8
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-8.7
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-8.6
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-8.5
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-8.4
- Rebuild to fix incorrect auto-requires

* Fri Feb 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-8.3
- SCL-ize requires and build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-8.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-8.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.4-8
- Mass rebuild 2013-12-27

* Fri Aug 16 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.4-7
- Migrate away from mvn-rpmbuild (#997439)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-6
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

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
