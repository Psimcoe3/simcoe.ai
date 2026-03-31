[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsAllowedTagType Method

---



|  |
| --- |
| [MultiReferenceAnnotationType Class](046b4d91-40b3-4dd0-be1b-635fb30956c2.htm)   [See Also](#seeAlsoToggle) |

Checks if the tag type can be assigned to this multi-reference annotation type.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public bool IsAllowedTagType( 	ElementId tagTypeId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsAllowedTagType ( _ 	tagTypeId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsAllowedTagType( 	ElementId^ tagTypeId ) ``` |

#### Parameters

tagTypeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The tag type to test.

#### Return Value

True if the tag type exclusively tags elements from the multi-reference annotation's reference category.

# Remarks

Only tag types which exclusively tag elements from the multi-reference annotation's reference category can be used.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[MultiReferenceAnnotationType Class](046b4d91-40b3-4dd0-be1b-635fb30956c2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)