---
title: "MDVA-15546: Column 'entity_id' where clause is ambiguous"
description: "The MDVA-15546 patch solves performance issues that may be related to some Amazon extensions. This issue in indicated by the following error in exception logs: *where*   *Column 'entity\\_id' in where clause is ambiguous, query was: SELECT \\`main\\_table\\`.\\*, \\`extension\\_attribute\\_amazon\\_order\\_reference\\_id* \\`. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.20 is installed. The patch ID is MDVA-15546."
exl-id: d58c1728-eb7a-49e8-a329-3197f2339b9c
---
# MDVA-15546: Column 'entity_id' where clause is ambiguous

The MDVA-15546 patch solves performance issues that may be related to some Amazon extensions. This issue in indicated by the following error in exception logs: *where*   *Column 'entity\_id' in where clause is ambiguous, query was: SELECT \`main\_table\`.\*, \`extension\_attribute\_amazon\_order\_reference\_id* \`. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.20 is installed. The patch ID is MDVA-15546.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

Adobe Commerce on cloud infrastructure 2.2.5

**Compatible with Adobe Commerce versions:**

Adobe Commerce on cloud infrastructure 2.3.0 - 2.4.2

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [QPT landing page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

Performance issues that may be related to some Amazon extensions.

<u>Prerequisites</u>:

Clean Adobe Commerce with B2B and Amazon\_Payment.

<u>Steps to reproduce</u>:

1. Go to the storefront page.
1. Add product to the cart.
1. Wait or trigger the cron job `flush_preview_quotas`.

<u>Actual result</u>:

When you check `var/log/exception/log`, you see following error:

 *`report.ERROR: Cron Jobflush_preview_quotashas an error: SQLSTATE[23000]: Integrity constraint violation: 1052 Column 'entity_id' in where clause is ambiguous, query was: SELECT `main_table`.*, `extension_attribute_amazon_order_reference_id`.`amazon_order_reference_id` AS `extension_attribute_amazon_order_reference_id_amazon_order_reference_id`, `extension_attribute_amazon_order_reference_id`.`quote_id` AS `extension_attribute_amazon_order_reference_id_quote_id`, `extension_attribute_amazon_order_reference_id`.` sandbox_simulation_reference` AS `extension_attribute_amazon_order_reference_id_sandbox_simulation_reference`, `extension_attribute_amazon_order_reference_id`.`confirmed` AS `extension_attribute_amazon_order_reference_id_confirmed` FROM `quote` AS `main_table` LEFT JOIN `amazon_quote` AS `extension_attribute_amazon_order_reference_id` ON main_table.entity_id = extension_attribute_amazon_order_reference_id.quote_id WHERE ...`*

<u>Expected result</u>:

Cron Job completes without errors.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to [Patches available in QPT](https://devdocs.magento.com/quality-patches/tool.html#patch-grid) in our developer documentation.
