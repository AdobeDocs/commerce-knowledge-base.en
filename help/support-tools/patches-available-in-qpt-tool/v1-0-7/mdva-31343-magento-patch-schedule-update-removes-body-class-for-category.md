---
title: 'MDVA-31343 patch: schedule update removes body class for category'
description: MDVA-31343 patch fixes the issue where the assigned layout body CSS class for a category gets removed during scheduled update. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.7 is installed. The issue is scheduled to be fixed in Adobe Commerce 2.4.2.
exl-id: 50dbff01-cb77-4cac-b90e-5c4b06f5e4e7
feature: "Cache, Categories"
---
# MDVA-31343 patch: schedule update removes body class for category

MDVA-31343 patch fixes the issue where the assigned layout body CSS class for a category gets removed during scheduled update. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.7 is installed. The issue is scheduled to be fixed in Adobe Commerce 2.4.2.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

Adobe Commerce on cloud infrastructure 2.3.5-p2

**Compatible with Adobe Commerce versions:**

Adobe Commerce on cloud infrastructure and Adobe Commerce on-premises 2.3.4 - 2.3.5-p2

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

Layout body class gets removed from the category after scheduled update.

<u>Steps to reproduce</u>:

1. In the Commerce Admin, create a category.
1. Set **Layout** = *Category -- Full width* in the **Design** section.
1. Save the category.
1. Go to category frontend page. In the page source notice the

    ```css
    page-layout-category-full-width
    ```

    CSS class.
1. Under **CATALOG** > **Category**, click **Schedule New Update** in the *Scheduled Changes* section for the new category.
1. Wait for the scheduled update to start, run cron and flush cache.
1. Go to the category page on the frontend and inspect the page source.

<u>Expected results</u>:

In the page body, you see the

```css
page-layout-category-full-width
```

CSS class.

<u>Actual results</u>:

In the page body, you see the

```css
page-layout-2columns-left
```

CSS class, which is default for the category page.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to the [Patches available in QPT](https://devdocs.magento.com/quality-patches/tool.html#patch-grid) in our developer documentation.
