---
title: "MDVA-40619: Hierarchy changes break CMS page inline edit and throw 500 error"
labels: QPT patches,Quality Patches Tool,QPT 1.1.5,MQP,Magento,Adobe Commerce,cloud infrastructure,on-premises,CMS page, hierarchy,500 error,2.3.0,2.3.1,2.3.2,2.3.3,2.3.2-p2,2.3.4,2.3.3-p1,2.3.5,2.3.4-p2,2.3.5-p1,2.3.5-p2,2.3.6,2.3.6-p1,2.3.7,2.3.7-p1,2.3.7p2,2.4.0,2.4.0-p1,2.4.1,2.4.1-p1,2.4.2,2.4.2-p1,2.4.2-p2,2.4.3,2.4.3-p1
---

The MDVA-40619 patch solves the issue where the CMS page hierarchy changes break CMS page inline edit and throw "500 error". This patch is available when the [Quality Patches Tool (QPT)](https://support.magento.com/hc/en-us/articles/360047139492) 1.1.5 is installed. The patch ID is MDVA-40619. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.4.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

* Adobe Commerce (all deployment methods) 2.4.3

**Compatible with Adobe Commerce versions:**

* Adobe Commerce (all deployment methods) 2.3.0 - 2.4.3-p1

>![info]
>
>Note: the patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [QPT landing page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

CMS page hierarchy changes break CMS page inline edit and throw "500 error".

<ins>Steps to reproduce</ins>:

1. Go to the Admin Panel > **Content** > **Hierarchy**.
1. Select "Default Store View".
1. Uncheck "Use the parent node hierarchy".
1. Select page manually and click **Save**.
1. Then Go to **Content** > **Pages**.
1. Try to edit any CMS page from the grid.
1. Click **Save**.

<ins>Expected results</ins>:

Page is saved successfully.

<ins>Actual results</ins>:

You get the following error:

*A technical problem with the server created an error. Try again to continue what you were doing. If the problem persists, try again later.*

`Error: Call to a member function getData() on null in /magento2ee/app/code/Magento/VersionsCms/Controller/Adminhtml/Cms/Page/InlineEdit/Plugin.php:62`

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](https://support.magento.com/hc/en-us/articles/360047139492) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](https://support.magento.com/hc/en-us/articles/360047125252) in our support knowledge base.

For info about other patches available in QPT, refer to the [Patches available in QPT](https://support.magento.com/hc/en-us/sections/360010506631-Patches-available-in-MQP-tool-) section.
