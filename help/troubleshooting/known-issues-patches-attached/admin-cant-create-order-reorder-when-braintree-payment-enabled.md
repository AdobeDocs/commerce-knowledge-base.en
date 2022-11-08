---
title: Admin can't create order/reorder when Braintree payment enabled
description: This article provides a patch for the Adobe Commerce 2.4.5 issue where an Admin user can't create orders nor reorders for customers when the Braintree payment method is enabled.
exl-id: 8840aecb-21d9-4965-8c09-395e2d263aaa
---
# Admin can't create order/reorder when Braintree payment enabled

This article provides a patch for the Adobe Commerce 2.4.5 issue where an Admin user can't create orders nor reorders for customers when the Braintree payment method is enabled.

## Affected products and versions

* Adobe Commerce on cloud infrastructure 2.4.5
* Adobe Commerce on-premises 2.4.5
* Magento Open Source 2.4.5

## Issue

<u>Steps to reproduce</u>:

1. The core Braintree integration is used (**Stores** > **Configurations** > **Sales** > **Payment Method** > **Braintree**).
1. Using Luma Storefront, place an order.
1. Go to Admin UI > **Sales**.
1. Either try to create a new order for a customer, or go to a previously placed order and click on **Reorder**.

 <u>Expected result</u>:

Admin users can successfully create orders and reorders for customers when the Braintree payment method is enabled.

<u>Actual result</u>:

Admin users can't create orders nor reorders for customers when the Braintree payment method is enabled, and returns the following error:

```bash
report.CRITICAL: Error: Call to a member function getMethodInstance() on null in /app/vendor/paypal/module-braintree-core/Block/Form.php:174
```

## Cause

Incorrect class dependencies (`vendor/paypal/module-braintree-core/Block/Form.php`)

## Solution

Apply the patch provided in this article.

## Patch

The patch is attached to this article. To download it, click the following link:

[BUNDLE-3137-composer.patch.zip](assets/BUNDLE-3137-composer.patch.zip)

>[!NOTE]
>
>Additionally for Adobe Commerce on cloud infrastructure merchants: Adobe has included the fix in the Cloud Patches for Commerce version 1.0.18. Please refer to [Cloud Patches for Commerce release notes](https://devdocs.magento.com/cloud/release-notes/mcp-release-notes.html) in our developer documentation to find instructions on applying the latest package.

### Compatible Adobe Commerce versions:

The patch was created for:

* Adobe Commerce on cloud infrastructure 2.4.5
* Adobe Commerce on-premises 2.4.5
* Magento Open Source 2.4.5

>[!NOTE]
>
>The patch is not compatible with any other Adobe Commerce and Magento Open Source versions and editions.

## How to apply the patch

See [How to apply a composer patch provided by Adobe](/help/how-to/general/how-to-apply-a-composer-patch-provided-by-magento.md) in our support knowledge base for instructions.
