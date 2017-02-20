---
layout: post
title:  "Setting up PrivateInternetAccess VPN client on Fedora Linux"
date:   2016-06-27 22:25:44
categories: code
---

Linux is great because it works on any computer for free of charge. But some times it’s really inconvenient to get certain softwares installed or to get something to work. 

If you are using Fedora and want to get a PIA VPN service setup on your machine, then good luck, because Fedora is not supported by PIA. 

Anyhow, I’ve worked out a solution for you, that is an installer. Just follow the steps and you’ll have your VPN setup in no time. 

It also stores your VPN password automatically if you choose to do so, that way you don’t have to retype your password when you select a different region.

[**PIA Fedora project git**](https://github.com/shaynewang/piafedora)

Here is how to run the installer:

{% highlight bash%}
$ git clone https://github.com/shaynewang/piafedora.git
$ cd piafedora
$ chmod +x install_fedora.sh
$ sudo ./install_fedora.sh
{% endhighlight %}
