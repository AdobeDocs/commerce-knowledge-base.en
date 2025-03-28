---
title: 2.3.4 PayPal issue hotfix
description: This article provides a fix for errors received during order placement when selecting a region in PayPal Express Checkout. The issue is caused by changes made in the Adobe Commerce v2.3.4 release and is related to how PayPal Express Checkout address fields are parsed.
exl-id: 9f5ec100-49b0-4ac5-8951-32b5c4fe6bed
feature: Orders, Payments
role: Developer
---
# 2.3.4 PayPal issue hotfix

This article provides a fix for errors received during order placement when selecting a region in PayPal Express Checkout. The issue is caused by changes made in the Adobe Commerce v2.3.4 release and is related to how PayPal Express Checkout address fields are parsed.

## Affected versions and products

* Adobe Commerce on cloud infrastructure v2.3.4
* Adobe Commerce on-premises v2.3.4

## Issue

An error occurs when entering the country and region during order placement in PayPal Express Checkout. The issue is reproducible for any country where the region field in the address section is a text field (as opposed to a drop-down menu).

<u>Steps to reproduce</u> :

1. Enable PayPal Express Checkout.
1. Add product to cart as a guest or when you are logged in.
1. Go to checkout.
1. Select your shipping address. For example, the *UK* . Then enter an input into the **State/Province** field. For example, *Nottinghamshire*.
1. Click on the **Place Order** button to place order. You get a successful order page and order confirmation email.

<u>Expected Result:</u>

The order is placed successfully.

<u>Actual Result:</u>

When the order button is clicked on, an error displays:

```
Error 500: NOTICE: PHP message: PHP Fatal error: Uncaught Error: Call to a member
  function getId() on null in httpdocs/vendor/magento/module-paypal/Model/Api/Nvp.php:1527
```

## Solution

For Adobe Commerce on-premises merchants: Apply the [hotfix,](https://magento.com/tech-resources/download#download2353) which is available from the Downloads section on [magento.com](https://magento.com) portal in My account.

For Adobe Commerce on cloud infrastructure merchants: Adobe has included the fix in the Cloud Patches for Commerce v1.0.2. Please refer to [Cloud Patches for Commerce release notes](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/release-notes/cloud-patches?itm_source=devdocs&itm_medium=quick_search&itm_campaign=federated_search&itm_term=cloud%20patche) in our developer documentation to find instructions on applying the latest package.

## How to Apply the Patch

For instructions, see [How to apply a composer patch provided by Adobe](/help/how-to/general/how-to-apply-a-composer-patch-provided-by-magento.md) in our support knowledge base.

## Related Reading

* [Release information > Adobe Commerce 2.3.4 Release Notes > Apply the PayPal Express Checkout issue with region patch for Adobe Commerce 2.3.4 to address a critical PayPal Express Checkout issue](https://commerce-docs.github.io/devdocs-archive/2.3/guides/v2.3/release-notes/release-notes-2-3-4-commerce.html#apply-the-paypal-express-checkout-issue-with-region-patch-for-magento-234-to-address-a-critical-paypal-express-checkout-issue) in our developer documentation.
