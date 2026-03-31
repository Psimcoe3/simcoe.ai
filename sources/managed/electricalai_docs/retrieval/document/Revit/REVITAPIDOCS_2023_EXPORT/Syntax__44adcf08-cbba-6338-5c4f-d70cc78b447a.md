[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetPlaneReference Method

---



|  |
| --- |
| [PointOnPlane Class](ca9299cc-2931-1a63-cacb-a41f20baf7f1.htm)   [See Also](#seeAlsoToggle) |

Change the geometric plane reference.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public void SetPlaneReference( 	Reference planeReference ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetPlaneReference ( _ 	planeReference As Reference _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetPlaneReference( 	Reference^ planeReference ) ``` |

#### Parameters

planeReference
:   Type:  [Autodesk.Revit.DB Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     A reference to some plane in the document. (Note: the reference must satisfy IsValidPlaneReference(), but this is not checked until this PointOnPlane object is assigned to a ReferencePoint.)

# See Also

[PointOnPlane Class](ca9299cc-2931-1a63-cacb-a41f20baf7f1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)