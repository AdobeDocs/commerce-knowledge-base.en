---
title: Product status incorrect when created programmatically
description: This article provides a fix for when product status is Disabled and products are not displayed on the store front, or are assigned to the wrong store views, when created/updated programmatically.
exl-id: ac02f961-f9e2-4620-839f-b8dbd0befb15
feature: Products
role: Developer
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: 4067ab89-2e97-5de1-8d98-de8318461a8d
    internal-label: Products
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# Product status incorrect when created programmatically

This article provides a fix for when product status is Disabled and products are not displayed on the store front, or are assigned to the wrong store views, when created/updated programmatically.

## Affected products and versions

* Adobe Commerce on cloud infrastructure 2.X.X
* Adobe Commerce on-premises 2.X.X

## Issue

When the catalog products get created or updated programmatically from a script with Adobe Commerce application bootstrapped, products might have Disabled status and/or assigned to the wrong store views.

## Cause

The issue might appear because of ACL restrictions set for the Adobe Commerce instance admin roles. In case of bootstrapped application, there will be no initialized admin sessions with appropriate ACL settings. That would cause validations to fail in the `Magento_AdminGws` module, which is responsible for permissions check on such actions.

## Solution for incorrect product status

Set a dynamic DI preference for the `Magento\Framework\Authorization\PolicyInterface`, as described in the [ObjectManager>Programmatic product updates](https://developer.adobe.com/commerce/php/development/components/object-manager/) topic in our developer documentation.

## Related reading

* [Github: Can not change product status which product created with productRepository](https://github.com/magento/magento2/issues/5664)
