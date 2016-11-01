$ ~/bakasablepp 3
Does it work?
Foobar Start!
backtrace() returned 5 addresses
/home/user/bakasablepp() [0x400c68]
/home/user/bakasablepp(_Z6foobari+0x3d) [0x400d1d]
/home/user/bakasablepp(main+0x4e) [0x400b2e]
/lib/x86_64-linux-gnu/libc.so.6(__libc_start_main+0xf5) [0x7fa0a4f44b45]
/home/user/bakasablepp() [0x400b7f]
Foobar End!
End!

$ ~/bakasablepp 3 | ~/do_readelf.py ~/bakasablepp
/home/user/bakasablepp
Does it work?
Foobar Start!
backtrace() returned 5 addresses
/home/user/bakasablepp() [0x400c68] <=== bakasable.cpp@10
/home/user/bakasablepp(_Z6foobari+0x3d) [0x400d1d] <=== bakasable.cpp@30
/home/user/bakasablepp(main+0x4e) [0x400b2e] <=== bakasable.cpp@38
/lib/x86_64-linux-gnu/libc.so.6(__libc_start_main+0xf5) [0x7fe097270b45] <=== not found
/home/user/bakasablepp() [0x400b7f] <=== not found
Foobar End!
End!
