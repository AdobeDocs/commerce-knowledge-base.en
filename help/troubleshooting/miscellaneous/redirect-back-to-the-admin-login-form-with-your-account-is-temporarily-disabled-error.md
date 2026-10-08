---
title: Redirect back to the [!UICONTROL Commerce Admin] login form with "Your account is temporarily disabled" error
description: 'This article provides the possible solutions for the Commerce Admin login issue, where you are redirected back to the login form with the following error message: *"Your account is temporarily disabled"*. The suggested solution is checking and correcting the admin user database settings.'
exl-id: 1c7ffa1c-1fb1-4f69-9534-77d1e119318a
feature: Admin Workspace, Customer Service
role: Developer
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: e7dae43f-215c-4cdf-90d3-c5a461a6e669
    internal-label: Admin tools and workspace
  - id: da76473c-f99b-5ad0-9b14-896aed473f8a
    internal-label: Services
subfeature_v2:
  - id: bb2df8be-afdd-4818-b6b5-95ca1dd3bc3a
    internal-label: Admin workspace
  - id: deedbb4d-f1b7-58ea-a34a-de1f481f9d4c
    internal-label: Customer Service
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# Redirect back to the [!UICONTROL Commerce Admin] login form with "Your account is temporarily disabled" error

This article provides the possible solutions for the [!UICONTROL Commerce Admin] login issue, where you are redirected back to the login form with the following error message: *"Your account is temporarily disabled"*. The suggested solution is checking and correcting the admin user database settings.

## Affected editions and versions:

All Adobe Commerce versions and editions

## Issue

<u>Steps to reproduce</u>:

1. Go to the **[!UICONTROL Commerce Admin]** page.
1. Enter your credentials and click **Sign in**.

<u>Expected result</u>:

You get logged in to the [!UICONTROL Commerce Admin].

<u>Actual result</u>:

You are redirected back to the login form, with the following error message displayed: *"Your account is temporarily disabled. Please try again later"*.

## Solution

1. Create a database backup.
1. Use a database tool such as [[!DNL phpMyAdmin]](https://experienceleague.adobe.com/en/docs/commerce-operations/installation-guide/prerequisites/optional-software#phpmyadmin), or access the DB manually from the command line. In the `admin_user` database table, for your admin user record, check if `is_active` is set to "`1`" and `lock_expires` is `NULL`. Reset these values, if required.

## Related reading

* [Best practices for modifying database tables](https://experienceleague.adobe.com/en/docs/commerce-operations/implementation-playbook/best-practices/development/modifying-core-and-third-party-tables#why-adobe-recommends-avoiding-modifications) in the Commerce Implementation Playbook
