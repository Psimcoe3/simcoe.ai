[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ConnectDuctPlaceholdersAtCross Method (Document, Connector, Connector, Connector, Connector)

---



|  |
| --- |
| [MechanicalUtils Class](f7cbd23a-1b69-d9bf-88b4-df10a8c4be0b.htm)   [See Also](#seeAlsoToggle) |

Connects a group of placeholders that can intersect in a Cross connection.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static bool ConnectDuctPlaceholdersAtCross( 	Document document, 	Connector connector1, 	Connector connector2, 	Connector connector3, 	Connector connector4 ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function ConnectDuctPlaceholdersAtCross ( _ 	document As Document, _ 	connector1 As Connector, _ 	connector2 As Connector, _ 	connector3 As Connector, _ 	connector4 As Connector _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool ConnectDuctPlaceholdersAtCross( 	Document^ document,  	Connector^ connector1,  	Connector^ connector2,  	Connector^ connector3,  	Connector^ connector4 ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

connector1
:   Type:  [Autodesk.Revit.DB Connector](11e07082-b3f2-26a1-de79-16535f44716c.htm)    
     The end connector of the first placeholder.

connector2
:   Type:  [Autodesk.Revit.DB Connector](11e07082-b3f2-26a1-de79-16535f44716c.htm)    
     The end connector of the second placeholder.

connector3
:   Type:  [Autodesk.Revit.DB Connector](11e07082-b3f2-26a1-de79-16535f44716c.htm)    
     The end connector of the third placeholder.

connector4
:   Type:  [Autodesk.Revit.DB Connector](11e07082-b3f2-26a1-de79-16535f44716c.htm)    
     The end connector of the fourth placeholder.

#### Return Value

True if connection succeeds, false otherwise.

# Remarks

The placeholders may or may not have physical connection. However:

* The ends of four connectors should intersect at same point.
* The first and second placeholders should be collinear each other.
* The third and fourth placeholders should be collinear each other.
* The third and fourth should have intersection with first or second placeholder.

If connection fails, the placeholders cannot be physically connected.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The owner of connector is not duct placeholder. -or- The owners of connectors belong to different types of system. -or- The curves of connector1 and connector2 are not collinear or either the connecto1 or connector2 is not connector of curve end. -or- The curves of connector3 and connector4 are not collinear or either the connecto1 or connector2 is not connector of curve end. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[MechanicalUtils Class](f7cbd23a-1b69-d9bf-88b4-df10a8c4be0b.htm)

[ConnectDuctPlaceholdersAtCross Overload](92a83e26-7a54-9d57-7baf-f17e7adfd461.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)