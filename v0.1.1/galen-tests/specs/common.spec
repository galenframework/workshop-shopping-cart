
=====================================

header          css #header
navigation      css #navigation
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


##################### NAVIGATION ##################
@ Navigation | *
-------------------
navigation
    inside: screen 0px left
    below: header 0px

@^| desktop
-----------------------
navigation
    width: 200 to 350px
    aligned horizontally all: main
    near: main 0px left

@^| tablet
-----------------
navigation
    inside: screen 0px left right
    above: main 0px
    % height: 50 to 100px

@^| mobile
----------------------
navigation
    inside: screen 0px left right
    above: main 0px
    % height: > 60px




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





