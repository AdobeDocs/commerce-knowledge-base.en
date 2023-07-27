---
title: 'Adobe Commerce 2.4.0: exception during B2B 1.2.0 install'
description: This article provides a fix for an Adobe Commerce known issue for an exception thrown during `setup:upgrade` when installing B2B 1.2.0.
exl-id: 2c1dadd9-7754-4b4c-8d37-b75c13beae5c
feature: B2B, Install, Upgrade
role: Developer
---
# Adobe Commerce 2.4.0: exception during B2B 1.2.0 install

This article provides a fix for an Adobe Commerce known issue for an exception thrown during `setup:upgrade` when installing B2B 1.2.0.

## Affected products and versions

* Adobe Commerce on-premises 2.4.0
* Adobe Commerce on cloud infrastructure 2.4.0
* B2B 1.2.0

## Issue

 <u>Steps to reproduce</u>

1. Install Adobe Commerce with more than one store created.
1. Create an additional store.
1. Install B2B 1.2.0.

>[!WARNING]
>
>The upgrade of any B2B instance with more than 1 store from a version below 1.2.0 or Commerce instance below 2.4.0, is also affected.

 <u>Expected result</u>

B2B 1.2.0 installs.

 <u>Actual result</u>

When `setup:upgrade` runs to install B2B 1.2.0, this error appears on the `PurchaseOrder` module:

```php
Module 'Magento_PurchaseOrder':
  Unable to apply data patch Magento\PurchaseOrder\Setup\Patch\Data\InitPurchaseOrderSalesSequence
  for module Magento_PurchaseOrder. Original exception message: DDL statements
  are not allowed in transactions
```

## Solution

Apply the patch provided in this article.

## Patch

The patch is attached to this article, available for download in both `.composer` and `.git` formats (after you unzip the files).

To download it, scroll down to the end of the article and click the file name, or click one of the following links:

* [Composer patch B2B-716\_composer.patch](assets/B2B-716_composer.patch.zip)
* [Git patch B2B-716\_git.patch](assets/B2B-716_git.patch.zip)

## How to apply a patch

 <u>Composer patch </u>

See [How to apply a composer patch provided by Adobe](/help/how-to/general/how-to-apply-a-composer-patch-provided-by-magento.md) for composer patch instructions.

 <u>Git patch </u>

* See [Apply patches](https://devdocs.magento.com/cloud/project/project-patch.html) in developer documentation for git patch instructions for Adobe Commerce on cloud infrastructure.
* See [Applying patches: Custom patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching.html#custom-patches) in developer documentation for git patch instructions for Adobe Commerce.

## Related reading

* [Adobe Commerce 2.4.0 known issue: raw message data display on storefront](/help/troubleshooting/storefront/magento-2.4.0-issue-storefront-raw-message-data-display.md)
* [Adobe Commerce 2.4.0 known issue: Export Tax Rates does not work](/help/troubleshooting/miscellaneous/magento-2.4.0-known-issue-export-tax-rates-does-not-work.md)
* [Adobe Commerce 2.4.0 known issue: Braintree payment methods do not show up in Multiple Addresses checkout](/help/troubleshooting/payments/magento-2.4.0-braintree-not-in-multiple-addresses-checkout.md)
* [Adobe Commerce 2.4.0 known issue: Error message selecting local payment method displayed for some countries during checkout](/help/troubleshooting/payments/magento-2.4.0-checkout-error-selecting-local-payments.md)
* [Adobe Commerce 2.4.0 known issue: 404 error when removing rewards points on multi-shipping checkout](/help/troubleshooting/storefront/magento-2.4.0-404-error-removing-rewards-points-on-multi-shipping-checkout.md)
* [Adobe Commerce 2.4.0 known issue: orders display error](/help/troubleshooting/storefront/magento-2.4.0-known-issue-orders-display-error.md)
* [Adobe Commerce 2.4.0 B2B Admin can't add configurable product to quote](/help/troubleshooting/miscellaneous/magento-2.4.0-b2b-admin-can-t-add-configurable-product-to-quote.md)
* [Shipping labels creation known issue in Adobe Commerce 2.4.0](/help/troubleshooting/known-issues-patches-attached/shipping-labels-creation-known-issue-in-magento-2.4.0.md)
* [Adobe Commerce 2.4.0 known issue - refresh on Customer's Activities does not work](/help/troubleshooting/miscellaneous/magento-2.4.0-refresh-on-customer-activities-does-not-work.md)
* [Adobe Commerce 2.4.0 known issue: "Add selections to my cart" button does not work](/help/troubleshooting/miscellaneous/magento-2.4.0-add-selections-to-my-cart-does-not-work.md)
