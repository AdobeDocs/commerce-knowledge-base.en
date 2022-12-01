---
title: Cannot access Adobe Commerce on cloud infrastructure UI
description: This article provides solutions for the issue where you cannot log in to your Adobe Commerce on cloud infrastructure UI and get the "403 error".
exl-id: 948e4acd-abd6-4562-b9c0-771a977188ba
---
# Cannot access Adobe Commerce on cloud infrastructure UI

This article provides solutions for the issue where you cannot log in to your Adobe Commerce on cloud infrastructure UI and get the *403 error*.

## Issue

When trying to log in to your Adobe Commerce on cloud infrastructure UI for the first time, you get a *403: Environment Access Denied* error. This error might occur because going to the cloud URL for the first time loads the master branch, and you might not have access to that branch.

## Solution

If you get a 403 error when accessing the URL for the first time, make sure you have a role in the master branch.

1. Сontact the license owner or a super user on the project and make sure they provided access to you as an **environment-level user,** also described in [Cloud projects > Manage users from the Project Web UI](https://devdocs.magento.com/cloud/project/user-admin.html#cloud-user-webinterface) in our developer documentation.

If you only have an applicable role in a specific branch, then you would need to go to the URL for that branch, e.g., <https://region.magento.cloud/projects/PROJECTID/environments/allowed_branch>.

The next time you access the main URL, it will default to the last environment you've visited.

1. If you still cannot log in, сontact the license owner or a super user on the project and make sure they provided access for you as a **project-level user**, as described in step 5 of Manage user access to [Cloud projects > Manage users from the Project Web UI](https://devdocs.magento.com/cloud/project/user-admin.html#cloud-user-webinterface) in our developer documentation.
1. If the error persists, [submit a support ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket).
