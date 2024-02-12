---
title: Cannot access Adobe Commerce on cloud infrastructure UI
description: This article provides solutions for the issue where you cannot log in to your Adobe Commerce on cloud infrastructure UI and get the "403 error".
exl-id: 948e4acd-abd6-4562-b9c0-771a977188ba
feature: Cloud, Paas
role: Developer
---
# Cannot access Adobe Commerce on cloud infrastructure UI

This article provides solutions for the issue where you cannot log in to your Adobe Commerce on cloud infrastructure UI and get the *403 error*.

## Issue

When trying to log in to your Adobe Commerce on cloud infrastructure UI for the first time, you get a *403: Environment Access Denied* error. This error might occur because going to the cloud URL for the first time loads the master branch, and you might not have access to that branch.

## Solution

If you get a 403 error when accessing the URL for the first time, make sure you have a role in the master branch.

1. Сontact the license owner or a super user on the project and make sure they provided access to you as an **environment-level user**, also described in [Cloud projects > Manage users from the Project Web UI](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/project/user-access.html) in our developer documentation.

    If you only have an applicable role in a specific branch, then you would need to go to the URL for that branch, e.g., 
    `https://console.adobecommerce.com/<owner-name>/<project-id>/<branch-name>`

    The next time you access the main URL, it will default to the last environment you've visited.

1. If you still cannot log in, сontact the license owner or a super user on the project and make sure they provided access for you as a **project-level user**, as described in step 5 in [Cloud projects > Manage users from the Project Web UI](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/project/user-access.html) in our developer documentation.
1. If the error persists, [submit a support ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket).
