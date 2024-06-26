---
title: The `Magento-cloud` [!DNL CLI] doesn't show an active environment
description: This article describes a known Adobe Commerce issue where the `Magento-cloud` [!DNL CLI] (command-line tool) does not show an active environment.
feature: Cloud, Integration, Configuration
role: Developer
exl-id: 3c1b5de2-8888-4531-9dc1-cd478e3c96fc
---
# The `Magento-cloud` [!DNL CLI] doesn't show an active environment

## Issue

There are several active environments, and you are trying to interact with an environment by running a `Magento-cloud` [!DNL CLI] (command-line tool) command. (For example: `ssh`, `db:size`, `db:sql`, etc.)
However, the prompt to choose the desired environment doesn't list this environment. (For example: the integration environment)

```
Enter a number to choose an environment:
Default: master
  [0] integration2 (type: development)
  [1] master (type: development)
  [2] production
  [3] staging
 >
```

## Cause

The environment may not be available due to a deployment that is in progress, stuck, or has failed.

## Solution

You will have to manually specify the environment with the `e|-environment` flag.

1. Find the list of active environments and take note of the environment names:

```
$ magento-cloud environment: list |grep "Active\|ID"
Your environments are:

| ID                     | Title            | Status       | Type           |
| Master                 | Master           | Active       | Development    |
|   Production           | Production       | Active       | Production     |
|     Staging            | Staging          | Active       | Staging        |
|       Integration      | Integration      | Active       | Development    |
|          Integration 2 | Integration 2    | Active       | Development    |
```

 2.Specify the environment's ID with your command:

   `magento-cloud ssh -e integration`
