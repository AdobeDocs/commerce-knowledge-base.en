---
title: Google Analytics gets disabled after deployment
description: This topic discusses a solution to a typical issue you might experience with Google Analytics during deployment.
exl-id: ecf6a277-2dfa-45cf-b86f-9a27f39017f4
feature: Build, Deploy, Variables
role: Developer
---
# Google Analytics gets disabled after deployment

This topic discusses a solution to a typical issue you might experience with Google Analytics during deployment.

## Affected products and versions

* Adobe Commerce on cloud infrastructure, all versions

## Issue

When deploying your code across environments, the build and deploy scripts verify the `master/production/staging` branch is deployed to keep Google Analytics enabled. When deploying develop (or child) branches of master to developer environments (Integration), the deploy script disables Google Analytics.

## Cause

This is an intended feature to ensure that developer data and interactions are not sent to or tracked by Google Analytics.

## Solution

If you want to have Google Analytics always enabled, set the deploy variable `ENABLE_GOOGLE_ANALYTICS = true`, as described in [Deploy variables](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/configure/env/stage/variables-deploy#enable_google_analytics) in our developer documentation.

>[!NOTE]
>
>We are aware that this article may still contain industry-standard software terms that some may find racist, sexist, or oppressive and which may make the reader feel hurt, traumatized, or unwelcome. Adobe is working to remove these terms from our code, documentation, and user experiences.
