```
Installing
[server]$ mkdir ${HOME}/soft
[server]$ cd ${HOME}/soft
Download and extract the package

[server]$ wget http://prdownloads.sourceforge.net/swig/swig-3.0.5.tar.gz
[server]$ tar xvzf swig-3.0.5.tar.gz
[server]$ cd swig-3.0.5
Assuming you've followed the virtualenv directions, configure using:

[server]$ ./configure --prefix=$HOME --with-perl5=/usr/local/bin/perl \
          --with-python=$HOME/opt/python-2.7.7/bin/python  --with-ruby=/usr/bin/ruby
Compile and verify

[server]$ make
[server]$ make check
You might get some errors about ocaml. 
These don't matter (unless you intend to use this version of SWIG to generate ocaml bindings too.

[server]$ make install
```
