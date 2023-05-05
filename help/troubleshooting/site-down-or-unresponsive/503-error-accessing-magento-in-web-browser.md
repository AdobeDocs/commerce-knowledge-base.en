---
title: 503 error accessing Adobe Commerce in web browser
description: This article provides a possible solution for the issue where you get a 503 error when trying to access Adobe Commerce storefront and/or Admin.
exl-id: 4232aa21-40c2-41b0-9fb0-fc8cd4db8e39
---
# 503 error accessing Adobe Commerce in web browser

This article provides a possible solution for the issue where you get a 503 error when trying to access Adobe Commerce storefront and/or Admin.

## Affected products and versions

Adobe Commerce 2.3.x

## Issue {#symptoms}

 <u>Steps to reproduce</u>

(Prerequisites: make sure the store is not in [maintenance mode](https://devdocs.magento.com/guides/v2.3/config-guide/cli/config-cli-subcommands-mode.html#config-mode-show)).

Navigate to your Commerce Admin or storefront in a web browser.

 <u>Expected result</u>

The page loads.

 <u>Actual result</u>

You get the HTTP 503 (Service Unavailable) error. The Apache `error.log` includes the following message:

 *Invalid command 'Order', perhaps misspelled or defined by a module not included in the server configuration.*

## Cause {#details}

Apache 2.4 compatibility module `mod_access_compat` is disabled, which results in Adobe Commerce URL rewrites not working properly.

## Solution {#suggested-solution}

Enable the `mod_access_compat` Apache module and restart Apache, by running the following as a user with 'root' privileges:

```bash
a2enmod access_compat
service <name> restart
```

On CentOS,

```bash
<name>
```

is

```bash
httpd
```

. On Ubuntu,

```bash
<name>
```

is

```bash
apache2
```

.

## Related reading {#additional-resources}

* [Apache documentation about mod\_access\_compat](https://httpd.apache.org/docs/current/mod/mod_access_compat.html)
* [Apache documentation about mod\_authz\_host](https://httpd.apache.org/docs/current/mod/mod_authz_host.html)
* [Order, Allow, Deny from the Apache Definitive Guide](https://docstore.mik.ua/orelly/linux/apache/ch05_06.htm)
* [askubuntu.com](https://askubuntu.com/questions/335228/changes-in-apache-config-between-12-04-2-and-12-04-3-lts)
