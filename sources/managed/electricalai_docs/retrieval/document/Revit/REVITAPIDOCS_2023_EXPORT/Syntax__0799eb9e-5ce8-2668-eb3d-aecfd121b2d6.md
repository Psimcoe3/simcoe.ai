[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetChangedElements Method

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Extracts a collection containing the ids of elements that have been created, modified or deleted between the input baseVersion and the document's current version.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public DocumentDifference GetChangedElements( 	Guid baseVersionGUID ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetChangedElements ( _ 	baseVersionGUID As Guid _ ) As DocumentDifference ``` |

 

| Visual C++ |
| --- |
| ``` public: DocumentDifference^ GetChangedElements( 	Guid baseVersionGUID ) ``` |

#### Parameters

baseVersionGUID
:   Type:  System Guid    
     GUID of base version(excluded) to compare. This GUID should be retrieved from property  [!:Autodesk::Revit::DB::DocumentVersion::VersoinGUID]  . Empty GUID is allowed to retrieve changes of each version in the document.

#### Return Value

An object containing collections of the created, modified and deleted ids between the input version and current version.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
private void ShowChangedElements(Autodesk.Revit.DB.Document document, Guid baseVerseionGuid)
{
    //Parameter baseVersionGuid is retrieved from property VersionGUID of Autodesk.Revit.DB.DocumentVersion.
    //System.Guid.Empty is allowed to get all changes in document.
    DocumentDifference docDiff = document.GetChangedElements(baseVerseionGuid);
    if (docDiff.AreDeletedElementIdsAvailable)
    {
        TaskDialog.Show("Revit", "Deleted element history is available in current document.");
    }
    else
    {
        TaskDialog.Show("Revit", "Deleted element history is not available in current document.");
    }

    // New added elements.
    var createdElementIds = docDiff.GetCreatedElementIds();

    // Modified elements.
    var modifiedElementIds = docDiff.GetModifiedElementIds();

    // Deleted elements.
    // For nonworkshared model, always returns an empty collection.
    var deletedElementIds = docDiff.GetDeletedElementIds();

    var changesetMessage = $"Found {createdElementIds.Count} new created elements, {modifiedElementIds.Count} modified elements and {deletedElementIds.Count} deleted elements.";
    TaskDialog.Show("Revit", changesetMessage);
}
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | This GUID is invalid in the given document. |

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)