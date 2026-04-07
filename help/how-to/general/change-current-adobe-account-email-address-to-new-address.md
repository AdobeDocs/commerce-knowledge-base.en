---
title: Change current Adobe account email address
description: Learn how to change the current email address registered in the Adobe account to a new address currently not registered in the Adobe account or the Magento account.
exl-id: ca549d38-0d62-4206-9727-0ed85b733dc3
feature: Communications
---
# Change current Adobe account email address

This article explains how to change the current email address registered in the [Adobe account](https://account.adobe.com/) to a new address currently not registered in the [Adobe account](https://account.adobe.com/) or the [Magento account](https://account.magento.com/).

## Affected products and versions

* Adobe Commerce (all deployment methods and versions)

## Prerequisites 

The owner of the new email address must have access to the current email address.

If you do not have access to the current email address, set up email forwarding from the current owner's email to a new email using the company mail server configuration.

## Steps to change the email address

Follow these steps to change the email address:

1. Reset the password used with the old email address. Follow the instructions given in [Reset forgotten password](https://helpx.adobe.com/manage-account/using/change-or-reset-password.html) in Adobe helpx.
1. The password reset link is sent to the current owner's mailbox with instructions.
1. Navigate to the [Adobe account page](https://account.adobe.com) to log in with the new email and set up the password.

## Important: Cloud account username is not updated automatically

If you use Adobe Commerce on cloud infrastructure, changing the email address on your Adobe account or MAGE ID does not automatically update the username shown in your [Cloud account](https://accounts.magento.cloud).

After completing the steps in this article to change your Adobe account email address:

1. Sign in to your Cloud account at [https://accounts.magento.cloud](https://accounts.magento.cloud).
1. Manually update the Cloud account profile (username) by following the steps in [How to update the cloud account profile](/help/how-to/general/how-to-update-the-cloud-account-profile.md) in our support knowledge base.

This ensures that your Cloud account username stays aligned with your updated Adobe or MAGE ID email and avoids confusion when accessing cloud projects or receiving system notifications.

## Verify Marketplace and Support access after the email change

After you change the email address for your MAGE ID, you must also complete the following steps to ensure that Adobe Commerce Marketplace and Support correctly recognize your new email:

### Verify Commerce Marketplace email

1. Log in to [https://commercemarketplace.com/customer/account](https://commercemarketplace.com/customer/account) and confirm that your account email has been updated to the new address.
1. If the email has not been updated, submit a Support ticket requesting that the Commerce Marketplace account email be corrected.

### Ask Support to finalize internal account updates

1. Submit a Support ticket asking us to complete any required internal updates (for example, updating the linkage between your old and new Adobe IDs and your MAGE ID).
1. If you already opened a ticket because the Commerce Marketplace email did not update (step 1), you can use the same ticket to request these additional internal updates.
