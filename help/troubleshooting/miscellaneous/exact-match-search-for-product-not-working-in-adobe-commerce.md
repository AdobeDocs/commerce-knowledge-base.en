---
title: Exact match search not working in Adobe Commerce 2.4.x
description: This article provides a clarification for the issue where store front search results using the same search string differ in Adobe Commerce 2.4.x compared to Adobe Commerce 2.3.x.
exl-id: 0867558e-1d74-4b83-abf3-651ca7fc32cb
feature: "Products, Search"
role: Developer
---
# Exact match search not working in Adobe Commerce 2.4.x

This article provides a clarification for the issue where store front search results using the same search string differ in Adobe Commerce 2.4.x compared to Adobe Commerce 2.3.x.

## Affected products and versions

- Adobe Commerce (all deployment methods) 2.4.x, 2.3.x
- Live Search

## Issue

<u>Prerequisites:</u>

You have products with attribute values `Saga 1` and `Saga 16` in both Adobe Commerce 2.3 and Adobe Commerce 2.4 stores.

<u>Steps to reproduce:</u>

1. On the store front of an Adobe Commerce 2.3 powered store, enter *Saga 1* in the search field and click **Search**.
1. Notice that in search results, you only get the products with the attribute value `Saga 1`.
1. On the store front of an Adobe Commerce 2.4 powered store, enter *Saga 1* in the search field and click **Search**.

<u>Actual result:</u>

Search results in 2.4 include products with attribute values `Saga 1` and `Saga 16`.

<u>Expected result:</u>

Search results in 2.4 are similar to 2.3 and only include products with attribute value `Saga 1`.

## Cause

The Adobe Commerce native search functionality used in 2.3.x provides exact match search results. While Live Search, an optional module available for installation, which was released with Adobe Commerce 2.4.x, is implemented differently, and the actual result is the expected behavior when the module is used.

## Related Reading

[Install Live Search](https://experienceleague.adobe.com/docs/commerce-merchant-services/live-search/onboard/install.html) in our user guide.

[Live Search](https://devdocs.magento.com/live-search/overview.html?itm_source=devdocs&itm_medium=search_page&itm_campaign=federated_search&itm_term=Live%20Search) in our developer documentation.
