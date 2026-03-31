[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddProfile Method

---



|  |
| --- |
| [Form Class](49f6ae4c-1629-98ef-d9a9-799bb1fd43ec.htm)   [See Also](#seeAlsoToggle) |

Add a profile into the form, by a specified edge/param.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public int AddProfile( 	Reference edgeReference, 	double param ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function AddProfile ( _ 	edgeReference As Reference, _ 	param As Double _ ) As Integer ``` |

 

| Visual C++ |
| --- |
| ``` public: int AddProfile( 	Reference^ edgeReference,  	double param ) ``` |

#### Parameters

edgeReference
:   Type:  [Autodesk.Revit.DB Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     The geometry reference of edge.

param
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The param on edge to specify the location.

#### Return Value

Index of newly created profile.

# See Also

[Form Class](49f6ae4c-1629-98ef-d9a9-799bb1fd43ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)