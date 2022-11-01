---
title: Site not accessible due to origin cloaking
description: "This article provides a solution for when your Adobe Commerce on cloud infrastructure staging or production site storefront and/or Admin is not accessible."
---

# Site not accessible due to origin cloaking

This article provides a solution for when your Adobe Commerce on cloud infrastructure staging or production site storefront and/or Admin is not accessible.

## Affected products and versions

* Adobe Commerce on cloud infrastructure 2.3.x, 2.4.x

## Issue

https:&#8203;//mydomain.com.c.&lt;projectid&gt;.magento.cloud/ is no longer accessible.

<u>Steps to reproduce:</u>

1. Log in to your project.
1. Click **Access Project** for a list of URLs and SSH.

<u>Actual results:</u>

Page fails to load with the following error:

*NET::ERR\_CERT\_INVALID*  *TLS alert, bad certificate (554):*

<u>Expected results:</u>

Page loads successfully.

## Cause

Origin Cloaking has been enabled, so the origin is no longer accessible directly.

Origin cloaking is a security feature that allows Adobe Commerce to block any non-Fastly traffic going to the cloud infrastructure (origin) to prevent DDoS attacks.

## Solution

* If your cloud site is live, switch to https://mydomain.com/.
* If you have an active site (non-cloud), using the https://mydomain.com/ domain, set up a sub-domain `mcprod.mydomain.com` and update your **Base URL** to *https://mcprod.mydomain.com* instead, then [point the DNS to Fastly](https://devdocs.magento.com/cloud/cdn/configure-fastly.html#update-dns-configuration-with-development-settings).

## Related reading

[Fastly origin cloaking enablement FAQ](https://support.magento.com/hc/en-us/articles/360055181631) in our support knowledge base. 

