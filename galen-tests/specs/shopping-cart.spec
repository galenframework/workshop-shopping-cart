
@@ import common.spec

======================================================
main-title          css     #main-container h1

cart-item-*         css     #shopping-cart  .cart-item
======================================================


@@ set cartsNum   ${count("cart-item-*")}

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


@^| desktop
-----------------------------------------------
cart-item-*
    inside: main 15px top left

[ 2 - ${cartsNum} ]
cart-item-@
    below: cart-item-@{-1} ~15 px



@^| tablet, mobile 
-----------------------------------------------
cart-item-*
    inside: main 0 to 1px top left

[ 2 - ${cartsNum} ]
cart-item-@
    below: cart-item-@{-1} 0 to 1 px



