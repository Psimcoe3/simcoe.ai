[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateOnMultistoryStairs Method

---



|  |
| --- |
| [StairsPath Class](ed5913d6-1219-9c7c-7e52-317dd58d7cd3.htm)   [See Also](#seeAlsoToggle) |

Creates a new stairs path for the stairs in a multistory stairs with the specified stairs path type only in the plan view.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public static IList<StairsPath> CreateOnMultistoryStairs( 	Document document, 	LinkElementId multistoryStairsId, 	ElementId typeId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateOnMultistoryStairs ( _ 	document As Document, _ 	multistoryStairsId As LinkElementId, _ 	typeId As ElementId _ ) As IList(Of StairsPath) ``` |

 

| Visual C++ |
| --- |
| ``` public: static IList<StairsPath^>^ CreateOnMultistoryStairs( 	Document^ document,  	LinkElementId^ multistoryStairsId,  	ElementId^ typeId ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

multistoryStairsId
:   Type:  [Autodesk.Revit.DB LinkElementId](6e18abde-8787-9906-8576-ab0c9c5432c6.htm)    
     The id of the multistory stairs element either in the host document or in a linked document.

typeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The type of stairs path.

#### Return Value

The new stairs paths.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Cannot add more stairs paths on multistoryStairsId. -or- The typeId is not a valid stairs path type. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[StairsPath Class](ed5913d6-1219-9c7c-7e52-317dd58d7cd3.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)