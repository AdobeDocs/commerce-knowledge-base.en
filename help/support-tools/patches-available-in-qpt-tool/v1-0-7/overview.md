---
title: "Overview: [!DNL Quality Patches Tool] (QPT) v1.0.7"
description: This sub-section provides a detailed description of the issues fixed by the patches available in [!DNL Quality Patches Tool] (QPT) v1.0.7.
---
# [!DNL Quality Patches Tool] (QPT) v1.0.7 overview

This sub-section provides a detailed description of the issues fixed by the patches available in [!DNL Quality Patches Tool] (QPT) v1.0.7.

QPT v1.0.7 includes the following patches:

1. **MDVA-29148**: Fixes the issue when creating a product via an API call, the product custom attribute of `\Magento\Eav\Model\Entity\Attribute\Backend\ArrayBackend` (like Multiselect) type does not use its default value if no value was provided in the payload.
1. **MDVA-29389**: Fixes the issue with Advanced Reporting where the `analytics_collect_data` cronjob says: *Port must be configured within host parameter (like localhost:3306)*.
1. **MDVA-30594**: Fixes the issue where an order with multiple addresses could not be saved during checkout when FPT is configured.
1. **MDVA-30782**: Fixes the issue where Dynamic Block is displayed regardless of cart rule.
1. **MDVA-30815**: Fixes the issue where when you change how many search results should be displayed on the search results page.
1. **MDVA-30837**: Adds configuration options for the free shipping calculation so the user can configure the Minimum Order Amount to get Free Shipping based on the Subtotal (or Grand Total).
1. **MDVA-30945**: Fixes the issue where you receive a fatal error message when updating carts `Call to a member function getValue() on null in module-configurable-product CartItemProcessor.php`.
1. **MDVA-30972**: Fixes the issue where custom order status was changed to *Processing* after partial shipment creation using WebApi.
1. **MDVA-31007**: Fixes the issue where custom address attributes are not correctly displayed in the order details page in the my account area and in the backend.
1. **MDVA-31021**: Fixes the issue where performance issues exists in `module-catalog-import-export/Model/Import/Product/Option.php`. If there are more than ~100k records in `catalog_product_option` table, a new CSV with single product takes less than 10 sec to validate.
1. **MDVA-31224**: Improves the performance of the `catalog_product_price` re-index operation for bundle products.
1. **MDVA-31282**: Fixes the issue where double authorizations occur on [!DNL Paypal PayFlow Pro] in Adobe Commerce. The double authorizations also have the effect of bypassing [!DNL PayFlow Pro's] fraud filters and doubling transaction fees.
1. **MDVA-31343**: Fixes the issue with the removed body class `page-layout-category-full-width` when a category is scheduled.

Use the menu on the left to navigate to a specific patch page.
