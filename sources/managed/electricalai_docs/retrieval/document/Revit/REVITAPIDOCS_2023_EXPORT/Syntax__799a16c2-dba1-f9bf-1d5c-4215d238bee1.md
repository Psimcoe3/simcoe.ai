[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetLineStyleId Method

---



|  |
| --- |
| [FilledRegion Class](3685651c-a789-3550-f6bb-7c1decc29079.htm)   [See Also](#seeAlsoToggle) |

Sets the line style Id for all boundaries.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public void SetLineStyleId( 	ElementId lineStyleId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetLineStyleId ( _ 	lineStyleId As ElementId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetLineStyleId( 	ElementId^ lineStyleId ) ``` |

#### Parameters

lineStyleId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The line style Id.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | lineStyleId is not a valid line style Id for a filled region. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FilledRegion Class](3685651c-a789-3550-f6bb-7c1decc29079.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)