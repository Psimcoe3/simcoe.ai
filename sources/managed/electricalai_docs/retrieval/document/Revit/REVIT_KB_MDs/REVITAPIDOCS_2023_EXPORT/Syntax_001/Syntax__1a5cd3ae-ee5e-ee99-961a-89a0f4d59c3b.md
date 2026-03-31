[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RotateConnectedTap Method

---



|  |
| --- |
| [FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)   [See Also](#seeAlsoToggle) |

Rotates a connected fabrication tap by the specified angles about the primary and secondary axis.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016 Subscription Release

# Syntax

| C# |
| --- |
| ``` public static void RotateConnectedTap( 	Document doc, 	FabricationPart tap, 	double primaryAxisRotateBy, 	double secondaryAxisRotateBy ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Sub RotateConnectedTap ( _ 	doc As Document, _ 	tap As FabricationPart, _ 	primaryAxisRotateBy As Double, _ 	secondaryAxisRotateBy As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: static void RotateConnectedTap( 	Document^ doc,  	FabricationPart^ tap,  	double primaryAxisRotateBy,  	double secondaryAxisRotateBy ) ``` |

#### Parameters

doc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

tap
:   Type:  [Autodesk.Revit.DB FabricationPart](c9b86162-c105-696a-a919-49a7a7938cc4.htm)    
     The connected fabrication part tap to rotate.

primaryAxisRotateBy
:   Type:  System Double    
     The primary axis rotation angle in radians to rotate by.

secondaryAxisRotateBy
:   Type:  System Double    
     The secondary axis rotation angle in radians to rotate by.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Is not connected as a fabrication part tap. -or- tap cannot be rotated about the primary axis by the specified angle: primaryAxisRotateBy -or- tap cannot be rotated about the secondary axis by the specified angle: secondaryAxisRotateBy |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)