## -*- coding: utf-8 -*-
# parameter %r refers to get the value from debugs
# boolean values is sensitive with the capita letter True or False
formatter="%r %r %r %r"
print formatter % (1,2,3,4)
print formatter % ("one","two","three","four")
print formatter % (True,False,False,True)
print formatter % (formatter,formatter,formatter,formatter)
print formatter % (
	"This tutorial is a little exausting but i'm enjoying to get a great knowledge",
	"Well second line",
	"Third line and the last one is following",
	"The last and ultimate."
	)

