---
title: 'ERROR: Warming up failed on Adobe Commerce on cloud infrastructure'
description: 'This article provides a solution for when the page cache is warming up and fails with an error:'
exl-id: 20a88030-b1c9-4fdc-83c1-f344d44cd2e1
feature: Cache, Cloud, Paas
role: Developer
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: 5a951749-fac9-5bc7-9a98-ebe4ff066437
    internal-label: Cloud
  - id: 00451af3-7b97-5414-9992-3a6c269e413f
    internal-label: Paas
  - id: e7dae43f-215c-4cdf-90d3-c5a461a6e669
    internal-label: Admin tools and workspace
subfeature_v2:
  - id: b673188e-f9fa-492a-b470-c8f949bf7827
    internal-label: Cache
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
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
