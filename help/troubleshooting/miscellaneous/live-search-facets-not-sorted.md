---
title: '[!DNL Live Search] facets are not alphabetically sorted'
description: This article provides troubleshooting information if the [!DNL Live Search] facets are not alphabetically sorted.
feature: Admin Workspace, Categories, Search
role: Developer
exl-id: 59f86727-c2a6-4418-8753-40f7937e059c
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
# [!DNL Live Search] facets are not alphabetically sorted

## Affected products and versions

Adobe Commerce versions 2.4.x and newer

## Issue

All Adobe Commerce storefront facets are sorted alphabetically with single-select options, regardless of the input type that is assigned to the corresponding attribute.

## Workaround

However, in certain edge cases, facets might not sort alphabetically as set up in the [[!DNL Live Search] Faceting workspace](https://experienceleague.adobe.com/en/docs/commerce-merchant-services/live-search/live-search-admin/facets/faceting-workspace).

As a workaround, you can sort product attributes in the [!UICONTROL Admin] attributes section.

1. On the **[!UICONTROL Admin]** sidebar, go to **Stores** > *Attributes* > **Product**.
1. Select an attribute from the table.

   ![Attribute List](assets/attribute-list.png)

1. Open the attribute that has the values you want to sort and select **Attribute Information** > **Properties**. 
1. Under **Manage Options**, you can sort the attribute values.

    ![Sort attributes](assets/sort-attributes.png)
