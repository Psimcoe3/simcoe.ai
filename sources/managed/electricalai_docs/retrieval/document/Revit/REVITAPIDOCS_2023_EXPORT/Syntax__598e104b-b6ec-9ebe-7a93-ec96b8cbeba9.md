[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Asset Class

---



|  |
| --- |
| [Members](a4771475-8e1c-3a28-c7f4-49a19df4e2d1.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Represents a connected property of material.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)

# Syntax

| C# |
| --- |
| ``` public class Asset : AssetProperties ``` |

 

| Visual Basic |
| --- |
| ``` Public Class Asset _ 	Inherits AssetProperties ``` |

 

| Visual C++ |
| --- |
| ``` public ref class Asset : public AssetProperties ``` |

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
public void ReadAsset(Asset asset)
{
   // Get the asset name, type and library name.
   AssetType type = asset.AssetType;
   string name = asset.Name;
   string libraryName = asset.LibraryName;

   // travel the asset properties in the asset.
   for (int idx = 0; idx < asset.Size; idx++)
   {
      AssetProperty prop = asset.Get(idx);
      ReadAssetProperty(prop);
   }
}

public void ReadAssetProperty(AssetProperty prop)
{
   switch (prop.Type)
   {
      // Retrieve the value from simple type property is easy.
      // for example, retrieve bool property value.
      case AssetPropertyType.Boolean:
         AssetPropertyBoolean boolProp = prop as AssetPropertyBoolean;
         bool propValue = boolProp.Value;
         break;

      // When you retrieve the value from the data array property,
      // you may need to get which value the property stands for.
      // for example, the APT_Double44 may be a transform data.
      case AssetPropertyType.Double44:
         AssetPropertyDoubleArray4d transformProp = prop as AssetPropertyDoubleArray4d;
         IList<double> tranformValue = transformProp.GetValueAsDoubles();
         break;

      // The APT_List contains a list of sub asset properties with same type.
      case AssetPropertyType.List:
         AssetPropertyList propList = prop as AssetPropertyList;
         IList<AssetProperty> subProps = propList.GetValue();
         if (subProps.Count == 0)
            break;
         switch (subProps[0].Type)
         {
            case AssetPropertyType.Integer:
               foreach (AssetProperty subProp in subProps)
               {
                  AssetPropertyInteger intProp = subProp as AssetPropertyInteger;
                  int intValue = intProp.Value;
               }
               break;
         }
         break;

      case AssetPropertyType.Asset:
         Asset propAsset = prop as Asset;
         ReadAsset(propAsset);
         break;
      default:
         break;
   }

   // Get the connected properties.
   // please notice that the information of many texture stores here.
   if (prop.NumberOfConnectedProperties == 0)
      return;
   foreach (AssetProperty connectedProp in prop.GetAllConnectedProperties())
   {
      // Note: Usually, the connected property is an Asset.
      ReadAssetProperty(connectedProp);
   }
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Public Sub ReadAsset(asset As Asset)
    ' Get the asset name, type and library name.
    Dim type As AssetType = asset.AssetType
    Dim name As String = asset.Name
    Dim libraryName As String = asset.LibraryName

    ' travel the asset properties in the asset.
    For idx As Integer = 0 To asset.Size - 1
    Dim prop As AssetProperty = asset.Get(idx)
    ReadAssetProperty(prop)
    Next
End Sub

Public Sub ReadAssetProperty(prop As AssetProperty)
    Select Case prop.Type
        ' Retrieve the value from simple type property is easy.
        ' for example, retrieve bool property value.
    Case AssetPropertyType.Boolean
       Dim boolProp As AssetPropertyBoolean = TryCast(prop, AssetPropertyBoolean)
       Dim propValue As Boolean = boolProp.Value
       Exit Select

            ' When you retrieve the value from the data array property,
            ' you may need to get which value the property stands for.
            ' for example, the APT_Double44 may be a transform data.
    Case AssetPropertyType.Double44
       Dim transformProp As AssetPropertyDoubleArray4d = TryCast(prop, AssetPropertyDoubleArray4d)
       Dim tranformValue As IList(Of Double) = transformProp.GetValueAsDoubles()
       Exit Select

            ' The APT_List contains a list of sub asset properties with same type.
    Case AssetPropertyType.List
       Dim propList As AssetPropertyList = TryCast(prop, AssetPropertyList)
       Dim subProps As IList(Of AssetProperty) = propList.GetValue()
       If subProps.Count = 0 Then
          Exit Select
       End If
       Select Case subProps(0).Type
          Case AssetPropertyType.Integer
             For Each subProp As AssetProperty In subProps
                Dim intProp As AssetPropertyInteger = TryCast(subProp, AssetPropertyInteger)
                Dim intValue As Integer = intProp.Value
             Next
             Exit Select
       End Select
       Exit Select

    Case AssetPropertyType.Asset
       Dim propAsset As Asset = TryCast(prop, Asset)
            ReadAsset(propAsset)
            Exit Select
        Case Else
            Exit Select
    End Select

    ' Get the connected properties.
    ' please notice that the information of many texture stores here.
    If prop.NumberOfConnectedProperties = 0 Then
        Return
    End If
    For Each connectedProp As AssetProperty In prop.GetAllConnectedProperties()
        ' Note: Usually, the connected property is an Asset.
        ReadAssetProperty(connectedProp)
    Next
End Sub
```

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB.Visual AssetProperty](7be89499-d011-ab43-4715-0ee6f9335970.htm)    
  [Autodesk.Revit.DB.Visual AssetProperties](45955e9d-7dd4-b06c-f71a-f9ae2cc1c34a.htm)    
  Autodesk.Revit.DB.Visual Asset

# See Also

[Asset Members](a4771475-8e1c-3a28-c7f4-49a19df4e2d1.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)