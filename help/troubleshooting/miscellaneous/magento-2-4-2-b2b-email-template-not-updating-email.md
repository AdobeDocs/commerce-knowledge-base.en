---
title: 'Adobe Commerce 2.4.2 B2B: email template not updating email'
description: This article describes a known Adobe Commerce 2.4.2 B2B issue where updating some information in an email template is not updated in emails. This issue impacts email contents such as customer info, currency rates, currency symbol, email template change, etc. There is not a solution available at this time, but there is a workaround at the bottom of this article.
exl-id: 31b7086f-a941-4682-aa07-301ac31d543b
feature: B2B, Communications
role: Developer
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: bb03f6c4-cab9-560e-9d02-5816e1808d17
    internal-label: Communications
  - id: bd989d82-1e15-4534-88db-f1f51dd77ffa
    internal-label: Accounts
subfeature_v2:
  - id: f56d26ed-050b-4fb7-b29b-8e6e994e80a2
    internal-label: B2B
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# Adobe Commerce 2.4.2 B2B: email template not updating email

This article describes a known Adobe Commerce 2.4.2 B2B issue where updating some information in an email template is not updated in emails. This issue impacts email contents such as customer info, currency rates, currency symbol, email template change, etc. There is not a solution available at this time, but there is a workaround at the bottom of this article.

## Affected products and versions

* Adobe Commerce on-premises 2.4.2
* Adobe Commerce cloud infrastructure 2.4.2
* B2B 1.3.1

## Issue

 <u>Steps to reproduce</u>:

1. Company Admin creates a PO (Purchase Order) in the frontend.
1. Check the Auto-Approved email. The **customer name** / **currency rate** should be expected values.
1. Change currency symbol (**Stores > Configuration > Currency Setup > Currency Options**) in Admin and company admin name on the Customer Account page.
1. Customer Admin creates another PO in Admin.
1. Check the Auto-Approved email.

 <u>Expected results:</u>

 The customer name and currency symbol are changed in emails, and have their new values as expected.

 <u>Actual results</u>:

 The customer name and currency symbol are not changed in emails, and have their previous values.

## Workaround

Manually run the cron job or consumer to propagate the new information.

## Related reading

* [Manage message queues](https://experienceleague.adobe.com/en/docs/commerce-operations/configuration-guide/message-queues/manage-message-queues) in our developer documentation.
