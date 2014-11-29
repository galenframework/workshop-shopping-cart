
============================================

main-category       css     a.main-category
sub-item-*          css     a.sub-item

============================================


@ Navigation | desktop
----------------------------------------
main-category
    inside: parent ~ 0px top left
    height: 22 to 25px

sub-item-1
    below: main-category 0 to 2px
    inside: parent 15px left
    height: 16 to 20px

sub-item-*
    width: > 50px
    height: < 100% of main-category/height

[ 2 - ${count("sub-item-*")} ]
sub-item-@
    below: sub-item-@{-1} 2px
    height: 100% of sub-item-1/height
    aligned vertically left: sub-item-1


@^| tablet, mobile
----------------------------------------

sub-item-*
    absent



