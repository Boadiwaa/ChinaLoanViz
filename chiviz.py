# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 14:57:20 2022

@author: Boadiwaa
"""
import pandas as pd
from ipyvizzu import Data,Config, Style
from ipyvizzustory import Story, Slide, Step

# from colorama import Fore, Back, Style  #for formatting the output font of printed texts

data = Data()
df = pd.read_csv("D:\\Documents\\cdviz1.csv")
df.rename(columns={'Invested On': 'Sector', "Dollar_Amount": "Amount[$]"}, inplace=True)

data.add_data_frame(df)

# Exploratory data analysis of outcome variable and demographics
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())

#Create story object, add data to it
story = Story(data=data)
 
# Set the size of the HTML element
# that appears within the notebook
story.set_size("100%", "400px")
 
 
# Each slide here is a page in the final interactive story
# Add the first slide
slide1 = Slide(
    Step(
        Data.filter("record.Country == 'Ghana'"),
        Config.splittedArea(
            {
                "x": "Year",
                "y": "Amount[$]",
                "splittedBy": "Sector",
                "title": "Chinese Lending to Ghana: 2000 - 2020",
            }
        ),
        Style({"plot": {"xAxis": {"label": {"angle": 2.0}}}}),
    )
)
# Add the slide to the story
story.add_slide(slide1)
 
slide2 = Slide(
    Step(
        Config.line(
            {
                "x": "Year",
                "y": "Amount[$]",
                "dividedBy": "Sector",
                "title": "Chinese Lending to Ghana: 2000 - 2020",
               
            }
        )
    )
)
story.add_slide(slide2)
 
slide3 = Slide()

slide3.add_step(
    Step(
        Config(
            {
                "geometry": "rectangle",
            }
        )
    )
)
slide3.add_step(
    Step(
        Config(
            {#"geometry": "rectangle",
                "x": ["Year", "Sector"],
                "y": "Amount[$]",
                "label": "Amount[$]",
                "title": "Chinese Lending to Ghana: 2000 - 2020",
               
            }
        )
    )
)
slide3.add_step(Step(Config({"x": ["Sector", "Year"]})))
story.add_slide(slide3)

story.set_feature("tooltip", True)

story.play()

story.export_to_html(filename="D:\\Documents\\chinastory.html")
