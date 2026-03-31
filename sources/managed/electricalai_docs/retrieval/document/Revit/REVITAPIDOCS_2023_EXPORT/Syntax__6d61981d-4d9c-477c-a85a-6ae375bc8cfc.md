[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetFolderItems Method

---



|  |
| --- |
| [BrowserOrganization Class](4fd57c3f-6127-efd9-f79e-70ad3e5dc1cc.htm)   [See Also](#seeAlsoToggle) |

Returns a collection of leaf  [FolderItemInfo](ef79812e-ea11-eda4-9c51-b54df57dc197.htm)  objects each containing the given element Id.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public IList<FolderItemInfo> GetFolderItems( 	ElementId elementId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetFolderItems ( _ 	elementId As ElementId _ ) As IList(Of FolderItemInfo) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<FolderItemInfo^>^ GetFolderItems( 	ElementId^ elementId ) ``` |

#### Parameters

elementId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Element id located at a leaf position in the project browser.

#### Return Value

An array of FolderItemInfo objects.

# Remarks

Each returned  [FolderItemInfo](ef79812e-ea11-eda4-9c51-b54df57dc197.htm)  includes the folder name and the corresponding folder parameter Id.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | elementId is not a valid Element identifier. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[BrowserOrganization Class](4fd57c3f-6127-efd9-f79e-70ad3e5dc1cc.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)