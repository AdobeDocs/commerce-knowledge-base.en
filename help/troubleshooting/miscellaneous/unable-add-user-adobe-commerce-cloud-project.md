---
title: Unable to add user to Adobe Commerce cloud project
description: This article provides a solution for when you are unable to add a user to an Adobe Commerce cloud project.
exl-id: 59940916-bf92-4e89-a6f9-bca87c54125c
feature: Cloud, Paas
role: Developer
---
# Unable to add user to Adobe Commerce cloud project

This article provides a solution for when you are trying to add a user to a cloud project, but it fails with an error: *User XXX does not exist*.

## Affected products and versions

* Adobe Commerce on cloud infrastructure, [all supported versions](https://magento.com/sites/default/files/magento-software-lifecycle-policy.pdf)

## Issue

This article provides a solution for when you are unable to add a user to an Adobe Commerce cloud project.

## Cause

This is the expected behavior. The user's account should first be created at https://accounts.magento.cloud and linked to their Adobe SSO for them to be added as a user to the project.

## Solution

1. Ask the user to log in to their account at https://accounts.magento.cloud (they must have already registered for an account at adobe.com under that email address. Creating/having an account at https://account.adobe.com does not automatically mean that the user would have an account at https://accounts.magento.cloud)
Note: If the user has had an account on account.magento.com or accounts.magento.cloud prior to Aug 2022, they might not have an account with/on adobe.com unless they had created it in Aug 2022 or later. If the user does have an Adobe account and is unable to log in, please [submit a Support request](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/help-center-guide/magento-help-center-user-guide) at https://experienceleague.adobe.com/home#support and provide the details (Issue Reason = User Management). 
1. The user should then go to https://accounts.magento.cloud.
1. Once they have done that, you should be able to add the user to the project. For steps, refer to [Add users and manage access](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/project/user-access.html#add-users-and-manage-access) in our Commerce on Cloud Infrastructure Guide. 

## Related reading:

* [Manage user access](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/project/user-access.html) in our Commerce on Cloud Infrastructure Guide.
* [Unable to log in to Adobe Commerce support or cloud account](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/troubleshooting/miscellaneous/unable-to-log-in-to-support-or-cloud-project.html)
