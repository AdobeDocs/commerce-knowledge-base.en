---
title: Getting thousands of search results after upgrading from 2.4.2 to 2.4.5-p3
description: This article provides a solution to the issue where you get thousands of search results after upgrading from 2.4.2 to 2.4.5-p3.
feature: Quotes, Search, Returns
role: Developer, Admin
---

# Getting thousands of search results after upgrading from 2.4.2 to 2.4.5-p3

This article provides a solution to the issue where you get thousands of search results after upgrading from 2.4.2 to 2.4.5-p3.

## Affected products and versions

* Adobe Commerce versions => 2.4.5-p3

## Issues

You are looking for a particular product (for example, *WSH12-32-Red*) but the search returns lots of similar products.

## Solutions

The nature of a full-text search in [!DNL Elasticsear] is based on relevance, not exact matching. So most relevant matches (like exact matched SKU) are ordered first.

However, if you need an exact match (non-obivious case for search), you should use quotes for your search query. Query for *WSH12-32-Red* without quotes will return several results with the exact match (product with *SKU WSH12-32-Red*) appearing first in the result. But quoted query *"WSH12-32-Red"* will return only one exact match result.
