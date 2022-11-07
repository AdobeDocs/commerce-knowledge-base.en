---
title: "MDVA-32012 patch: S. Korean and Argentina zip codes validation"
description: "The MDVA-32012 patch solves the issue where Argentine and South Korean zip codes are not validating, due to changes or variation in national postal code formats. South Korean zip codes are now required to be 5-digits, whereas previously they were 6-digits. Argentine zip codes can be both numeric and alphanumeric. The MDVA-32012 patch means that these formats for postal code values will validate for these countries. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.9 is installed. Please note that the issue is scheduled to be fixed in Adobe Commerce version 2.4.2."
---

# MDVA-32012 patch: S. Korean and Argentina zip codes validation

The MDVA-32012 patch solves the issue where Argentine and South Korean zip codes are not validating, due to changes or variation in national postal code formats. South Korean zip codes are now required to be 5-digits, whereas previously they were 6-digits. Argentine zip codes can be both numeric and alphanumeric. The MDVA-32012 patch means that these formats for postal code values will validate for these countries. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.9 is installed. Please note that the issue is scheduled to be fixed in Adobe Commerce version 2.4.2.

## Affected products and versions

* The patch was designed for Adobe Commerce on cloud infrastructure 2.3.5.
* The patch is also compatible with the following Adobe Commerce versions: Adobe Commerce on cloud infrastructure and Adobe Commerce on-premises 2.3.0 - 2.4.1.

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [QPT landing page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

Inputting a 5-digit South Korean or alphanumeric Argentine zip codes produces a warning:

*Provided Zip/Postal Code seems to be invalid. Example: [1234 (if inputted an alphanumeric Argentine address)] or [123-456 (if inputted a 5-digit South Korean address)]. If you believe it is the right one you can ignore this notice.*

<u>Steps to reproduce</u>:

1. Open the storefront.
1. Add item to cart.
1. Process to checkout.
1. Add a new address with South Korea for the country and input a 5-digit zip code or add a new address with Argentina for the country and input an alphanumeric zip code.
1. Try to save.

<u>Expected results</u>:

Address should save without warning.

<u>Actual results</u>:

Saving address returns warning.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](https://support.magento.com/hc/en-us/articles/360047125252) in our support knowledge base.

For info about other patches available in QPT, refer to the [Patches available in QPT](https://devdocs.magento.com/quality-patches/tool.html#patch-grid) in our developer documentation.