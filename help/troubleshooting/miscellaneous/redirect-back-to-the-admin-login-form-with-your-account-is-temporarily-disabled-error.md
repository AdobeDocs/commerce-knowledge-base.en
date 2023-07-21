---
title: Redirect back to the Commerce Admin login form with "Your account is temporarily disabled" error
description: 'This article provides the possible solutions for the Commerce Admin login issue, where you are redirected back to the login form with the following error message: *"Your account is temporarily disabled"*. The suggested solution is checking and correcting the admin user database settings.'
exl-id: 1c7ffa1c-1fb1-4f69-9534-77d1e119318a
feature: Admin Workspace, Customer Service
---
# Redirect back to the Commerce Admin login form with "Your account is temporarily disabled" error

This article provides the possible solutions for the Commerce Admin login issue, where you are redirected back to the login form with the following error message: *"Your account is temporarily disabled"*. The suggested solution is checking and correcting the admin user database settings.

## Affected editions and versions:

All Adobe Commerce versions and editions

## Issue

<u>Steps to reproduce</u>:

1. Go to the Commerce Admin page.
1. Enter your credentials and click Sign in.

<u>Expected result</u>:

You get logged in to the Commerce Admin.

<u>Actual result</u>:

You are redirected back to the login form, with the following error message displayed: *"Your account is temporarily disabled. Please try again later"*.

## Solution

1. Create a database backup.
1. Use a database tool such as [phpMyAdmin](https://devdocs.magento.com/guides/v2.2/install-gde/prereq/optional.html#install-optional-phpmyadmin), or access the DB manually from the command line. In the `admin_user` database table, for your admin user record, check if `is_active` is set to "`1`" and `lock_expires` is `NULL`. Reset these values, if required.

## Related reading in our support knowledge base

* [Redirect back to the login form with no error, when trying to login to the Commerce Admin](/help/troubleshooting/miscellaneous/login-redirect-when-trying-to-login-to-magento-admin.md)
