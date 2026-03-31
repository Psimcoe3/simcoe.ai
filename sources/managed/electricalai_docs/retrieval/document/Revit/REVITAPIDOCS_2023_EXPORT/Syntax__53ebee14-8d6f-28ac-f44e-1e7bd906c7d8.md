[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LightFamily Class

---



|  |
| --- |
| [Members](abedd83f-c9fd-ac11-12fe-0c3562489f21.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

This class encapsulates light family information.

**Namespace:**   [Autodesk.Revit.DB.Lighting](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public class LightFamily : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class LightFamily _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class LightFamily : IDisposable ``` |

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
public void GetLightDataInFamilyDocument(Document familyDoc)
{
    // LightFamily API should work only in light fixture family document.
    if (familyDoc.OwnerFamily.FamilyCategory.BuiltInCategory == BuiltInCategory.OST_LightingFixtures)
        return;

    // Get the light family from the static method.
    LightFamily lightFamily = LightFamily.GetLightFamily(familyDoc);

    // Get the light source shape style and distribution style
    LightShapeStyle shapeStyle = lightFamily.GetLightShapeStyle();
    LightDistributionStyle distributionStyle = lightFamily.GetLightDistributionStyle();

    // Get the light photometric for each family type
    for (int index = 0; index < lightFamily.GetNumberOfLightTypes(); index++)
    {
        string typeName = lightFamily.GetLightTypeName(index);  // the type name
        LightType lightData = lightFamily.GetLightType(index);  // the light data for each type
        // How to get and set data in LightType object, please read help document for LightType class.
    }
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Public Sub GetLightDataInFamilyDocument(familyDoc As Document)
   ' LightFamily API should work only in light fixture family document.
   If familyDoc.OwnerFamily.FamilyCategory.BuiltInCategory = BuiltInCategory.OST_LightingFixtures Then
      Return
   End If

   ' Get the light family from the static method.
   Dim lightFamily__1 As LightFamily = LightFamily.GetLightFamily(familyDoc)

   ' Get the light source shape style and distribution style
   Dim shapeStyle As LightShapeStyle = lightFamily__1.GetLightShapeStyle()
   Dim distributionStyle As LightDistributionStyle = lightFamily__1.GetLightDistributionStyle()

   ' Get the light photometric for each family type
   For index As Integer = 0 To lightFamily__1.GetNumberOfLightTypes() - 1
      Dim typeName As String = lightFamily__1.GetLightTypeName(index)
      ' the type name
      ' the light data for each type
      ' How to get and set data in LightType object, please read help document for LightType class.
      Dim lightData As LightType = lightFamily__1.GetLightType(index)
   Next
End Sub
```

# Inheritance Hierarchy

System Object    
  Autodesk.Revit.DB.Lighting LightFamily

# See Also

[LightFamily Members](abedd83f-c9fd-ac11-12fe-0c3562489f21.htm)

[Autodesk.Revit.DB.Lighting Namespace](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)