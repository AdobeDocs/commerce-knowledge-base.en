---
title: Adobe Commerce 2.4.6 error placing order from Admin panel
description: This article provides a patch for the known Adobe Commerce on cloud infrastructure 2.4.6 issue when you become stuck on store selection after you place an order from the Commerce Admin panel.
---

# Adobe Commerce 2.4.6 error placing order from Admin panel

This article provides a patch for the known Adobe Commerce on cloud infrastructure 2.4.6 issue when you become stuck on store selection after you place an order from the Commerce Admin panel.

## Issue

When placing an order from the Admin panel, you are stuck on store selection.

<u>Steps to reproduce</u>

1. Go to **Sales** > **Orders** and select a customer to create an order.
2. Select the store to place the order from the store selector screen.

<u>Expected result</u>

After selecting the store, you are able to complete the order.

<u>Actual result:</u>

After selecting the store, you are redirected back to the store selector page, and you cannot create an order.

## Patch

Click the following link to download the patch.

 [Download ACSD-52277_2.4.6.patch](assets/ACSD-52277_2.4.6.patch)

### Compatible Adobe Commerce versions

The patch was created for and compatible with Adobe Commerce on cloud infrastructure and Adobe Commerce on-premises 2.4.6 and 2.4.6-p1.

## How to apply the patch

* For instructions on applying patches for Adobe Commerce on cloud infrastructure, refer to [Apply patches](/docs/commerce-cloud-service/user-guide/develop/upgrade/apply-patches.html) in our Commerce on Cloud Infrastructure Guide. 
* For instructions on applying patches for Adobe Commerce on-premises, refer to [Apply patches](/docs/commerce-operations/upgrade-guide/patches/apply.html?lang=en#composer) in our Commerce Upgrade Guide.

