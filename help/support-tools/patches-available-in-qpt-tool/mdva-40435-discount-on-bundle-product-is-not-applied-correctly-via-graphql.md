---
title: "MDVA-40435: Discount on bundle product is not applied correctly via GraphQL"
labels: QPT patches,Quality Patches Tool,QPT,MQP,Magento,QPT 1.1.4,Adobe Commerce,on-premises,cloud infrastructure,bundle product,GraphQL,discount,2.3.4-p2,2.3.5-p1,2.3.5-p2,2.3.6,2.3.6-p1,2.3.7,2.4.0,2.4.0-p1,2.4.1,2.4.1-p1,2.4.2,2.4.2-p1,2.4.2-p2,2.4.3,2.4.3-p1
---

The MDVA-40435 patch solves the issue where the discount on a bundled product is not applied correctly via GraphQL. This patch is available when the [Quality Patches Tool (QPT)](https://support.magento.com/hc/en-us/articles/360047139492) 1.1.4 is installed. The patch ID is MDVA-40435. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.4.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

* Adobe Commerce (all deployment methods) 2.4.1

**Compatible with Adobe Commerce versions:**

* Adobe Commerce (all deployment methods) 2.3.4 - 2.4.3-p1

>![info]
>
>Note: the patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [QPT landing page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

Discount on a bundled product is not applied correctly via GraphQL.

<ins>Steps to reproduce</ins>:

1. Create a cart price rule with a coupon code for $5 fixed discount.
1. Create an empty cart via GraphQL.
1. Add a bundled product to the cart via GraphQL.
1. Apply the coupon code on the fixed amount (5$) via GraphQL.
1. Get the cart information via GraphQL.

<ins>Expected results</ins>:

"discounts" is $5.

<ins>Actual results</ins>:

"discounts" is NULL.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](https://support.magento.com/hc/en-us/articles/360047139492) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](https://support.magento.com/hc/en-us/articles/360047125252) in our support knowledge base.

For info about other patches available in QPT, refer to the [Patches available in QPT](https://support.magento.com/hc/en-us/sections/360010506631-Patches-available-in-MQP-tool-) section.
