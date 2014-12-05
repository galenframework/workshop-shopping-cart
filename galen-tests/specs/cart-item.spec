
=========================

image           css     img.item-main-icon
title           css     .item-title
description     css     .item-description
price           css     .item-price
quantity        css     .item-quantity

quantity-controls   css .quantity-controls
remove-link         css .remove-link

=========================



@ Cart item | *
---------------------------------------
image 
    inside: parent 14 to 16px top left bottom
    width: 64px
    height: 64px


title 
    near: image 15px right
    aligned horizontally top: image 1px
    height: 15 to 20px

description
    aligned vertically left: title
    below: title 9 to 11px
    inside: parent >9px bottom

price
    centered vertically inside: parent 1px
    near: description > 5 px right

quantity
    centered vertically inside: parent 1px
    near: price ~ 14px right


@^| desktop
-----------------------
quantity-controls
    near: quantity ~ 9px right
    centered vertically inside: parent 3px

remove-link
    near: quantity-controls ~ 9px right
    centered vertically inside: parent 2px
    inside: parent 15 to 16px right


@^| tablet, mobile
----------------------
quantity-controls, remove-link
    absent
