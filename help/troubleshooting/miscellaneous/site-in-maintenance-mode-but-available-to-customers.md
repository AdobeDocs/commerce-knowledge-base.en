---
title: Site in maintenance mode but available to customers
description: This article provides a fix for when maintenance mode is enabled (an Adobe Commerce on cloud infrastructure issue), but the storefront is still available for customers.
exl-id: 61b81fbd-a382-44b5-94e9-5b6d72f11349
feature: Cache
role: Developer
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: e7dae43f-215c-4cdf-90d3-c5a461a6e669
    internal-label: Admin tools and workspace
subfeature_v2:
  - id: b673188e-f9fa-492a-b470-c8f949bf7827
    internal-label: Cache
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# Site in maintenance mode but available to customers

This article provides a fix for when maintenance mode is enabled (an Adobe Commerce on cloud infrastructure issue), but the storefront is still available for customers.

## Affected products and versions

* Adobe Commerce on cloud infrastructure (all versions)

## Issue

<u>Steps to reproduce:</u>

1. Enable the maintenance mode for the site.
1. Navigate to the storefront.

<u>Expected result:</u>

The maintenance page is displayed.

<u>Actual result:</u>

Storefront pages are displayed as usual.

## Cause

Pages are still cached, so the maintenance page does not show.

## Solution to site visible despite being in maintenance mode

1. SSH to your environment.
1. Run the `php bin/magento cache:clean` command.

## Related reading

[Enable or disable maintenance mode](https://experienceleague.adobe.com/en/docs/commerce-operations/installation-guide/tutorials/maintenance-mode) in our developer documentation.
