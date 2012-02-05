# What is this spec?

This spec is an attempt to build [Burp](http://burp.grke.net/) on RHEL systems.

### How to install

#### RHEL/CentOS 5/6
    wget http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-5.noarch.rpm
    yum install ./epel-release-6-5.noarch.rpm -y --nogpg
    yum install -y rpm-build rpmdevtools librsync-devel openssl-devel zlib-devel gcc make gcc-c++
    rpmdev-setuptree
    cd ~/rpmbuild/SOURCES
    wget "http://downloads.sourceforge.net/project/burp/burp-1.2.2%20%28stable%29/burp-1.2.2.tar.bz2?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fburp%2F&ts=1328452547&use_mirror=kent"
    cd ~/rpmbuild/SPECS
    wget http://github.com/kaerast/burp-spec/burp-1.2.2.spec
    rpmbuild -bb burp-1.2.2.spec
    rpm -Uvh ~/rpmbuild/RPMS/x86_64/burp-1.2.2-1.el6.x86_64.rpm

**PROFIT!**

### What it does

+ Builds
+ Installs

### What it does **not** do

+ Create SSL certificates

### Distro support

Builds cleanly on:

* Centos 6 x86_64

### Personal thoughts

This is by no means, correct, or sane. Nor does it follow any sort of policy for packaging. I leave that to the people who are most familiar with such things, and will willingly accept patches that add those features.