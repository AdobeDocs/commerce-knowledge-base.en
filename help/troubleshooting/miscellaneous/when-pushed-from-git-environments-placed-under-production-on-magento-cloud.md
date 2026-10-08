---
title: New environments placed under production when pushed from Git
description: This article provides a solution for the issue where new environments are placed under the production environment on Adobe Commerce on cloud infrastructure when pushed from the git version-control system.
exl-id: 279cd6d8-fd45-45ba-8456-8b397a01976f
feature: Cloud, Paas
role: Developer
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: 5a951749-fac9-5bc7-9a98-ebe4ff066437
    internal-label: Cloud
  - id: 00451af3-7b97-5414-9992-3a6c269e413f
    internal-label: Paas
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# New environments placed under production when pushed from Git

This article provides a solution for the issue where new environments are placed under the production environment on Adobe Commerce on cloud infrastructure when pushed from the git version-control system.

## Affected products and versions

* Adobe Commerce on cloud infrastructure, [all supported versions](https://magento.com/sites/default/files/magento-software-lifecycle-policy.pdf).

## Issue

<u>Prerequisites</u>:

Have a local git controlled clone of the project.

<u>Steps to reproduce</u>:

You need to create an integration branch from the staging branch:

1. Switch to the staging branch by running the following command in the local shell: `git checkout staging`
1. Create an integration branch from the staging branch by running the following command in the local shell: `git checkout -b <branch>`
1. Push the branch to the remote repository and set up an upstream branch by running the following command in the local shell: `git push --set-upstream origin <branch>`

<u>Expected results</u>:

The new branch is created under the staging branch.

<u>Actual results</u>:

The new branch was created under the production branch.

## Cause

This is not a bug. For setting a parent branch for another branch, the merchant should use the magento-cloud CLI.

## Solution

A parent branch can only be set after the merchant has pushed a newly created branch and activated it. Refer to [Adobe Commerce on cloud infrastructure > Bitbucket integration](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/dev-tools/integrations/bitbucket#create-a-cloud-branch) in our developer documentation.

To update a parent for the existing branch on the server, please use the `magento-cloud environment:info` command in the magento-cloud CLI.

Example of usage:

 `magento-cloud environment:info parent Staging`

This will set the parent branch to "Staging" for the currently checked out branch.

## Related reading

* [Adobe Commerce on cloud infrastructure > magento-cloud CLI](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/dev-tools/cloud-cli/cloud-cli-overview) in our developer documentation.
