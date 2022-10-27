---
title: "ACSD-47106: new custom attribute on company creation page not saved"

labels: QPT patches,Quality Patches Tool,Support Tools,QPT 1.1.22,company creation page,Magento,Adobe Commerce,cloud infrastructure,custom company attribute,2.4.4,2.4.4-p1,2.4.4-p2,2.4.5,2.4.5-p1
description: "The ACSD-47106 patch fixes the issue where a value cannot be saved in a new custom attribute on a company creation page. This patch is available when the [[!DNL Quality Patches Tool (QPT)]](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/announcements/commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.html) 1.1.22 is installed. The patch ID is ACSD-47106. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.6."
---

# ACSD-47106: new custom attribute on company creation page not saved

The ACSD-47106 patch fixes the issue where incorrect details are displayed on the checkout payment page when Purchase Orders for companies are enabled. This patch is available when the [[!DNL Quality Patches Tool (QPT)]](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/announcements/commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.html) 1.1.22 is installed. The patch ID is ACSD-47106. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.6.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

* Adobe Commerce (all deployment methods) 2.4.4

**Compatible with Adobe Commerce versions:**

* Adobe Commerce (all deployment methods) 2.4.4 - 2.4.5-p1

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [QPT landing page](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html). Use the patch ID as a search keyword to locate the patch.

## Issue

A value cannot be saved in a new custom attribute on a company creation page.

<u>Prerequisites</u>:

1. B2B modules are installed.

<u>Steps to reproduce</u>:

1. Go to the Commerce Admin > **Stores** > *Attributes* > **Customer** > **Add New Attribute**. 
1. Create new attribute: *Test 01*.
1. Go the Admin > **Customers** > **Companies** > and create a new company with all the required detail.
1. Try to add a value to the custom attribute *Test 01*.
1. Try to update the value of the custom attribute *Test 01*.

<u>Expected results</u>:

Changes should be saved.

<u>Actual results</u>:

Changes are not saved.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://experienceleague.adobe.com/docs/commerce-operations/tools/quality-patches-tool/usage.html) in the Quality Patches Tool guide.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/announcements/commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.html?lang=en) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/support-tools/patches/check-patch-for-magento-issue-with-magento-quality-patches.html?lang=en) in our support knowledge base.

For info about other patches available in QPT, refer to [Patches available in QPT](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html) in our developer documentation.
