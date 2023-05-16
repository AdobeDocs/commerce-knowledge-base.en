---
title: Unable to add user to Adobe Commerce cloud project
description: This article provides a solution for when you are unable to add a user to an Adobe Commerce cloud project.
---
# Unable to add user to Adobe Commerce cloud project

## Affected products and versions

* Adobe Commerce on cloud infrastructure, [all supported versions](https://magento.com/sites/default/files/magento-software-lifecycle-policy.pdf)

## Issue

This article provides a solution for when you are unable to add a user to an Adobe Commerce cloud project.

## Cause

This is the expected behavior. The user's account should first be created at https://accounts.magento.cloud and linked to their Adobe SSO for them to be added as a user to the project.

## Solution

1. Ask the user to log in to their account at https://accounts.magento.cloud (they must have already registered for an account at adobe.com under that email address.)
Note: If the user has had an account on account.magento.com or accounts.magento.cloud prior to Aug 2022, they might not have an account with/on adobe.com unless they had created it in Aug 2022 or later. If the user does have an Adobe account and is unable to log in, please send an email to <Grp-Magento-HelpCenterLoginIssues@adobe.com> with the details. 
1. The user should then go to https://accounts.magento.cloud.
1. Once they have done that, you should be able to add the user to the project. For steps, refer to [Add users and manage access](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/project/user-access.html#add-users-and-manage-access) in our Commerce on Cloud Infrastructure Guide. 

## Related reading:

* [Manage user access](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/project/user-access.html) in our Commerce on Cloud Infrastructure Guide.
