[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetPipeScheduleId Method

---



|  |
| --- |
| [PipeScheduleType Class](d580725f-60f3-034a-e358-d4ed8896d915.htm)   [See Also](#seeAlsoToggle) |

Returns an existing pipe schedule type with the same name.

**Namespace:**   [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public static ElementId GetPipeScheduleId( 	Document doc, 	string name ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetPipeScheduleId ( _ 	doc As Document, _ 	name As String _ ) As ElementId ``` |

 

| Visual C++ |
| --- |
| ``` public: static ElementId^ GetPipeScheduleId( 	Document^ doc,  	String^ name ) ``` |

#### Parameters

doc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document

name
:   Type:  System String    
     The name of requested schedule type.

#### Return Value

Returns the element id of request schedule type, or invalidElementId if the name is not found.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PipeScheduleType Class](d580725f-60f3-034a-e358-d4ed8896d915.htm)

[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.htm)