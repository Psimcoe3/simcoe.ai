[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ConvertToRealSheet Method

---



|  |
| --- |
| [ViewSheet Class](af2ee879-173d-df3a-9793-8d5750a17b49.htm)   [See Also](#seeAlsoToggle) |

Converts a placeholder sheet to a real one with an optional titleblock.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public void ConvertToRealSheet( 	ElementId titleBlockTypeId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub ConvertToRealSheet ( _ 	titleBlockTypeId As ElementId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void ConvertToRealSheet( 	ElementId^ titleBlockTypeId ) ``` |

#### Parameters

titleBlockTypeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of the placeholder sheet, or invalidElementId if no titleblock should be added.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | titleBlockTypeId does not correspond to a TitleBlock type. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This method may only be called on a placeholder sheet. -or- Failed to convert the sheet because the input titleblock could not be applied. |

# See Also

[ViewSheet Class](af2ee879-173d-df3a-9793-8d5750a17b49.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)