[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### EditFamily Method

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Gets the document of a loaded family to edit.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public Document EditFamily( 	Family loadedFamily ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function EditFamily ( _ 	loadedFamily As Family _ ) As Document ``` |

 

| Visual C++ |
| --- |
| ``` public: Document^ EditFamily( 	Family^ loadedFamily ) ``` |

#### Parameters

loadedFamily
:   Type:  [Autodesk.Revit.DB Family](f51d019d-6ff3-692b-d1d2-b497cab564de.htm)    
     The loaded family in current document.

#### Return Value

Reference of the document of the family.

# Remarks

This creates an independent copy of the family for editing. To apply the changes back to the family stored in the document, use the LoadFamily overload accepting  [IFamilyLoadOptions](d447ed92-74e1-2125-dd0a-38a5ae85ce53.htm)  .

This method may not be called if the document is currently modifiable (has an open transaction) or is in a read-only state. The method may not be called during dynamic updates. To test the document's current status, check the values of IsModifiable and IsReadOnly properties.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
public void GetLoadedSymbols(Autodesk.Revit.DB.Document document, FamilyInstance familyInstance)
{
    if (null != familyInstance.Symbol)
    {
        // Get family associated with this
        Family family = familyInstance.Symbol.Family;

        // Get Family document for family
        Document familyDoc = document.EditFamily(family);
        if (null != familyDoc && familyDoc.IsFamilyDocument == true)
        {
            String loadedFamilies = "FamilySymbols in " + family.Name + ":\n";
            FilteredElementCollector collector = new FilteredElementCollector(document);
            ICollection<Element> collection = 
                collector.OfClass(typeof(FamilySymbol)).ToElements();
            foreach (Element e in collection)
            {
                FamilySymbol fs = e as FamilySymbol;
                loadedFamilies += "\t" + fs.Name + "\n";
            }

            TaskDialog.Show("Revit",loadedFamilies);
        }
    }
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Public Sub GetLoadedSymbols(document As Autodesk.Revit.DB.Document, familyInstance As FamilyInstance)
    If familyInstance.Symbol IsNot Nothing Then
        ' Get family associated with this
        Dim family As Family = familyInstance.Symbol.Family

        ' Get Family document for family
        Dim familyDoc As Document = document.EditFamily(family)
        If familyDoc IsNot Nothing AndAlso familyDoc.IsFamilyDocument = True Then
            Dim loadedFamilies As [String] = "FamilySymbols in " + family.Name & ":" & vbLf
            Dim collector As New FilteredElementCollector(document)
            Dim collection As ICollection(Of Element) = collector.OfClass(GetType(FamilySymbol)).ToElements()
            For Each e As Element In collection
                Dim fs As FamilySymbol = TryCast(e, FamilySymbol)
                loadedFamilies += vbTab + fs.Name & vbLf
            Next

            TaskDialog.Show("Revit", loadedFamilies)
        End If
    End If
End Sub
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the input argument-"loadedFamily"-is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when the input argument-"loadedFamily"-is an in-place family or a non-editable family. (This can be checked with the IsInPlace and IsEditable properties of the Family class. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when the family is already being edited. |
| [Autodesk.Revit.Exceptions ForbiddenForDynamicUpdateException](c5b911f6-1e8f-2cd4-6965-286f41221fe0.htm) | Thrown if this method is called during dynamic update. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown if this method is called while the document is modifiable (i.e. it has an unfinished transaction.) |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown if this method is currently in a read-only state. |

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)