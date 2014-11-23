
=====================================

header              css #header
header-logo         css #header .navbar-brand img
header-caption      css #header .navbar-brand span
header-menu         css #header-menu
header-menu-login   css #header-menu a[href='#login']
header-menu-help    css #header-menu a[href='#help']
header-menubutton   css #header-menubutton


navigation          css #navigation
navigation-item-*   css #navigation > ul > li



main            css #main-container
banner-panel    css #banner-panel
footer          css #footer

=====================================

#################### HEADER ###################
@ Header | *
--------------------
header
    inside: screen 0px top left right
    height: 50px

header-logo
    inside: header 5 to 10px left
    centered vertically inside: header
    width: 24 to 35 px

header-caption
    near: header-logo 5 to 20px right
    text is: Galen Shopping Cart

@^| desktop,tablet
------------------
header-menu
    visible
    inside: header 5 to 20px right
    centered vertically inside: header

header-menu-help
    inside: header-menu 0px top right bottom
    text is: Help

header-menu-login
    inside: header-menu 0px top bottom
    near: header-menu-help 0 to 10px left

header-menubutton
    absent

@^| mobile
----------
header-menu
    absent

header-menubutton
    visible
    inside: header 5 to 20px right
    centered vertically inside: header
    width: ~ 44px
    height: ~ 32px



##################### NAVIGATION ##################
@ Navigation | *
-------------------


navigation
    inside: screen 0px left
    below: header 0px

[ 1 - 4 ]
navigation-item-@
    component: navigation.spec



@^| desktop
-----------------------
navigation
    width: 200 to 350px
    aligned horizontally all: main
    near: main 0px left
    inside: screen 0px left

navigation-item-1
    inside: navigation 15px top left right

[ 1 - 3 ]
navigation-item-@
    above: navigation-item-@{+1} ~ 15px
    inside: navigation 15px left right

navigation-item-4
    inside: navigation 15px left right, > 14px bottom


@^| tablet, mobile
-----------------
navigation
    inside: screen 0px left right
    above: main 0px
    % height: 50 to 100px



@^| tablet
-----------------
navigation-item-1
    inside: navigation 15px left, 0px top bottom
    
[ 1 - 3 ]
navigation-item-@
    near: navigation-item-@{+1} 0px left
    aligned horizontally all: navigation-item-@{+1}

navigation-item-4
    inside: navigation > 14px right


@^| mobile
-----------------
[ 1 - 4 ]
navigation-item-@
    width: 49 to 50 % of navigation/width
    height: 100% of navigation-item-1/height

[ 1 - 2 ]
navigation-item-@
    above: navigation-item-@{+2} 0px

[ 1, 3 ]
navigation-item-@
    near: navigation-item-@{+1} 0px left 

navigation-item-1
    inside: navigation 0px top left

navigation-item-2
    inside: navigation 0px top right

navigation-item-3
    inside: navigation 0 to 1px bottom left

navigation-item-4
    inside: navigation 0 to 1px bottom right




##################### FOOTER #####################
@ Footer | *
-------------------
footer
    % inside: screen 0px bottom left right
    below: banner-panel 0px
    height: 100px



#################### MAIN ########################

@ Main | desktop
-----------------------
main, banner-panel
    below: header 0px

@^| tablet
----------
main
    inside: screen 0px left
    below: navigation 0px

@^| mobile
------------------
main
    inside: screen 0px left right
    above: banner-panel 0px





################## BANNER PANEL ####################

@ Banner panel | desktop, tablet
-------------------
banner-panel
    inside: screen 0px right
    width: 220 to 400px
    near: main 0px right
    aligned horizontally all: main


@^| tablet
--------------------
banner-panel
    below: navigation 0px


@^| mobile
------------------
banner-panel
    inside: screen 0px left right
    % height: > 50px





