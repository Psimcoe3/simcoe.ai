[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FamilySymbol Class

---



|  |
| --- |
| [Members](33042823-a11d-19d4-0d39-f1a4869284a3.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

An element that represents a single type with a Family.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class FamilySymbol : InsertableObject ``` |

 

| Visual Basic |
| --- |
| ``` Public Class FamilySymbol _ 	Inherits InsertableObject ``` |

 

| Visual C++ |
| --- |
| ``` public ref class FamilySymbol : public InsertableObject ``` |

# Remarks

Custom families within the Revit API represented by three objects - Family,  FamilySymbol  and  [FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.htm)  . Each object plays a significant part in the structure of families. The Family element represents the entire family that consists of a collection of types, such as an 'I Beam'. You can think of that object as representing the entire family file. The Family object contains a number of  FamilySymbol  elements. The  FamilySymbol  object represents a specific set of family settings within that Family and represents what is known in the Revit user interface as a Type, such as 'W14x32'. The  [FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.htm)  object represents an actual instance of that type placed the Autodesk Revit project. For example the  [FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.htm)  would be a single instance of a W14x32 column within the project.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
public void GetInfo_FamilySymbol(FamilySymbol familySymbol)
{
    string message;
    // Get FamilySymbol family name
    message = "Family name is : " + familySymbol.Family.Name;

    // Get FamilySymbol material
    message += "\nFamilySymbol materials are :";
    foreach (ElementId matid in familySymbol.GetMaterialIds(true))
    {
       Material material = familySymbol.Document.GetElement(matid) as Material;
       if (null != material)
       {
          message += "\n" + material.Name;
       }
    }

    TaskDialog.Show("Revit",message);
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Public Sub GetInfo_FamilySymbol(familySymbol As FamilySymbol)
    Dim message As String
    ' Get FamilySymbol family name
    message = "Family name is : " & Convert.ToString(familySymbol.Family.Name)

    ' Get FamilySymbol material
    message += vbLf & "FamilySymbol materials are :"
    For Each matid As ElementId In familySymbol.GetMaterialIds(True)
        Dim material As Material = TryCast(familySymbol.Document.GetElement(matid), Material)
        If material IsNot Nothing Then
            message += vbLf + material.Name
        End If
    Next

    TaskDialog.Show("Revit", message)
End Sub
```

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  [Autodesk.Revit.DB ElementType](ffb18296-0448-559c-580c-7857cbcdc094.htm)    
  [Autodesk.Revit.DB InsertableObject](73d870e0-a408-719c-58bd-1fb2ab8f9e5b.htm)    
  Autodesk.Revit.DB FamilySymbol    
  [Autodesk.Revit.DB AnnotationSymbolType](a8a53b66-bf87-7441-bf02-497d39fd011a.htm)    
  [Autodesk.Revit.DB.Architecture RoomTagType](69ece493-bfac-d3c5-8a80-b99081ed0733.htm)    
  [Autodesk.Revit.DB AreaTagType](78bd4d11-0ccd-9065-c316-7225f422fa16.htm)    
  [Autodesk.Revit.DB.Mechanical SpaceTagType](7d4d4ab0-a336-f832-3b95-a845a22c4596.htm)    
  [Autodesk.Revit.DB MullionType](d54e677d-9ec1-d218-2e26-796774f65369.htm)    
  [Autodesk.Revit.DB PanelType](3a8ad72e-5aa7-8fef-10ba-72041fe47346.htm)    
  [Autodesk.Revit.DB.Structure TrussType](6c8c06d7-14a0-a286-8c15-7391d67579a5.htm)

# See Also

[FamilySymbol Members](33042823-a11d-19d4-0d39-f1a4869284a3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)