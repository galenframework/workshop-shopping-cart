Shopping Cart. Visual Test Driven Development (Not finished yet)
======================

This project is an experiment on Visual Test Driven Development (VTDD) for Front-end with Galen Framework. It will be later used for Galen Framework workshops.
We will try to learn how to structure our tests properly and use them during whole website development process. Good automation starts in the beginning of the project, not in the end.


The idea
=============

We are going to build a responsive Shopping Cart web page. To make it simple we will test it and develop only for 3 sizes: desktop, tablet and mobile.
The first thing we get as a requirement is this sketch https://raw.githubusercontent.com/galenframework/workshop-shopping-cart/master/docs/sketch-scan.jpeg.
We will split our development into small iterations and for each of them the first thing we do is write a Galen test. Then we implement the page and try to get our test passed. For each iteration we implement only what is needed for the current tests.


How to run it
=============

The page is located in ```website``` folder and tests are in ```galen-tests``` folder. If you use Mac or Linux you should be able to use the ```./runGalenTests.sh``` script. For Windows users I will try to come up with .bat script later


Iterations
===============

Each iteration is represented as a git tag in this project. Just clone it and run ```git tag -n99``` to see all iterations.
I have generated the overview for all iterations in here http://galenframework.github.io/workshop-shopping-cart/


Publications
===============
[Visual Test-Driven Development For Responsive Interface Design](http://www.smashingmagazine.com/2015/04/07/visual-test-driven-development-responsive-interface-design/) - this article was based on this workshop and provides the detailed explanation.


