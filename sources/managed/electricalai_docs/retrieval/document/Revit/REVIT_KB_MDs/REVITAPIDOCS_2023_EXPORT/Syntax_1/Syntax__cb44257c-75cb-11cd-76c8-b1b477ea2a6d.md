[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CanCreateOnMultistoryStairs Method

---



|  |
| --- |
| [StairsPath Class](ed5913d6-1219-9c7c-7e52-317dd58d7cd3.htm)   [See Also](#seeAlsoToggle) |

Checks if more stairs paths can be added on the plan views of a multistory stairs.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static bool CanCreateOnMultistoryStairs( 	Document document, 	LinkElementId multistoryStairsId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CanCreateOnMultistoryStairs ( _ 	document As Document, _ 	multistoryStairsId As LinkElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool CanCreateOnMultistoryStairs( 	Document^ document,  	LinkElementId^ multistoryStairsId ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

multistoryStairsId
:   Type:  [Autodesk.Revit.DB LinkElementId](6e18abde-8787-9906-8576-ab0c9c5432c6.htm)    
     The multistory stairs id.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[StairsPath Class](ed5913d6-1219-9c7c-7e52-317dd58d7cd3.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)