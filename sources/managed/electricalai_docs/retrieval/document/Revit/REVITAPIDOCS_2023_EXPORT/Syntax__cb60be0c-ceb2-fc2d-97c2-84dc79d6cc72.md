[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetSelectedElementIds Method

---



|  |
| --- |
| [NavisworksExportOptions Class](a58dbe71-1be7-dad6-51b6-5386c162cf87.htm)   [See Also](#seeAlsoToggle) |

Sets the element ids of the elements to export. Used only when ExportScope = SelectedElements.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public void SetSelectedElementIds( 	ICollection<ElementId> ids ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetSelectedElementIds ( _ 	ids As ICollection(Of ElementId) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetSelectedElementIds( 	ICollection<ElementId^>^ ids ) ``` |

#### Parameters

ids
:   Type:  System.Collections.Generic ICollection   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[NavisworksExportOptions Class](a58dbe71-1be7-dad6-51b6-5386c162cf87.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)