[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddEdge Method (Reference, Double, Reference, Double)

---



|  |
| --- |
| [Form Class](49f6ae4c-1629-98ef-d9a9-799bb1fd43ec.htm)   [See Also](#seeAlsoToggle) |

Add an edge to the form, connecting two edges on same/different profile, by a pair of specified edge/param.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public void AddEdge( 	Reference startEdgeReference, 	double startParam, 	Reference endEdgeReference, 	double endParam ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AddEdge ( _ 	startEdgeReference As Reference, _ 	startParam As Double, _ 	endEdgeReference As Reference, _ 	endParam As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AddEdge( 	Reference^ startEdgeReference,  	double startParam,  	Reference^ endEdgeReference,  	double endParam ) ``` |

#### Parameters

startEdgeReference
:   Type:  [Autodesk.Revit.DB Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     The geometry reference of start edge

startParam
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The param on start edge to specify the location.

endEdgeReference
:   Type:  [Autodesk.Revit.DB Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     The geometry reference of end edge

endParam
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The param on end edge to specify the location.

# See Also

[Form Class](49f6ae4c-1629-98ef-d9a9-799bb1fd43ec.htm)

[AddEdge Overload](6b262498-8f41-e7d0-0c08-2e2f9ab34707.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)