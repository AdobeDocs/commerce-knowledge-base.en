---
title: 'Adobe Commerce 2.4.0 patch: returns shipping label creation issue'
description: This article provides a patch for the known Adobe Commerce 2.4.0 issue when there is a problem with printing a shipping label for customers’ returns.
exl-id: f78f8d7e-29e9-4d6c-83f6-cd5afa1d7d9c
---
# Adobe Commerce 2.4.0 patch: returns shipping label creation issue

This article provides a patch for the known Adobe Commerce 2.4.0 issue when there is a problem with printing a shipping label for customers’ returns.

## Affected products and versions

* Adobe Commerce on cloud infrastructure 2.4.0
* Adobe Commerce on-premises 2.4.0

## Issue

<u>Steps to reproduce:</u>

1. Place and complete an order with one of the following core shipping methods: FedEx, DHL, UPS, and USPS.
1. Create and authorize returns for this order.
1. Open an authorized **Return Information** page and click the **Create Shipping Label** button.
1. Select shipping method, add a product to a package and click Save.

<u>Expected result:</u>

A shipping label is created successfully and you see a message: *You created a shipping label.*

<u>Actual result:</u>

The **Return Information** page is broken and you see an error message on the Return Information page: *General Information Changes have been made to this section that have not been saved. This tab contains invalid data*.

## Solution

Apply [patch](assets/MC-35984-2.4.0-CE-composer.patch.zip) provided in this article.

## Patch

The patch is attached to this article. To download it, scroll down to the end of the article and click the file name, or click the following link:

[MC-35984-2.4.0-CE-composer.patch](assets/MC-35984-2.4.0-CE-composer.patch.zip)

The patch is also available for download in both, `.git` and `.composer`, formats on [Adobe Commerce Downloads](https://magento.com/tech-resources/download) page, under **Patches** in the left column navigation. Search for MC-35984 patch.

## How to apply the patch

For instructions, see [How to apply a composer patch provided by Adobe](/help/how-to/general/how-to-apply-a-composer-patch-provided-by-magento.md) in our support knowledge page.

## Related readings in our support knowledge base:

* [Adobe Commerce 2.4.0 known issue: raw message data display on storefront](https://support.magento.com/hc/en-us/articles/360045804332)
* [Adobe Commerce 2.4.0 known issue: Export Tax Rates does not work](/help/troubleshooting/miscellaneous/magento-2.4.0-known-issue-export-tax-rates-does-not-work.md)
* [Adobe Commerce 2.4.0 known issue: “Add selections to my cart” button does not work](/help/troubleshooting/miscellaneous/magento-2.4.0-add-selections-to-my-cart-does-not-work.md)
* [Adobe Commerce 2.4.0 known issue: Braintree payment methods do not show up in Multiple Addresses checkout](/help/troubleshooting/payments/magento-2.4.0-braintree-not-in-multiple-addresses-checkout.md)
* [Adobe Commerce 2.4.0 B2B Admin can't add configurable product to quote](/help/troubleshooting/miscellaneous/magento-2.4.0-b2b-admin-can-t-add-configurable-product-to-quote.md)
* [Adobe Commerce 2.4.0 known issue: orders display error](/help/troubleshooting/storefront/magento-2.4.0-known-issue-orders-display-error.md)
* [Shipping labels creation known issue in Adobe Commerce 2.4.0](/help/troubleshooting/known-issues-patches-attached/shipping-labels-creation-known-issue-in-magento-2.4.0.md)
