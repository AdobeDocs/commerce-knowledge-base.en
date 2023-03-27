---
title: "Overview: [!DNL Quality Patches Tool] (QPT) v1.0.13"
description: This sub-section provides a detailed description of the issues fixed by the patches available in [!DNL Quality Patches Tool] (QPT) v1.0.13.
---
# [!DNL Quality Patches Tool] (QPT) v1.0.13 overview

This sub-section provides a detailed description of the issues fixed by the patches available in [!DNL Quality Patches Tool] (QPT) v1.0.13.

QPT v1.0.13 includes the following patches:

1. **MCP-87**: Improved indexation time for category product and stock indexers for large profiles.
1. **MDVA-13203**: Fixes the issue where the *Integrity constrain violation search_tmp_ table* error appears after a full reindex.
1. **MDVA-19391**: Fixes the issue where `analytics_collect_data` is throwing an error due to NULL description records in the `catalog_category_entity_text` table.
1. **MDVA-20376**: Fixes the issue with the *No such entity with customerId = 1* error in the `exception.log` for logged-in customers after order placement.
1. **MDVA-22150**: Fixes the issue where customers with a configurable product in cart and a coupon applied cannot log in if that configurable product is disabled in the Admin.
1. **MDVA-23426**: Fixes the issue where notification emails sent by Adobe Commerce contain a blank body with content being added as an attachment.
1. **MDVA-23764**: Fixes the bug in `JsFooterPlugin.php` that affects the display of dynamic blocks.
1. **MDVA-30858**: Fixes the issue with [!DNL PayPal] Settlement reports not being available under **[!UICONTROL Reports]** > **[!UICONTROL Sales]** > **[!UICONTROL PayPal]** Settlement as expected.
1. **MDVA-32545**: Fixes the issue where invoices are not sent out automatically when creating orders from the Admin.
1. **MDVA-32714**: Fixes the issue where customer group price is not working in GraphQL product query.
1. **MDVA-33106**: Fixes the issue where the rescheduled product changes are erased after the cron `run` command is executed.

Use the menu on the left to navigate to a specific patch page.
