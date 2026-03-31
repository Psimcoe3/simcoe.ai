[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Family Class

---



|  |
| --- |
| [Members](f3615aef-5a80-26d7-fe0d-18fc4285a277.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

An element that represents a custom family (not a system family) in Autodesk Revit.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class Family : Element ``` |

 

| Visual Basic |
| --- |
| ``` Public Class Family _ 	Inherits Element ``` |

 

| Visual C++ |
| --- |
| ``` public ref class Family : public Element ``` |

# Remarks

Custom families within the Revit API represented by three objects - Family,  [FamilySymbol](a1acaed0-6a62-4c1d-94f5-4e27ce0923d3.htm)  and  [FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.htm)  . Each object plays a significant part in the structure of families. The Family element represents the entire family that consists of a collection of types, such as an 'I Beam'. You can think of that object as representing the entire family file. The Family object contains a number of  [FamilySymbol](a1acaed0-6a62-4c1d-94f5-4e27ce0923d3.htm)  elements. The  [FamilySymbol](a1acaed0-6a62-4c1d-94f5-4e27ce0923d3.htm)  object represents a specific set of family settings within that Family and represents what is known in the Revit user interface as a Type, such as 'W14x32'. The  [FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.htm)  object represents an actual instance of that type placed the Autodesk Revit project. For example the  [FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.htm)  would be a single instance of a W14x32 column within the project.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
public void GetInfoForSymbols(Family family)
{
    StringBuilder message = new StringBuilder("Selected element's family name is : " + family.Name);
    ISet<ElementId> familySymbolIds = family.GetFamilySymbolIds();

    if (familySymbolIds.Count == 0)
    {
        message.AppendLine("Contains no family symbols.");
    }
    else
    {
        message.AppendLine("The family symbols contained in this family are : ");

        // Get family symbols which is contained in this family
        foreach (ElementId id in familySymbolIds)
        {
            FamilySymbol familySymbol = family.Document.GetElement(id) as FamilySymbol;
            // Get family symbol name
            message.AppendLine("\nName: " + familySymbol.Name);
            foreach (ElementId materialId in familySymbol.GetMaterialIds(false))
            {
                Material material = familySymbol.Document.GetElement(materialId) as Material;
                message.AppendLine("\nMaterial : " + material.Name);
            }
        }
    }

    TaskDialog.Show("Revit",message.ToString());
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Public Sub GetInfoForSymbols(family As Family)
    Dim message As New StringBuilder("Selected element's family name is : " & Convert.ToString(family.Name))
    Dim familySymbolIds As ISet(Of ElementId) = family.GetFamilySymbolIds()

    If familySymbolIds.Count = 0 Then
        message.AppendLine("Contains no family symbols.")
    Else
        message.AppendLine("The family symbols contained in this family are : ")

        ' Get family symbols which is contained in this family
        For Each id As ElementId In familySymbolIds
            Dim familySymbol As FamilySymbol = TryCast(family.Document.GetElement(id), FamilySymbol)
            ' Get family symbol name
            message.AppendLine(vbLf & "Name: " + familySymbol.Name)
            For Each materialId As ElementId In familySymbol.GetMaterialIds(False)
                Dim material As Material = TryCast(familySymbol.Document.GetElement(materialId), Material)
                message.AppendLine(vbLf & "Material : " + material.Name)
            Next
        Next
    End If

    TaskDialog.Show("Revit", message.ToString())
End Sub
```

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  Autodesk.Revit.DB Family

# See Also

[Family Members](f3615aef-5a80-26d7-fe0d-18fc4285a277.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)