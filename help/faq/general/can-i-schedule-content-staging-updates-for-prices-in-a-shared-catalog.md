---
title: Can I schedule Content Staging updates for prices in a shared catalog?
description: Adobe Commerce does not offer the functionality of scheduling a price update ([Content Staging](https://experienceleague.adobe.com/docs/commerce-admin/content-design/staging/content-staging.html)) for one or more products in a shared catalog.
exl-id: 5482326f-54c2-4efc-8e5e-6d075ee5be55
feature: "Catalogs, Customer Service"
---
# Can I schedule Content Staging updates for prices in a shared catalog?

Adobe Commerce does not offer the functionality of scheduling a price update ([Content Staging](https://experienceleague.adobe.com/docs/commerce-admin/content-design/staging/content-staging.html)) for one or more products in a shared catalog.

That means you cannot schedule such a price update directly from the **Set Pricing and Structure** menu of the Commerce Admin panel (there is no **Schedule New Update** button in this menu).

Still, you may use alternative methods and schedule a price update for:

* a customer group
* the product's base price

## Schedule price update for a customer group

1. Start [scheduling a new product update](https://experienceleague.adobe.com/docs/commerce-admin/content-design/staging/content-staging-scheduled-update.html).
1. Scroll down to the **Price** field and click **Advanced Pricing**.

    ![advanced_pricing.png](assets/advanced_pricing.png){width="600"}

1. In the **Customer Group Price section**, select the needed Customer Group and set the updated price.

    ![customer_group_price.png](assets/customer_group_price.png){width="700"}

1. Finish scheduling the update as usual.

In this workflow, you can only update the price for a single product; bulk price update is not available.

Remember: shared catalogs leverage the customer group pricing.

 **Related documentation**

* [Scheduling an update (Content Staging)](https://experienceleague.adobe.com/docs/commerce-admin/content-design/staging/content-staging-scheduled-update.html) in our user guide.
* [Advanced Pricing](https://experienceleague.adobe.com/docs/commerce-admin/catalog/products/pricing/pricing-advanced.html) in our user guide.

## Schedule price update for the base price

See the related article: [How base price change affects the shared catalog price?](/help/faq/general/base-price-change-affect-on-shared-catalog-price.md) in our support knowledge base.
