#!/usr/bin/tclsh

set arch "x86_64"
set base "collate-1.0"
set filename "collate-src-1.0.zip"
set fileurl "https://sourceforge.net/projects/tcl-collate/files/$filename"

set var [list wget $fileurl -O $filename]
exec >@stdout 2>@stderr {*}$var

set var [list unzip $filename]
exec >@stdout 2>@stderr {*}$var

file rename collate-src-1.0 $base

set var [list tar czvf $base.tar.gz $base]
exec >@stdout 2>@stderr {*}$var

# Remove old file
file delete -force $filename

if {[file exists build]} {
    file delete -force build
}

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.tar.gz build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb tcl-collate.spec]
exec >@stdout 2>@stderr {*}$buildit

# Remove our source code
file delete -force $base
file delete $base.tar.gz
