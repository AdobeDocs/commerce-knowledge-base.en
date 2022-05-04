---
title: "MDVA-35197: GraphQL add to cart error if added products out of stock"
labels: 2.3.5,2.3.5-p1,2.3.5-p2,2.3.6,2.3.6-p1,QPT 1.0.17,Magento Commerce,Magento Commerce Cloud,Quality Patches Tool,support tools,Adobe Commerce,cloud infrastructure,on-premises
---

The MDVA-35197 patch fixes the issue where there's an error when adding to cart using GraphQL if previously added products become out of stock. This patch is available when the [Quality Patches Tool (QPT)](https://support.magento.com/hc/en-us/articles/360047139492) 1.0.17 is installed.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

Adobe Commerce on cloud infrastructure 2.3.6

**Compatible with Adobe Commerce versions:**

Adobe Commerce (all deployment methods) 2.3.5 - 2.3.6-p1

>![info]
>
>Note: the patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [QPT landing page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

Error when trying to add a product to cart via GraphQL if the other product already in the cart (also added via GraphQL) becomes out of stock.

<ins>Steps to reproduce</ins>:

1. Using GraphQL, add any product to the cart.
1. Log in to the Commerce Admin panel and set this product as out of stock.
1. Try adding another product to the cart via GraphQL.

<ins>Expected results</ins>:

In-stock products can be added to the cart.

<ins>Actual results</ins>:

GraphQL error message: *Some of the products are out of stock*. A new "in-stock" product cannot be added.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](https://support.magento.com/hc/en-us/articles/360047139492) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](https://support.magento.com/hc/en-us/articles/360047125252) in our support knowledge base.

For info about other patches available in QPT, refer to [Patches available in QPT](https://devdocs.magento.com/quality-patches/tool.html#patch-grid) in our developer documentation.
