#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-guice
Version  : 3.0
Release  : 6
URL      : https://github.com/google/guice/archive/3.0.tar.gz
Source0  : https://github.com/google/guice/archive/3.0.tar.gz
Source1  : https://repo1.maven.org/maven2/com/google/inject/extensions/extensions-parent/3.0/extensions-parent-3.0.pom
Source2  : https://repo1.maven.org/maven2/com/google/inject/extensions/guice-servlet/3.0/guice-servlet-3.0.jar
Source3  : https://repo1.maven.org/maven2/com/google/inject/extensions/guice-servlet/3.0/guice-servlet-3.0.pom
Source4  : https://repo1.maven.org/maven2/com/google/inject/guice-parent/3.0/guice-parent-3.0.pom
Source5  : https://repo1.maven.org/maven2/com/google/inject/guice-parent/4.0/guice-parent-4.0.pom
Source6  : https://repo1.maven.org/maven2/com/google/inject/guice-parent/4.2.1/guice-parent-4.2.1.pom
Source7  : https://repo1.maven.org/maven2/com/google/inject/guice/3.0/guice-3.0.jar
Source8  : https://repo1.maven.org/maven2/com/google/inject/guice/3.0/guice-3.0.pom
Source9  : https://repo1.maven.org/maven2/com/google/inject/guice/4.0/guice-4.0.jar
Source10  : https://repo1.maven.org/maven2/com/google/inject/guice/4.0/guice-4.0.pom
Source11  : https://repo1.maven.org/maven2/com/google/inject/guice/4.2.1/guice-4.2.1-no_aop.jar
Source12  : https://repo1.maven.org/maven2/com/google/inject/guice/4.2.1/guice-4.2.1.pom
Source13  : https://repo1.maven.org/maven2/org/sonatype/sisu/inject/guice-bean/1.4.2/guice-bean-1.4.2.pom
Source14  : https://repo1.maven.org/maven2/org/sonatype/sisu/inject/guice-bean/2.3.0/guice-bean-2.3.0.pom
Source15  : https://repo1.maven.org/maven2/org/sonatype/sisu/inject/guice-parent/3.1.0/guice-parent-3.1.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-guice-data = %{version}-%{release}

%description
These libraries are not needed at runtime.

%package data
Summary: data components for the mvn-guice package.
Group: Data

%description data
data components for the mvn-guice package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/inject/extensions/extensions-parent/3.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/google/inject/extensions/extensions-parent/3.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/inject/extensions/guice-servlet/3.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/google/inject/extensions/guice-servlet/3.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/inject/extensions/guice-servlet/3.0
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/com/google/inject/extensions/guice-servlet/3.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/inject/guice-parent/3.0
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/com/google/inject/guice-parent/3.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/inject/guice-parent/4.0
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/com/google/inject/guice-parent/4.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/inject/guice-parent/4.2.1
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/com/google/inject/guice-parent/4.2.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/inject/guice/3.0
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/com/google/inject/guice/3.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/inject/guice/3.0
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/com/google/inject/guice/3.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/inject/guice/4.0
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/com/google/inject/guice/4.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/inject/guice/4.0
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/com/google/inject/guice/4.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/inject/guice/4.2.1
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/com/google/inject/guice/4.2.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/inject/guice/4.2.1
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/com/google/inject/guice/4.2.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/sonatype/sisu/inject/guice-bean/1.4.2
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/org/sonatype/sisu/inject/guice-bean/1.4.2

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/sonatype/sisu/inject/guice-bean/2.3.0
cp %{SOURCE14} %{buildroot}/usr/share/java/.m2/repository/org/sonatype/sisu/inject/guice-bean/2.3.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/sonatype/sisu/inject/guice-parent/3.1.0
cp %{SOURCE15} %{buildroot}/usr/share/java/.m2/repository/org/sonatype/sisu/inject/guice-parent/3.1.0


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/google/inject/extensions/extensions-parent/3.0/extensions-parent-3.0.pom
/usr/share/java/.m2/repository/com/google/inject/extensions/guice-servlet/3.0/guice-servlet-3.0.jar
/usr/share/java/.m2/repository/com/google/inject/extensions/guice-servlet/3.0/guice-servlet-3.0.pom
/usr/share/java/.m2/repository/com/google/inject/guice-parent/3.0/guice-parent-3.0.pom
/usr/share/java/.m2/repository/com/google/inject/guice-parent/4.0/guice-parent-4.0.pom
/usr/share/java/.m2/repository/com/google/inject/guice-parent/4.2.1/guice-parent-4.2.1.pom
/usr/share/java/.m2/repository/com/google/inject/guice/3.0/guice-3.0.jar
/usr/share/java/.m2/repository/com/google/inject/guice/3.0/guice-3.0.pom
/usr/share/java/.m2/repository/com/google/inject/guice/4.0/guice-4.0.jar
/usr/share/java/.m2/repository/com/google/inject/guice/4.0/guice-4.0.pom
/usr/share/java/.m2/repository/com/google/inject/guice/4.2.1/guice-4.2.1-no_aop.jar
/usr/share/java/.m2/repository/com/google/inject/guice/4.2.1/guice-4.2.1.pom
/usr/share/java/.m2/repository/org/sonatype/sisu/inject/guice-bean/1.4.2/guice-bean-1.4.2.pom
/usr/share/java/.m2/repository/org/sonatype/sisu/inject/guice-bean/2.3.0/guice-bean-2.3.0.pom
/usr/share/java/.m2/repository/org/sonatype/sisu/inject/guice-parent/3.1.0/guice-parent-3.1.0.pom
