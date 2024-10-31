---
title: Blank page or redirect loop error when accessing storefront or Commerce Admin
description: This article provides a solution for the issue when you access Adobe Commerce storefront or backend and you get a blank page or redirect loop.
exl-id: 65869de2-1939-481b-844b-69122345b407
feature: Admin Workspace, Cache, Storefront
role: Developer
---
# Blank page or redirect loop error when accessing storefront or Commerce Admin

This article provides a solution for the issue when you access Adobe Commerce storefront or backend and you get a blank page or redirect loop.

## Affected products and versions

* Adobe Commerce on cloud infrastructure, all versions
* Adobe Commerce on-premises, all versions
* Magento Open Source, all versions

## Issue

 <u>Steps to reproduce</u>

Open a storefront or Admin page.

 <u>Expected result</u>

The page opens.

 <u>Actual result</u>

The page is blank or displays the *"This webpage has a redirect loop"* error message.

## Cause

One of most probable reasons for the issue is that Adobe Commerce is set to redirect from unsecure URL to secure URL, but an unsecure URL is given as the value for the secure URL setting.

To fix the issue, you need to correct the value of the secure link.

## Solution

To make sure this is the cause of the problem, take the following steps:

1. Check the `web/secure/enable_upgrade_insecure` , `web/secure/use_in_adminhtml` (if you have the blank/loop redirect issue in Admin) or `web/secure/use_in_frontend` (if you have the blank/loop redirect issue on the store front) value in the `'core_config_data'` DB table.
    * If `web/secure/enable_upgrade_insecure` is set to "1", then Adobe Commerce is set up to add the response header `Content-Security-Policy: upgrade-insecure-requests`, thus instructing browsers to use HTTPS, redirecting all queries that come over HTTP
    to HTTPS, for both Admin and storefront.
    * If `web/secure/use_in_adminhtml` is set to "1", Adobe Commerce returns HTTPS redirects for all HTTP requests for the Admin pages.
    * If `web/secure/use_in_frontend` is set to "1", Adobe Commerce returns HTTPS redirects for all HTTP requests for the store front pages.
1. Check the `web/secure/base_url` and `web/unsecure/base_url` values in the `'core_config_data'` table. If they both start with    `http`, then you need to correct the "secure" value.

Fixing the issue:

1. Set the value starting with `https` for `web/secure/base_url.`
1. For the changes to be applied, clean the configuration cache by running the following command:

    ```bash
    php <your_magento_install_dir>/bin/magento cache:clean config
    ```

## Related reading

[Best practices for modifying database tables](https://experienceleague.adobe.com/en/docs/commerce-operations/implementation-playbook/best-practices/development/modifying-core-and-third-party-tables#why-adobe-recommends-avoiding-modifications) in the Commerce Implementation Playbook
