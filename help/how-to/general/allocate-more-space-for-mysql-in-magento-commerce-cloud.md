---
title: Allocate more space for MySQL in Adobe Commerce on cloud
description: This article provide instructions on how to allocate more space for MySQL in Adode Commerce on cloud infrastructure.
exl-id: 98501aa0-5ec7-4ea1-8856-13d171ad0be9
feature: Cloud
---
# Allocate more space for MySQL in Adobe Commerce on cloud


## Allocate space on Starter plan and Pro plan Integration

For all Starter plan environments and Pro plan [Integration environment](/help/announcements/adobe-commerce-announcements/integration-environment-enhancement-request-pro-and-starter.md), you can allocate more space for MySQL in the `.magento/services.yaml` file, by increasing the `mysql: disk:` parameter. For example:

```yaml
mysql:
    type: mysql:10.0
    disk: 2048
```

See the [Set up MySQL service](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/configure/service/mysql) article for reference.

Once you change the `.magento/services.yaml` file, you need to commit and push your changes, for them to be applied. The push will trigger the deployment process.

>[!WARNING]
>
>A Starter plan partition should never be made smaller (for example, going from 30GB to 20GB) as this will likely result in catastrophic data corruption.

## Allocate space on Pro plan Staging or Production

To make these changes for the Staging or Production environment of the Pro plan, you must create a [support ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md#merchant-not-displayed). When submitting a support ticket to increase storage, support will need to know how much and to what partition the storage should be applied to (`/mysql` or `/exports`). A storage increase request requires approval from your Adobe Account Team, who will review your entitled amount of storage (as per the order form) before approving.

## Decreasing allocated space not available (Pro and Starter plan)

Adobe Commerce Support can grow a partition (`/mysql` or `/exports`), but cannot shrink a partition. There is risk of data corruption in doing so, that is why decreasing storage for a partition isn't available.
It is also true for the Starter plan, where you can increase the allocated space yourself: decreasing is highly not recommended and might result in catastrophic data corruption.
