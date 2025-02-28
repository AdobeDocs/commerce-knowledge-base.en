---
title: 'Adobe Commerce on-premises 2.4.2: product image missing'
description: This article describes a known Adobe Commerce on-premises 2.4.2 issue where the product image is not uploaded to the product page. This issue is scheduled to be addressed in a future version after version 2.4.3. There is not a solution available at this time, but as a workaround, you can disable Nginx to resize images.
exl-id: c4d9240e-5df5-4eab-bb4e-1f06f9bd3a1e
feature: Iaas, Products, Storefront
role: Admin
---
# Adobe Commerce on-premises 2.4.2: product image missing

This article describes a known Adobe Commerce on-premises 2.4.2 issue where the product image is not uploaded to the product page. This issue is scheduled to be addressed in a future version after version 2.4.3. There is not a solution available at this time, but as a workaround, you can disable Nginx to resize images.

## Affected products and versions

* Adobe Commerce on-premises 2.4.2

## Issue

The product image is saved in the `s3` bucket, but it is not synced back to the `pub/media` directory. This issue only happens when using both:

* Site-enabled Nginx to resize images
* AWS `s3` as media storage

<u>Prerequisites</u>:

Adobe Commerce installed with Nginx.

<u>Steps to reproduce</u>:

1. Configure Adobe Commerce to use AWS `s3` as media storage.
1. Configure Nginx using the `nginx.conf.sample` configuration file provided in the Adobe Commerce installation directory and an Nginx virtual host. See [Configure Nginx](https://experienceleague.adobe.com/en/docs/commerce-operations/installation-guide/prerequisites/web-server/nginx) in our developer documentation.
1. Create a simple product with one product image.
1. Nginx has an uncommented configuration for image resizing in `nginx.conf.sample` similar to this:

```conf
load_module /etc/nginx/modules/ngx_http_image_filter_module.so;
location /media/ {
    location ~* ^/media/catalog/.* {
        set $width "-";
        set $height "-";
        if ($arg_width != '') {
            set $width $arg_width;
        }
        if ($arg_height != '') {
            set $height $arg_height;
        }
        image_filter resize $width $height;
        image_filter_jpeg_quality 90;
    }
```

 <u>Expected results</u>:

 The product image is uploaded to the product page.

 <u>Actual results</u>:

 The product image is not uploaded to the product page.

## Workaround

Disable Nginx to resize images.
