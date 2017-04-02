# Lesson 4 Function Definition

By now you would have seen some of the function defintion that is similar to what you learn in C, Java and even C#. Of course again the syntax is different and Python is usually much more flexible.

There are tons of great resources online that teaches python, it is not my intention to create just another of these tutorial. 
The intention is to cultivate the ability to use online resource to adapt to new language.
We would be following, the following tutorial closely for our workshop:

[The Python Tutorial](https://docs.python.org/2/tutorial/index.html) and
[Hands-on Python Tutorial](http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/functions.html)


Some other links:

* [Python 2.7 Tutorial](http://www.pitt.edu/~naraehan/python2/index.html)
* [A Python 2.7 Programming Tutorial](http://infohost.nmt.edu/tcc/help/pubs/lang/pytut27/web/index.html)
* [Python Basic Syntax](https://www.tutorialspoint.com/python/python_basic_syntax.htm)
* and lot more if you google properly

## Introduction

Please refer to [The Python Tutorial on function definition](https://docs.python.org/2/tutorial/controlflow.html#defining-functions) section 4.6 and 4.7
and also [Hands-on Python Tutorial](http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/functions.html)


### Assignment 1

In this assignment we are going to use the data.gov.sg "Surface Air Temperature - Monthly Mean"
Please refer to [https://data.gov.sg/dataset/surface-air-temperature-monthly-mean](https://data.gov.sg/dataset/surface-air-temperature-monthly-mean)for the detail and also download the csv file.


The tasks are to:

* Compute the mean and standard deviation of the monthly surface air temperature
* Find the maximum monthly surface air temperature and its corresponding date
* Find the minimium monthly surface air temperature and its corresponding date

A few requirements to create the following functions:

* def readcsv(datafile) where datafile is the file name of the csv file to be read and the function return list with two column (datetime and float)
* def computemean(data) where data is the array of surface temperature and the function return the mean temperature
* def computestd(data) where data is the array of the surface temperature and the function return the standard deviation of surface air temperature

Hint: You could reference to lesson 3 assignmet 2 solution as your reference.




