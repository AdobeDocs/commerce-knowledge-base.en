---
title: "ACSD-46674: Custom options of image type displayed as HTML in customer emails"
labels: QPT patches,Quality Patches Tool,Support Tools,Magento,Adobe Commerce,cloud infrastructure,on-premises,QPT 1.1.21,custom options,emails,image type,HTML,2.4.0,2.4.0-p1,2.4.1,2.4.1-p1,2.4.2,2.4.2-p1,2.4.2-p2,2.4.3,2.4.3-p1,2.4.3-p2,2.4.3-p3,2.4.4,2.4.4-p1,2.4.4-p2,2.4.5,2.4.5-p1
description: "The ACSD-46674 patch fixes the issue where the custom options of an image type are displayed as HTML in customer emails. This patch is available when the [Quality Patches Tool (QPT)](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html) 1.1.21 is installed. The patch ID is ACSD-46674. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.6."
---

# ACSD-46674: Custom options of image type displayed as HTML in customer emails

The ACSD-46674 patch fixes the issue where the custom options of an image type are displayed as HTML in customer emails. This patch is available when the [[!DNL Quality Patches Tool (QPT)]](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/announcements/commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.html?lang=en) 1.1.21 is installed. The patch ID is ACSD-46674. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.6.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

* Adobe Commerce (all deployment methods) 2.4.2-p2

**Compatible with Adobe Commerce versions:**

* Adobe Commerce (all deployment methods) 2.4.0 - 2.4.5-p1

>[!NOTE]
>
>The patch might become applicable to other versions with new [!DNL Quality Patches Tool] releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL QPT] landing page](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html). Use the patch ID as a search keyword to locate the patch.

## Issue

Custom options of an image type are displayed as HTML in customer emails.

<u>Steps to reproduce</u>:

1. Create a product with a custom option.

    * Option Type: File
    * Compatible File Extensions: png, jpg, gif
    * Required: Yes

1. Place an order for this product with an image uploaded as a custom option.
1. Create an invoice for the order created in step two.
1. Create a credit memo.
1. Check all confirmation emails.

<u>Expected results</u>:

The confirmation emails display the uploaded image.

<u>Actual results</u>:

The confirmation emails contain plain HTML code instead of the product custom option image.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [[!DNL Quality Patches Tools] > Usage](https://experienceleague.adobe.com/docs/commerce-operations/tools/quality-patches-tool/usage.html) in Adobe Experience League.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](https://support.magento.com/hc/en-us/articles/360047139492) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](https://support.magento.com/hc/en-us/articles/360047125252) in our support knowledge base.

For info about other patches available in QPT, refer to [Patches available in QPT](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html) in Adobe Experience League.
