---
title: "ACSD-46618: The product list widget shows incorrect cached prices for a logged-in customer"
description: This article provides the solution for the issue where the product list widget shows incorrect cached prices for a logged-in customer.
---

# ACSD-46618: The product list widget shows incorrect cached prices for a logged-in customer

The ACSD-46618 patch solves the issue where the product list widget shows incorrect cached prices for a logged-in customer. This patch is available when the [[!DNL Quality Patches Tool (QPT)]](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/announcements/commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.html?lang=en) 1.1.21 is installed. The patch ID is ACSD-46618. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.6. 

## Affected products and versions

**The patch is created for Adobe Commerce version:**
* Adobe Commerce (all deployment methods) 2.4.4

**Compatible with Adobe Commerce versions:**
* Adobe Commerce (all deployment methods) 2.4.0 - 2.4.5

>[!NOTE]
>
>Note: the patch might become applicable to other versions with new [!DNL Quality Patches Tool] releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL QPT] landing page](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html). Use the patch ID as a search keyword to locate the patch.

## Issue

The ACSD-46618 patch solves the issue where the product list widget shows incorrect cached prices for a logged-in customer.

<u>Steps to reproduce</u>:

1. In the Commerce Admin select **Stores**, then **Configuration**, expand **Sales**, and select **Tax**. Update the tax settings to show prices including and excluding taxes. 
1. Set **Enable Cross Border Trade** = *Yes*.
1. Create a tax rule that only applies to the US.
1. Add a widget to the home page including more than one product.
1. Create two customers with a US address and a non US address.
1. Log in using the US customer from the storefront. Make sure that the page is cached.
1. Observe the price displayed in the home page widget.
1. Log out and log in using the non-US customer.

<u>Expected results</u>:

The price displayed in the home page widget corresponds to the customer's address.

<u>Actual results</u>:

 The home page widget shows prices using the tax for non-US customers.


## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [[!DNL Quality Patches Tool] > Usage](https://experienceleague.adobe.com/docs/commerce-operations/tools/quality-patches-tool/usage.html) in the Quality Patches Tool guide.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about [!DNL Quality Patches Tool], refer to:

* [[!DNL Quality Patches Tool] released: a new tool to self-serve quality patches](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/announcements/commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.html?lang=en) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using [!DNL Quality Patches Tool]](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/support-tools/patches/check-patch-for-magento-issue-with-magento-quality-patches.html?lang=en) in our support knowledge base.

For info about other patches available in [!DNL QPT], refer to [Patches available in [!DNL QPT]](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html) in the Quality Patches Tool guide.
