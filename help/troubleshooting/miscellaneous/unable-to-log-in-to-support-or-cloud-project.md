---
title: Unable to log in to Adobe Commerce support or cloud account
description: This article provides a solution for when you struggle to log in to Adobe Commerce support or your cloud project.
exl-id: 676b32d2-8197-4c60-a1b1-3c51b01dd3a3
feature: Cloud, Paas
role: Developer
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: 5a951749-fac9-5bc7-9a98-ebe4ff066437
    internal-label: Cloud
  - id: 00451af3-7b97-5414-9992-3a6c269e413f
    internal-label: Paas
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# Unable to log in to Adobe Commerce support or cloud account

This article provides a solution for when you struggle to log in to Adobe Commerce support or your cloud project.

## Affected products and versions

Adobe Commerce (all deployment methods) all [supported versions](https://www.adobe.com/content/dam/cc/en/legal/terms/enterprise/pdfs/Adobe-Commerce-Software-Lifecycle-Policy.pdf)

## Issue

When you go to [https://account.magento.com/customer/account/login/](https://account.magento.com/customer/account/login/) or [https://accounts.magento.cloud/user](https://accounts.magento.cloud/user) you might notice that there is now a unified login form and you are no longer able to enter your credentials like you have previously.

<u>Steps to reproduce</u>:

Try to log in to your Commerce account.

![adobe-login-one](assets/adobe-login-one.png)

<u>Expected result</u>:

Logging in successfully.

<u>Actual result</u>:

Get redirected to a page to sign in with an Adobe account and credentials do not work.

![adobe-login-two](assets/adobe-login-two.png)


## Cause

As part of our process of integrating Adobe Commerce with other Adobe solutions, all users will need to create an Adobe login - if they do not already have one - using the same email address connected to their MageID.

## Solution

You may log in to the account with:

- An existing Adobe corporate/personal account.
- If you do not have an Adobe account, create one with the same email address.

For steps refer to [Commerce Identity Manager](https://experienceleague.adobe.com/docs/commerce-admin/start/commerce-account/commerce-identity-manager.html) in Adobe Experience League.

## Related reading

- [Link Magento.com and accounts.magento.cloud account logins](/help/faq/general/linking-magento-com-and-accounts-magento-cloud-account-logins.md)
