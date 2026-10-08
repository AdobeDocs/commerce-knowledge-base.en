---
title: Getting thousands of results when looking for a particular product
description: This article provides a solution to the issue where you get thousands of search results when you are looking for a particular product.
feature: Quotes, Search, Returns
role: Developer, Admin
exl-id: 0eccf212-96be-4ea5-9e6e-95f27d7d9f92
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: 792a7e9b-6519-5e99-a913-56c3dd2408da
    internal-label: Quotes
  - id: ac07462c-732c-5c1c-947b-4ce533b4fcfb
    internal-label: Returns
  - id: dac87252-6066-4d6e-a9d2-f6d84c323de7
    internal-label: Configuration
subfeature_v2:
  - id: a1d22079-48b9-5e69-9ee6-eb236068ef34
    internal-label: Search
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
---
# Getting thousands of results when looking for a particular product

This article provides a solution to the issue where you are getting thousands of search results when you are looking for a particular product.

## Affected products and versions

* Adobe Commerce all versions with [!DNL ElasticSearch] installed

## Issues

You are looking for a particular product (for example, *WSH12-32-Red*) but the search returns lots of similar products.

## Solutions

The nature of a full-text search in [!DNL ElasticSearch] is based on relevance, not exact matching. So most relevant matches (like exact matched SKU) are ordered first.

However, if you need a search result that matches exactly with your search term (exact match), you should use quotes for your search query. For example, query for *WSH12-32-Red* without quotes will return several results with the exact match (product with *SKU WSH12-32-Red*) appearing first in the result. But quoted query *"WSH12-32-Red"* will return only one exact match result.
