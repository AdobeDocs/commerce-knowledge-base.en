---
title: '[!DNL Live Search] dashboard and search result ranking is incorrect'
description: This article provides troubleshooting information if the data in the [!DNL Live Search] dashboard is incorrect, or if the ranking of the search results are not what you expect.
feature: Admin Workspace, Categories, Search
role: Developer
exl-id: d4aea1f1-c2c4-45e5-87c8-73069f7c9ffd
---
# [!DNL Live Search] dashboard and search result ranking is incorrect

If you notice that the data displayed in the [!DNL Live Search] dashboard is incorrect, or if the [ranking of the search results](https://experienceleague.adobe.com/en/docs/commerce-merchant-services/live-search/live-search-admin/category-merch#ranking-strategies) are not what you expect, see the following for possible reasons:

* The `topLevelSku` field of product context in `productView` events is missing. This causes empty conversions and other unexpected metrics.

* The `add-to-cart` event does not have the `productContext` field set and populated.

* The environment type is incorrect. For example, if the environment is set to *[!UICONTROL Testing]* instead of *[!UICONTROL Production]*. See [Storefront context](https://github.com/adobe/commerce-events/blob/main/examples/events/example-contexts/mock-storefront-context.md) for more information.

* The search results context is missing from the [search-product-click](https://github.com/adobe/commerce-events/blob/main/examples/events/search-product-click.md) event.
