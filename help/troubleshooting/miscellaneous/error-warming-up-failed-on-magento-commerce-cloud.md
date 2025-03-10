---
title: 'ERROR: Warming up failed on Adobe Commerce on cloud infrastructure'
description: 'This article provides a solution for when the page cache is warming up and fails with an error:'
exl-id: 20a88030-b1c9-4fdc-83c1-f344d44cd2e1
feature: Cache, Cloud, Paas
role: Developer
---
# ERROR: Warming up failed on Adobe Commerce on cloud infrastructure

This article provides a solution for when the page cache is warming up and fails with an error:

 *ERROR: Warming up failed: `<website link>`*

## Affected products and versions

* Adobe Commerce on cloud infrastructure, all [supported versions](https://magento.com/sites/default/files/magento-software-lifecycle-policy.pdf)

## Issue

Cache warm-up failing.

<u>Steps to reproduce</u>:

Start cache warm-up operations.

<u>Expected result</u>:

Pages or whole site loads.

<u>Actual result</u>:

The site is unavailable or the response time is too high. *ERROR: Warming up failed: `<website link>`*

## Cause

Cache warm-up doesn't work with HTTP access control enabled.

## Solution

Ensure that you do not have access control enabled: go to the specific branch/environment and click on the **Settings** icon, and check the **HTTP access control** setting - cache warm-up cannot occur in this scenario, and access control has to be disabled.

## Related reading

* [Adobe Commerce User Guide > Full-Page Cache](https://experienceleague.adobe.com/en/docs/commerce-admin/systems/tools/cache-management#full-page-caching) in our user guide.
* [Cache warming up and site unavailable on Adobe Commerce](/help/troubleshooting/miscellaneous/cache-warming-up-and-site-unavailable-on-magento.md) in our support knowledge base.
