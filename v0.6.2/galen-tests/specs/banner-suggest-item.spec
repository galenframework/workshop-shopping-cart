===================================

image           css .item-icon img
title           css .item-title
description     css .item-description
price           css .item-price

===================================



@ Banner item | *
-----------------------------

image
    inside: parent 0px top left bottom
    width: 64px
    height: 64px

title
    aligned horizontally top: image 1px
    near: image 10px right
    height: 14 to 19px
    width: > 10px
    inside: parent > -1px right

description
    aligned vertically left: title
    height: 14 to 20px
    below: title 0 to 1px
    inside: parent > -1px right

price
    aligned vertically left: title
    height: 14 to 20px
    aligned horizontally bottom: image 1px


