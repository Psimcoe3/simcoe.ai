[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidFilledRegionTypeId Method

---



|  |
| --- |
| [FilledRegion Class](3685651c-a789-3550-f6bb-7c1decc29079.htm)   [See Also](#seeAlsoToggle) |

Indicates whether the given Id is a valid filled region type Id.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static bool IsValidFilledRegionTypeId( 	Document document, 	ElementId typeId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsValidFilledRegionTypeId ( _ 	document As Document, _ 	typeId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsValidFilledRegionTypeId( 	Document^ document,  	ElementId^ typeId ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

typeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The filled region type Id.

#### Return Value

True if it is a valid filled region type Id, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FilledRegion Class](3685651c-a789-3550-f6bb-7c1decc29079.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)