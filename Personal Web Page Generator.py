# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 13:05:39 2022

@author: Darby Mikal Tompkins
"""

def nameInp():
  name = str(input("Name: "))
  return name

def bioInp():
  bio = input("Enter a brief bio: ")
  return bio

def webPage(name, bio):
  web = "Personal_Web_Page_Generator.html"
  openFile = open(web, "w+")
  
  openFile.write("<html>\n<head>\n</head>\n<body>\n\t<center>\n\t\t<h1>"+name+"</h1>\n\t</center>\n\t<hr />\n\t"+bio+"\n\t<hr />\n</body>\n</html>")

  openFile.close()

webPage(nameInp(), bioInp())