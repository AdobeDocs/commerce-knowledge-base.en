---
title: Adobe Commerce prompts customers log in invalid link
description: The article provides a link to the patch for a known Adobe Commerce 2.3.5 issue, where customers are prompted to log in, but the link to resend a confirmation email does not work.
exl-id: 8adef44f-56a6-4f57-a9b5-fb8583d8ae8d
feature: Logs
---
# Adobe Commerce prompts customers log in invalid link

The article provides a link to the patch for a known Adobe Commerce 2.3.5 issue, where customers are prompted to log in, but the link to resend a confirmation email does not work.

## Affected products and versions

* Adobe Commerce (all deployment methods) 2.3.5

## Issue

Adobe Commerce prompts customers to log in by displaying this message: *"This account is not confirmed. Click here to resend confirmation email"*. The **Click here** link should open the Send confirmation link page, but is inactive.

## Solution

A patch for this issue is available in Adobe Commerce Technical Resources: [Resend account confirmation email link issue patch for Adobe Commerce 2.3.5](https://magento.com/tech-resources/download?_ga=2.193540264.409362045.1590506265-807369446.1578680711#download2368). A permanent fix will be available in Adobe Commerce 2.3.6, which is scheduled for release in Q4 2020.

See [How to apply a composer patch provided by Adobe](/help/how-to/general/how-to-apply-a-composer-patch-provided-by-magento.md) for instructions on how to apply a composer patch.

## Related reading

Articles in our support knowledge base and developer documentation for Adobe Commerce 2.3.5 known issues:

* [Adobe Commerce 2.3.5 known issue: virtual product multi-ship orders](/help/troubleshooting/miscellaneous/magento-2.3.5-known-issue-virtual-product-multi-ship-orders.md)
* [Product comparison known issue in Adobe Commerce 2.3.5](/help/troubleshooting/storefront/product-comparison-known-issue-in-magento-2.3.5.md)
* [Adobe Commerce 2.3.5, 2.3.5-p1 patch: country payment issue](/help/troubleshooting/known-issues-patches-attached/magento-2.3.5-2.3.5-p1-patch-country-payment-issue.md)
* [Adobe Commerce prompts customers log in invalid link](/help/troubleshooting/known-issues-patches-attached/magento-prompts-customers-log-in-invalid-link.md)
* [Bulk action product count known issue in Adobe Commerce 2.3.5](/help/troubleshooting/miscellaneous/bulk-action-product-count-known-issue-in-magento-2.3.5.md)
* [Patch for Amazon Pay checkout issue in Adobe Commerce 2.3.5-p1](/help/troubleshooting/payments/patch-for-amazon-pay-checkout-issue-in-magento-2.3.5-p1.md)
* [Adobe Commerce 2.3.5 Known Issues](https://devdocs.magento.com/guides/v2.3/release-notes/release-notes-2-3-5-commerce.html#known-issues)
