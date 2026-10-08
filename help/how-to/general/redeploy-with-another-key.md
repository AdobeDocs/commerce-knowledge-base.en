---
title: 'Adobe Commerce on cloud: change authentication keys and redeploy'
description: This article provides instructions on how to redeploy Adobe Commerce on cloud infrastructure with different authentication keys. For example, you might have used the keys for another account or you might have used Magento Open Source keys instead of Adobe Commerce keys.
exl-id: 47407c81-5c52-406f-812f-6c6b3ca5cafa
feature: Cloud, Deploy
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: 5a951749-fac9-5bc7-9a98-ebe4ff066437
    internal-label: Cloud
  - id: bcd8874c-7b93-5596-bdaa-22660e84df14
    internal-label: Deploy
---
# Adobe Commerce on cloud: change authentication keys and redeploy

This article provides instructions on how to redeploy Adobe Commerce on cloud infrastructure with different authentication keys. For example, you might have used the keys for another account or you might have used Magento Open Source keys instead of Adobe Commerce keys.

If you used the incorrect keys, deployment fails. To recover, you must clone the project, add the correct keys to `auth.json`, and push the change to the master branch.

In this article, we assume that your project has a `master` branch only (`master` is the default branch when you first create a project).

To redeploy with the correct authentication keys:

1. Log in to the machine that has your Adobe Commerce on cloud infrastructure SSH keys.
1. Log in to the project:

    ```
    magento-cloud login
    ```

1. Create a branch to update code with the name `auth`:

    ```
    magento-cloud environment:branch auth master
    ```

1. Change to the project root directory.
1. Open `auth.json` in a text editor.

    ```json
    {
       "http-basic": {
          "repo.magento.com": {
             "username": "<your public key>",
             "password": "<your private key>"
          }
       }
    }
    ```

1. Add the correct authentication keys.
1. Save your changes and exit the text editor.
1. Commit and merge your changes.

    ```
    git add -A
    ```

    ```
    git commit -m "<description of change>"
    ```

    ```
    git push origin master
    ```

1. Wait for the deployment to complete.

Messages indicate whether deployment was successful. You can confirm a successful deployment by going to one of the **Environment routes** displayed on your screen.
