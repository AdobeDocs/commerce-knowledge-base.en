---
title: How to update the cloud account profile
description: This article provides steps to modify the profile on the cloud account.
feature: Cloud, Support
role: Admin, Developer
exl-id: b0c9dbcf-9745-494d-a662-80c5c6378068
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: 5a951749-fac9-5bc7-9a98-ebe4ff066437
    internal-label: Cloud
  - id: 125c1f49-aefd-5f34-a252-288937f95f6b
    internal-label: Marketing Tools
subfeature_v2:
  - id: a59f76dc-e003-5617-951e-dffa5bd3de81
    internal-label: Support
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# How to update the cloud account profile

This article provides steps on how to modify the profile on the cloud account.

## Solution

When modifying a profile on the cloud account, the following fields can be modified:

1. [!UICONTROL First name]
1. [!UICONTROL Last name]
1. [!UICONTROL Username]

    >[!NOTE]
    >
    >Updating the Cloud Console username changes the project URL from `https://console.adobecommerce.com <old-username>/<project-id>` to `https://console.adobecommerce.com/<new-username>/<project-id>`.
    >
    >After the update, links that use the old URL no longer work. Team members must update saved bookmarks, internal documentation, and any automation to use the new URL.
    >
    >This change applies only to the new Cloud Console URL. The legacy project URL (`https://<region>.magento.cloud/projects/<project-id>`) does not use the username and continues to work without change.

To modify these fields, follow these steps:

1. Access your account at [Adobe account login](https://accounts.magento.cloud).
1. Click on the **[!UICONTROL Account Settings]** tab.
1. Select the *create new password* checkbox.
1. Make the necessary changes and click *save*.

>[!NOTE]
>
>Your password will not be changed.

## What cannot be modified?

1. **[!UICONTROL Password]**:
To change your password, visit [Adobe password reset](https://account.adobe.com/), as this profile is linked to your account/email address there.

1. **[!UICONTROL Email Address]**:
Modifying this field depends on your individual circumstances.

If you need to transfer ownership of your current account to a new owner or a different email address, you will need to update the primary user email associated with the account.

Refer to: [https://experienceleague.adobe.com/docs/commerce-admin/start/commerce-account/commerce-account-transfer.html?lang=en](https://experienceleague.adobe.com/docs/commerce-admin/start/commerce-account/commerce-account-transfer.html?lang=en)
