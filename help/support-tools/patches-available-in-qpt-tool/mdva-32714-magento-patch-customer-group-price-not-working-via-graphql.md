---
title: "MDVA-32714 patch: customer group price not working via GraphQL"
description: "The MDVA-32714 patch fixes the issue where сustomer group price is not added in GraphQL product query response. This patch is available when the Quality Patches Tool (QPT) 1.0.13 is installed. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.3."
---

# MDVA-32714 patch: customer group price not working via GraphQL

>[!WARNING]
>
>A new patch called MDVA-33975 fixes GraphQL price calculation issues. MDVA-32714 is depreciated and it is recommended that you apply the patch MDVA-33975. To access this patch, refer to [MDVA-33975 patch: GraphQL price calculations](https://support.magento.com/hc/en-us/articles/360055782351) in our support knowledge base.

The MDVA-32714 patch fixes the issue where сustomer group price is not added in GraphQL product query response. This patch is available when the [Quality Patches Tool (QPT)](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching.html#mqp) 1.0.13 is installed. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.3.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

Adobe Commerce on cloud infrastructure 2.4.0

**Compatible with Adobe Commerce versions:**

Adobe Commerce on cloud infrastructure and Adobe Commerce on-premises 2.3.4 - 2.4.0-p1

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [QPT landing page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

Customer group price for the general customer is not added in GraphQL product query response.

<u>Steps to reproduce</u>:

1. Enable and set Special Price for any product for any customer group.
1. Use product query in GraphQL to pull prices for this product, as described in: [Products query > Sample query](https://devdocs.magento.com/guides/v2.4/graphql/queries/products.html#sample-queries) in our developer documentation.

<u>Expected results</u>:

```api
price_range
```

displays the discounted price for general customers according to what has been defined in the Admin Panel.

<u>Actual results</u>:

```api
price_range
```

does not display the discounted price for general customers.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](https://support.magento.com/hc/en-us/articles/360047139492) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](https://support.magento.com/hc/en-us/articles/360047125252) in our support knowledge base.

For info about other patches available in QPT, refer to the [Patches available in QPT](https://devdocs.magento.com/quality-patches/tool.html#patch-grid) in our developer documentation.