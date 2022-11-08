---
title: Error enabling Image Optimization in Adobe Commerce
description: This article provides a solution for the issue when Fastly Image Optimization (IO) is disabled by default with a notification to contact Fastly to enable image optimization. (The Fastly Cloud Image Optimizer is a real-time image manipulation and optimization service that speeds up image delivery by serving bandwidth-efficient images.)
exl-id: 7b64c786-3c74-4642-b0d0-15b5648163a0
---
# Error enabling Image Optimization in Adobe Commerce

This article provides a solution for the issue when Fastly Image Optimization (IO) is disabled by default with a notification to contact Fastly to enable image optimization. (The Fastly Cloud Image Optimizer is a real-time image manipulation and optimization service that speeds up image delivery by serving bandwidth-efficient images.)

## Affected products and versions

* Adobe Commerce on cloud infrastructure 2.2.x, 2.3.x

## Issue

On the Fastly Configuration page, next to the Fastly IO Snippet, you see the Current state: \_disabled \_with the following message underneath: Please contact your sales rep or send an email to `support@fastly.com` to request image optimization activation for your Fastly service.

## Cause

The site may not be live yet. There are processes in place to pre-load the site when it goes live in the Fastly database.

## Solution

Create a [Support ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket) and request image optimization.
