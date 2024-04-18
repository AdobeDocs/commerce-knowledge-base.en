---
title: The `Magento-cloud` CLI doesn't show an active environment
description: This article describes a known Adobe Commerce issue where the `Magento-cloud` [!DNL CLI] (command-line tool) does not show an active environment. 
feature: Cloud, Integration, Configuration 
role: Developer
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

You have to manually specify the environment with the `e|-environment` flag.

1. Find the list of active environments and take note of the environment names:

```
$ magento-cloud environment: list |grep "Active\|ID"
Your environments are:

| ID  | Title          | Type        | Status |  
|-----|----------------|-------------|--------|
|     | Master         | Development | Active |  
|     | Production     | Production  | Active |   
|     | Staging        | Staging     | Active |   
|     | Integration    | Development | Active |   
|     | Integration 2  | Development | Active |   
```

2.Specify the environment's ID with your command:

   `magento-cloud ssh -e integration`
