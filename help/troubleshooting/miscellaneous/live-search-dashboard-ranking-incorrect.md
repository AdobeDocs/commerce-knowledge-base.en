---
title: '[!DNL Live Search] dashboard and search result ranking is incorrect'
description: This article provides troubleshooting information if the data in the [!DNL Live Search] dashboard is incorrect, or if the ranking of the search results are not what you expect.
feature: Admin Workspace, Categories, Search
role: Developer
exl-id: d4aea1f1-c2c4-45e5-87c8-73069f7c9ffd
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: e7dae43f-215c-4cdf-90d3-c5a461a6e669
    internal-label: Admin tools and workspace
  - id: c18ed297-2187-4aec-affb-9d9654eca6fc
    internal-label: Catalog management
  - id: dac87252-6066-4d6e-a9d2-f6d84c323de7
    internal-label: Configuration
subfeature_v2:
  - id: bb2df8be-afdd-4818-b6b5-95ca1dd3bc3a
    internal-label: Admin workspace
  - id: e91a50b1-0b31-436e-9033-00e4776e94cb
    internal-label: Categories
  - id: a1d22079-48b9-5e69-9ee6-eb236068ef34
    internal-label: Search
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# [!DNL Live Search] dashboard and search result ranking is incorrect

If you notice that the data displayed in the [!DNL Live Search] dashboard is incorrect, or if the [ranking of the search results](https://experienceleague.adobe.com/en/docs/commerce-merchant-services/live-search/live-search-admin/category-merch#ranking-strategies) are not what you expect, see the following for possible reasons:

* The `topLevelSku` field of product context in `productView` events is missing. This causes empty conversions and other unexpected metrics.

* The `add-to-cart` event does not have the `productContext` field set and populated.

* The environment type is incorrect. For example, if the environment is set to *[!UICONTROL Testing]* instead of *[!UICONTROL Production]*. See [Storefront context](https://github.com/adobe/commerce-events/blob/main/examples/events/example-contexts/mock-storefront-context.md) for more information.

* The search results context is missing from the [search-product-click](https://github.com/adobe/commerce-events/blob/main/examples/events/search-product-click.md) event.
