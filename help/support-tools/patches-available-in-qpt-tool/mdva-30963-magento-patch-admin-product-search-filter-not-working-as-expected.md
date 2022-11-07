---
title: "MDVA-30963: admin product search filter not working as expected"
description: "The MDVA-30963 patch solves the issue wherein the Commerce Admin and the product search filter do not work as expected. Values that are overridden in a store view scope are also considered when filtering on **All store view** store view scope. This patch is available when the [Quality Patches Tool (QPT)](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/announcements/commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.html) 1.0.8 is installed. Please note that the issue was fixed in Adobe Commerce 2.4.2."
---

# MDVA-30963: admin product search filter not working as expected

The MDVA-30963 patch solves the issue wherein the Commerce Admin and the product search filter do not work as expected. Values that are overridden in a store view scope are also considered when filtering on **All store view** store view scope. This patch is available when the [Quality Patches Tool (QPT)](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/announcements/commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.html) 1.0.8 is installed. Please note that the issue was fixed in Adobe Commerce 2.4.2.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

* Adobe Commerce on cloud infrastructure 2.4.0

**Compatible with Adobe Commerce versions:**

* Adobe Commerce (all deployment methods) 2.3.2 - 2.4.1

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [QPT landing page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

<u>Steps to reproduce</u>:

1. Set **Stores** > **Configuration** > **Catalog** > **Catalog** > **Price** > **Catalog Price Scope** = *Website*.
1. Create two websites having two different currencies (For example, the default website is an India Store \[Rupee ₹\], and the second one is the US Store \[Dollar $\]).
1. Set the following **Base Currency**, **Default Display Currency**, and **Allowed Currencies**:
    * **Default Config** = *US Dollar (Default)*
    * **Main Website** = *Indian Rupee*
    * **WebsiteUS** = **Use Default** = *US Dollar*
1. Set **Stores** > **Currency Rates** = *1:1*.
1. Create a test simple product assigned to both Websites with the following prices:
    * **Default Price** = **US Website price** = *123 USD*
    * **Main Website price** = *321 Rupee*
1. Create a subAdmin user that has access only to the US Store.
1. Go to the US storefront, and put a product in the cart (Example: *123 USD price*).
1. Log in to the Admin with subAdmin just created (Example: *US Only admin*).
1. Go to **Reports** > **Products in cart**.

<u>Expected results</u>:

When filtering within the **All store view** store view scope, products filtering should get the value set in that particular scope.

<u>Actual results</u>:

Values overridden in a store view scope are also considered when filtering on the "All store view" store view scope.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/announcements/commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.html) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](https://support.magento.com/hc/en-us/articles/360047125252) in our support knowledge base.

For info about other patches available in QPT, refer to [Patches available in QPT](https://devdocs.magento.com/quality-patches/tool.html#patch-grid) in our developer documentation.