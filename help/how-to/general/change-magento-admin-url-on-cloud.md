---
title: Change Admin URL on Adobe Commerce on cloud infrastructure
description: By default, the [Commerce Admin](https://docs.magento.com/m2/ee/user_guide/stores/admin.html) URL is set to *&lt;domain\_name&gt;/admin*. This article shows how to change the URL.
exl-id: 6236370c-e0a2-45a6-a38f-12e219c540af
feature: Admin Workspace, Cloud
---
# Change Admin URL on Adobe Commerce on cloud infrastructure

By default, the [Commerce Admin](https://experienceleague.adobe.com/docs/commerce-admin/start/admin/admin.html) URL is set to *<domain\_name>/admin*. This article shows how to change the URL.

## Method 1: Change using the Admin

Read the steps: [Using a Custom Admin URL > Change from the Admin](https://experienceleague.adobe.com/docs/commerce-admin/stores-sales/site-store/store-urls.html#use-a-custom-admin-url) in our user guide.

## Method 2: Add ADMIN\_URL environment variable

### Integration environment

From your [Project Web Interface](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/project/overview.html), add a new variable with:

 **Name:** ADMIN\_URL **Value:** new Admin URL

* For detailed steps, see [add environment variables](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/project/overview.html#configure-environment) in our developer documentation.
* Also refer to [environment variables](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/configure/env/stage/variables-admin.html) in our developer documentation.

### When Staging and Production are not available in Project Web Interface

 [Submit a support ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket) requesting to add the ADMIN\_URL variable for your Staging or Production environment.

If Staging and Production are accessible from your Project Web Interface, add the Environment Variable as described in the *Integration environment* section above.

### Add variables using Cloud CLI

See [Add environment variables](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/configure/env/stage/variables-admin.html) in our developer documentation for detailed steps.

We don't recommend adding **global** variables via Cloud CLI (the `magento-cloud project:variable:set <name> <value>` command) since such global variables:

* get inherited by your Staging/Production environments (if these are included in your Project Web Interface)
* trigger the undesired redeploy process on all branches/environments of your project

We recommend adding environment variables for every branch/environment using the `magento-cloud variable:set` command.
