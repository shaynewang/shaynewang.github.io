---
layout: post
title:  "Hacking on Zircon 1" 
date:  2017-10-30 22:28:22
categories: code
---

Google is working on a new exciting OS project called Fuchsia. Fuchsia is an operating system using a new micro kernel called "Zircon". "Zircon" is in it's early stage of development, which means there is little documentation, and the code base changes frequently; and it has a lot of bugs. All of these sound very exciting to me, because this means to work on Zircon will be difficult and rewarding.

I came across my first hurdle when trying to debug the kernel in qemu on my mac. I want to work on this project in my
local environment. I'm planning on running Zircon in qemu and debug it in GDB. However, the GDB came with macOS is built
for darwin, which means it cannot debug .elf files. Since I needed to be able to debug .elf files. I had to resolve to
use LLDB, a GDB alternative for macs. I'm okay with using it but there is no documentation on how to connect to the
remote debugging server. After many tries, I finally found out using `gdb-remote localhost:1234` in LLDB is the same as
`target extended-remote :1234` in GDB. Now I can work on Zircon happily without having to spin up a vm, which is
really nice.

![]({{ site.url }}/images/zircon_lldb.png)
