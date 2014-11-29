
@@ import common.spec

======================================================
main-title          css     #main-container h1

cart-item-*         css     #shopping-cart  .cart-item

total-label         css     .total span
pay-button          css     .btn.button-pay
cancel-button       css     .btn.button-cancel
======================================================


@@ set cartsNum         ${count("cart-item-*")}
@@ set lastCartItem     cart-item-${cartsNum}


@ Shopping Cart items | *
------------------------------------------------------
main-title
    inside: main 15px top left
    height: ~ 30px
    text is: Shopping Cart

cart-item-*
    height: > 40px
    component: cart-item.spec


cart-item-1
    below: main-title ~ 10px

total-label
    below: ${lastCartItem} 10 to 20px 
    width: 100 to 150px
    inside: main 15 px right


pay-button
    aligned horizontally all: cancel-button
    below: total-label 40 to 50px 
    height: ~ 45px


@^| desktop
-----------------------------------------------
cart-item-*
    inside: main 15px left right

[ 2 - ${cartsNum} ]
cart-item-@
    below: cart-item-@{-1} ~15 px



@^| desktop, tablet
-----------------------------------------------
pay-button
    width: 50 to 120px
    text is: Pay
    inside: main 15 px left, ~ 30px bottom

cancel-button
    width: 50 to 120px
    near: pay-button 4 to 10px right
    text is: Cancel




@^| tablet, mobile 
-----------------------------------------------
cart-item-*
    inside: main 0 to 1px left right

[ 2 - ${cartsNum} ]
cart-item-@
    below: cart-item-@{-1} 0 to 1 px


@^| mobile
-----------------------------------------------
pay-button
    inside: main 15px left, 30px bottom

cancel-button
    inside: main 15px right, 30px bottom
    near: pay-button 4 to 10px right 



