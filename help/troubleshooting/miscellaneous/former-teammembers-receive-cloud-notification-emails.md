---
title: Former team members receive Adobe Commerce cloud notification emails
description: This article provides a solution to Adobe Commerce on cloud infrastructure notification emails being sent to former team members.
exl-id: b2535f66-8aec-4ddf-9a69-60879a0a1939
feature: Cloud, Communications, Paas
role: Developer
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: 5a951749-fac9-5bc7-9a98-ebe4ff066437
    internal-label: Cloud
  - id: bb03f6c4-cab9-560e-9d02-5816e1808d17
    internal-label: Communications
  - id: 00451af3-7b97-5414-9992-3a6c269e413f
    internal-label: Paas
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# Former team members receive Adobe Commerce cloud notification emails

This article provides a solution for removing users from the recipients' list of notification emails who are:

* Former team members who are no longer associated with your project.
* Current team members who should not be receiving the notifications.

## Issue

A notice of a detected outage or important issue regarding the cloud project/environment has been sent to your team. This includes members that may no longer be associated with your project such as external/agency developers or system integrators. You want these users to stop receiving notifications.

## Solution

>[!NOTE]
>
>If you are an external/agency developer or system integrator and are no longer associated with the project, you must reach out to the Project Owner or the Project Admin on that project for assistance.

There are two ways to stop the notifications by removing the user(s) from your project:

* Method 1: Using the cloud [!DNL Project URL]. Refer to [Manage user access](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/project/user-access.html) in the Commerce on cloud infrastructure guide for steps.  
* Method 2: Using the magento-cloud [!DNL CLI]. Refer to [Manage users with the [!DNL CLI]](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/project/user-access.html#manage-users-with-the-cli) in the Commerce on cloud infrastructure guide for steps.

If this has already been done and yet the email notifications continue to include those users, submit a support ticket to request that they be removed from the *[!UICONTROL Always CC]* setting on the account.

## Related reading

* [View a user's project role](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/project/user-access.html#view-a-user's-project-role) in the Commerce on cloud infrastructure guide.
* [How to include a team member in Support notifications](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/how-to/how-to-include-a-team-member-in-support-notifications.html) in the Commerce KB.
