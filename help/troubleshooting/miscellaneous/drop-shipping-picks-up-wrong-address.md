---
title: Drop shipping picks up wrong address
description: The shipping solution does not pick up the address of the product's source.
exl-id: ce89713f-d506-4e4f-bf49-cdee3e6d29b5
feature: Customer Service, Orders, Shipping/Delivery
role: Developer
---
# Drop shipping picks up wrong address

## Issue

The shipping solution does not pick up the address of the product's source.

## Affected products and versions

* Adobe Commerce on cloud infrastructure (all versions), with Magento Inventory installed
* Adobe Commerce on-premises 2.3.0 and later, with Magento Inventory installed
* Magento Open Source 2.3.0 and later, with Magento Inventory installed

### Cause

Magento Inventory does not currently support using drop shipping rates calculation based on source address during checkout. Instead the default store address from the config is used in all cases.

## Related Reading

* [Magento Inventory FAQ](https://github.com/magento/inventory/wiki/MSI-FAQs) in GitHub.
