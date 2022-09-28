---
title: "MDVA-31969 patch: import products .csv images duplicated"
labels: 2.3.3,2.3.3-p1,2.3.4,2.3.4-p2,2.3.6,2.4.0,2.4.0-p1,2.4.1,QPT 1.0.14,Magento Commerce Cloud,csv file,duplicate,images,images-issues,import,product image,support tools,Adobe Commerce,cloud infrastructure,on-premises,quality patches for Adobe Commerce,Magento Open Source
---

The MDVA-31969 patch fixes the issue where images are duplicated when importing two products .csv files. This patch is available when the [Quality Patches Tool (QPT)](https://support.magento.com/hc/en-us/articles/360047139492) 1.0.14 is installed.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

Adobe Commerce on cloud infrastructure 2.3.4-p2

**Compatible with Adobe Commerce versions:**

Adobe Commerce on cloud infrastructure and Adobe Commerce on-premises 2.3.3 - 2.3.4-p2, 2.4.0 - 2.4.1

>![info]
>
 >Note: the patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [QPT landing page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

New product images are created in the `pub/media` folder, even if the same image already exists, when importing products.

<ins>Steps to reproduce</ins>:

1. Create a directory for images: `mkdir var/import-images`    
1. Add images inside the path `<install dir>/var/import-images`.
1. Import the product .csv file twice.

<ins>Expected results</ins>:

Products end up with each product image attached once.

<ins>Actual results</ins>:

Products end up with product images duplicated.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](https://support.magento.com/hc/en-us/articles/360047139492) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](https://support.magento.com/hc/en-us/articles/360047125252) in our support knowledge base.

For info about other patches available in QPT, refer to the [Patches available in QPT](https://devdocs.magento.com/quality-patches/tool.html#patch-grid) in our developer documentation.
