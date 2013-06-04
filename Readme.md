# What is this spec?

This spec is an attempt to build [Burp](http://burp.grke.net/) on RHEL systems.

### How to install

#### RHEL/CentOS 5/6

    wget http://mirrors.ircam.fr/pub/fedora/epel/6/i386/epel-release-6-7.noarch.rpm
    yum install ./epel-release-6-7.noarch.rpm -y --nogpg
    yum install -y rpm-build rpmdevtools librsync-devel openssl-devel zlib-devel gcc make gcc-c++ ncurses-devel libacl-devel
    rpmdev-setuptree
    cd ~/rpmbuild/SOURCES
    # download the 1.2.32.tar.bz2 tarball
    wget https://raw.github.com/goneri/burp-spec/master/burp
    wget https://raw.github.com/goneri/burp-spec/master/burp_ca.diff
    cd ~/rpmbuild/SPECS
    wget https://raw.github.com/goneri/burp-spec/master/burp.spec
    rpmbuild -bb burp.spec
    rpm -Uvh ~/rpmbuild/RPMS/x86_64/burp-*.rpm

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
