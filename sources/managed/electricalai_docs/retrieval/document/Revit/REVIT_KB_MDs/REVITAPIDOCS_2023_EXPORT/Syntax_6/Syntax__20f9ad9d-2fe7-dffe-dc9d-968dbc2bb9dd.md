[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetStructuralAsset Method

---



|  |
| --- |
| [PropertySetElement Class](dd2c8fbb-98ec-7249-87f0-542401f490dd.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Gets a copy of the StructuralAsset.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public StructuralAsset GetStructuralAsset() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetStructuralAsset As StructuralAsset ``` |

 

| Visual C++ |
| --- |
| ``` public: StructuralAsset^ GetStructuralAsset() ``` |

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
private void ReadMaterialProps(Document document, Material material)
{
   ElementId strucAssetId = material.StructuralAssetId;
   if (strucAssetId != ElementId.InvalidElementId)
   {
      PropertySetElement pse = document.GetElement(strucAssetId) as PropertySetElement;
      if (pse != null)
      {
         StructuralAsset asset = pse.GetStructuralAsset();

         // Check the material behavior and only read if Isotropic
         if (asset.Behavior == StructuralBehavior.Isotropic)
         {
            // Get the class of material
            StructuralAssetClass assetClass = asset.StructuralAssetClass;

            // Get other material properties
            double poisson = asset.PoissonRatio.X;
            double youngMod = asset.YoungModulus.X;
            double thermCoeff = asset.ThermalExpansionCoefficient.X;
            double unitweight = asset.Density;
            double shearMod = asset.ShearModulus.X;

            if (assetClass == StructuralAssetClass.Metal)
            {
               double dMinStress = asset.MinimumYieldStress;
            }
            else if (assetClass == StructuralAssetClass.Concrete)
            {
               double dConcComp = asset.ConcreteCompression;
            }
         }
      }
   }
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Sub ReadMaterialProps(document As Document, material As Material)
    Dim strucAssetId As ElementId = material.StructuralAssetId
    If strucAssetId <> ElementId.InvalidElementId Then
        Dim pse As PropertySetElement = TryCast(document.GetElement(strucAssetId), PropertySetElement)
        If pse IsNot Nothing Then
            Dim asset As StructuralAsset = pse.GetStructuralAsset()

            ' Check the material behavior and only read if Isotropic
            If asset.Behavior = StructuralBehavior.Isotropic Then
                ' Get the class of material
                Dim assetClass As StructuralAssetClass = asset.StructuralAssetClass

                ' Get other material properties
                Dim poisson As Double = asset.PoissonRatio.X
                Dim youngMod As Double = asset.YoungModulus.X
                Dim thermCoeff As Double = asset.ThermalExpansionCoefficient.X
                Dim unitweight As Double = asset.Density
                Dim shearMod As Double = asset.ShearModulus.X

                If assetClass = StructuralAssetClass.Metal Then
                    Dim dMinStress As Double = asset.MinimumYieldStress
                ElseIf assetClass = StructuralAssetClass.Concrete Then
                    Dim dConcComp As Double = asset.ConcreteCompression
                End If
            End If
        End If
    End If
End Sub
```

# See Also

[PropertySetElement Class](dd2c8fbb-98ec-7249-87f0-542401f490dd.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)