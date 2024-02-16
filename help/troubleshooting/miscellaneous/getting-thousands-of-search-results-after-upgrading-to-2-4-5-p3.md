---
title: Getting thousands of results when looking for a particular product
description: This article provides a solution to the issue where you get thousands of search results when you are looking for a particular product.
feature: Quotes, Search, Returns
role: Developer, Admin
exl-id: 0eccf212-96be-4ea5-9e6e-95f27d7d9f92
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
