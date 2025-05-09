---
title: Top navigation panel does not load on storefront
description: This article provides configuration solutions to the Varnish Edge Side Includes (ESI) issues, where certain pages' content, usually the top navigation panel, is not displayed on the storefront if Varnish is used for caching.
exl-id: e7f9b773-1a2d-4c3b-9e1f-a1781fbc898c
feature: Categories, Site Navigation, Storefront, Variables
role: Admin
---
# Top navigation panel does not load on storefront

This article provides configuration solutions to the Varnish Edge Side Includes (ESI) issues, where certain pages' content, usually the top navigation panel, is not displayed on the storefront if Varnish is used for caching.

## Affected products and versions

* Adobe Commerce 2.X.X
* All Varnish versions

## Issue

<u>Prerequisites</u>:

Install and configure Varnish for your Adobe Commerce store.

<u>Steps to reproduce</u>:

1. Go to the storefront.
1. Browse through the store pages.

<u>Expected results</u>:

All content and all page blocks load successfully.

<u>Actual results</u>:

Observe that some content blocks, like the top navigation panel with categories, are not loading. Blank space is displayed instead.

## Cause

The possible reasons for the issue are the following:

* ESI include tags are generated with HTTPS access protocol, while Varnish only works with HTTP.
* Varnish does not process ESI inside JSON.
* Response headers are too big for Varnish; it cannot process them.

## Solution

To resolve the issues, you need to perform an additional Varnish configuration and restart Varnish.

1. As a user with `root` privileges, open your Vanish configuration file in a text editor. See the [Modify the Varnish system configuration](https://experienceleague.adobe.com/en/docs/commerce-operations/configuration-guide/cache/config-varnish-server) in our developer documentation for info on where this file might be located for different operating systems.
1. In the `DAEMON_OPTS variable`, add `-p feature=+esi_ignore_https`, `-p  feature=+esi_ignore_other_elements`, `-p  feature=+esi_disable_xml_check`. This would look like:

    ```bash
    DAEMON_OPTS="-a :6081 \    -p feature=+esi_ignore_other_elements \    -p feature=+esi_disable_xml_check \    -p feature=+esi_ignore_https \    -T localhost:6082 \    -f /etc/varnish/default.vcl \    -S /etc/varnish/secret \    -s malloc,256m"
    ```

1. Save your changes and exit the text editor.
1. In the VCL configuration file, increase the response headers by increasing the values of these parameters: `http_resp_hdr_len`, `http_resp_size`, `workspace_backend`. Make sure that the last two of them have similar values.
1. When you change this, you need to run `service varnish restart` for the changes to take effect.

## Related reading

* [Configure Varnish and your web server](https://experienceleague.adobe.com/en/docs/commerce-operations/configuration-guide/cache/config-varnish-server) in our developer documentation.
* [Varnish documentation](https://varnish-cache.org/docs/5.1/reference/index.html)
