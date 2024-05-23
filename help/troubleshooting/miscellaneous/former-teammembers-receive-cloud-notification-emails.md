---
title: Former team members receive Adobe Commerce cloud notification emails
description: This article provides a solution to Adobe Commerce on cloud infrastructure notification emails being sent to former team members.
exl-id: b2535f66-8aec-4ddf-9a69-60879a0a1939
feature: Cloud, Communications, Paas
role: Developer
---
# Former team members receive Adobe Commerce cloud notification emails

This article provides a solution for removing users from the recipients list of notification emails who are:
* former team members that are no longer associated with your project
* current team members who should not be receiving the notifications

## Issue

A notice of a detected outage or important issue regarding the cloud project/environment has been sent to your team. This includes members that may no longer be associated with your project such as external/agency developers or system integrators. You want these users to stop receiving notifications.

## Solution

There are two ways to stop the notifications by removing the user(s) from your project:

* Method 1: Using the cloud [!DNL Project URL]. Refer to [Manage user access](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/project/user-access.html) in the Commerce on cloud infrastructure guide for steps.  
* Method 2: Using the magento-cloud [!DNL CLI]. Refer to [Manage users with the [!DNL CLI]](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/project/user-access.html#manage-users-with-the-cli) in the Commerce on cloud infrastructure guide for steps.

If this has already been done and yet the email notifications continue to include those users, submit a support ticket to request that they be removed from the *[!UICONTROL Always CC]* setting on the account.

## Related reading

* [View a user's project role](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/project/user-access.html#view-a-user’s-project-role) in the Commerce on cloud infrastructure guide.
* [How to include a team member in Support notifications](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/how-to/how-to-include-a-team-member-in-support-notifications.html) in the Commerce KB.
