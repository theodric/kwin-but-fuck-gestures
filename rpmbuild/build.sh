#rpmbuild -ba SPECS/kwin6.spec &> compilation.log
#rpmbuild -ba SPECS/kwin6.spec > /dev/null 2> >(tee compilation.log)
rpmbuild -ba SPECS/kwin6.spec |& tee compilation.log
