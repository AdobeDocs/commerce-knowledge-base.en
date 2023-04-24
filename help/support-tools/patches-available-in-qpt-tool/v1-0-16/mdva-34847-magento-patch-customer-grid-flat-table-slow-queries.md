---
title: 'MDVA-34847: customer_grid_flat table slow queries'
description: The MDVA-34847 patch solves the issue where slow queries occur on the `customer_grid_flat` table. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.16 is installed. Please note that the issue was fixed in Adobe Commerce version 2.4.3.
exl-id: e91cb86d-83cd-4267-a132-64465a57da7f
---
# MDVA-34847: customer_grid_flat table slow queries

The MDVA-34847 patch solves the issue where slow queries occur on the `customer_grid_flat` table. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.16 is installed. Please note that the issue was fixed in Adobe Commerce version 2.4.3.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

Adobe Commerce on cloud infrastructure 2.3.3

**Compatible with Adobe versions:**

Adobe Commerce on cloud infrastructure and Adobe Commerce on-premises 2.3.0 - 2.4.2

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

Slow queries occur on the `customer_grid_flat` table.

<u>Steps to reproduce</u>:

1. Create an Admin user with a Custom scope (Example: Set **GWS** = *0,* and choose the existing default website with **ID** = *1*).
1. Create any product and category items.
1. Place an order from the frontend.
1. Log in to the Admin as the new user.
1. Go to the Sales grid (**Sales > Orders**).
1. Check that the SQL query has been sent to DB (database).

<u>Expected results</u>:

The Admin GWS extension should use

```sql
int
```

values of

```sql
website_id
```

in SQL conditions, as expected, like:

```sql
main_table.website_id IN (1)
```

<u>Actual results</u>:

The Admin GWS extension added a condition with

```sql
website_id
```

value as

```sql
string
```

, like:

```sql
main_table.website_id IN ('1')
```

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to the [Patches available in QPT](https://support.magento.com/hc/en-us/sections/360010506631-Patches-available-in-QPT-tool-) section.
