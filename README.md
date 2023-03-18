Data Visualization using Python, PyViz, and HvPlot.
======
The purpose of this repository is to display the functionality of Hvplot. As a data analyst, being able to gain insights through data visualization is an important skill. Hvplot is a Python library for creating interactive data visualizations in Jupyter notebooks and web applications. It is built on top of the HoloViews library and provides a simple interface for creating high-level plots with concise and intuitive syntax. Hvplot supports a wide range of chart types, including line plots, scatter plots, bar charts, histograms, and more, and allows you to customize the appearance and behavior of your plots using a variety of options.

Procedure & Screenshots
======
The .csv file we are working with contains 397 rows and 5 columns. We are going to read in the data using the Path library and display some rows.

![alt text](https://github.com/Gsilvera24/Data-Visualization/blob/main/screenshots/real_one.png "VS CODE")

Next, using the group by function we will aggregate the data by year and obtain the average. 

![alt text](https://github.com/Gsilvera24/Data-Visualization/blob/main/screenshots/real_two.png "VS CODE")

Once the data is aggregated in this maner we will simply call an Hvplot function to create a bar chart displaying average rent per year during the lenght of the data provided.

![alt text](https://github.com/Gsilvera24/Data-Visualization/blob/main/screenshots/real_three.png "VS CODE")
