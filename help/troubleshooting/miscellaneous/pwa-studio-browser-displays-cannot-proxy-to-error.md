---
title: 'PWA Studio: Browser displays “Cannot proxy to“ error'
description: This topic discusses a solution when your web browser displays a "*Cannot proxy to*" and the console displays an
exl-id: de689633-34b8-4a25-bbd0-a58742c4d03c
feature: Console
role: Developer
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: 125c1f49-aefd-5f34-a252-288937f95f6b
    internal-label: Marketing Tools
subfeature_v2:
  - id: c4af0798-d497-5e6b-8380-19812c26d00a
    internal-label: Console
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# PWA Studio: Browser displays “Cannot proxy to“ error

This topic discusses a solution when your web browser displays a "*Cannot proxy to*" and the console displays an

```
ENOTFOUND
```

error when using Progressive Web App (PWA) Studio for Adobe Commerce.

## Affected products and versions

* PWA Studio for Adobe Commerce

## Issue

<u>Step to reproduce</u>:

* Load your Adobe Commerce store in a browser.

<u>Expected result</u>:

* The Adobe Commerce store loads normally in your browser.

<u>Actual result</u>:

* Your web browser displays the “*Cannot proxy to*“ error and the console displays an error like:

```
    ENOTFOUND
```


## Cause

NodeJS cannot resolve the hostname of your Adobe Commerce store.

## Solution

1. Make sure your Adobe Commerce store loads in more than one web browser.
1. If you are running a local DNS server or VPN, add an entry to your hostfile (located in `/etc/hosts`) and manually map this domain ([Generic instructions on hostfile editing](https://linuxize.com/post/how-to-edit-your-hosts-file/)) so NodeJS can resolve it.

## Related reading

* [PWA Studio for Adobe Commerce Documentation](https://developer.adobe.com/commerce/pwa-studio/)
* [Tools and libraries](https://developer.adobe.com/commerce/pwa-studio/guides/project/tools-libraries/)
