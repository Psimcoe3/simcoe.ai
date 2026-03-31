[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetInitialIntensity Method

---



|  |
| --- |
| [LightType Class](42c83d85-60cd-52c3-7b97-b89e81d7d9fe.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Replace the current initial intensity object with the given object

**Namespace:**   [Autodesk.Revit.DB.Lighting](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public void SetInitialIntensity( 	InitialIntensity initialIntensity ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetInitialIntensity ( _ 	initialIntensity As InitialIntensity _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetInitialIntensity( 	InitialIntensity^ initialIntensity ) ``` |

#### Parameters

initialIntensity
:   Type:  [Autodesk.Revit.DB.Lighting InitialIntensity](557d9e25-430a-2f92-3dbc-c9ec84e07900.htm)    
     An object derived from an InitialIntensity object

# Remarks

The argument object is cloned

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
public void SetInitialIntensityProperty(LightType lightType)
{
    InitialIntensity initialIntensity = lightType.GetInitialIntensity();
    if (initialIntensity is InitialFluxIntensity)
    {
        InitialFluxIntensity fluxIntensity = initialIntensity as InitialFluxIntensity;
        double fluxValue = fluxIntensity.Flux;

        // Set new value for Flux proeprty and set modified InitialIntensity to LightType.
        fluxIntensity.Flux = 34.50;
        lightType.SetInitialIntensity(fluxIntensity);

        // Create a InitialWattageIntensity and set it to LightType.
        InitialWattageIntensity wattageIntensity = new InitialWattageIntensity(25.57, 130.89);
        lightType.SetInitialIntensity(wattageIntensity);
    }
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Public Sub SetInitialIntensityProperty(lightType As LightType)
   Dim initialIntensity As InitialIntensity = lightType.GetInitialIntensity()
   If TypeOf initialIntensity Is InitialFluxIntensity Then
      Dim fluxIntensity As InitialFluxIntensity = TryCast(initialIntensity, InitialFluxIntensity)
      Dim fluxValue As Double = fluxIntensity.Flux

      ' Set new value for Flux proeprty and set modified InitialIntensity to LightType.
      fluxIntensity.Flux = 34.5
      lightType.SetInitialIntensity(fluxIntensity)

      ' Create a InitialWattageIntensity and set it to LightType.
      Dim wattageIntensity As New InitialWattageIntensity(25.57, 130.89)
      lightType.SetInitialIntensity(wattageIntensity)
   End If
End Sub
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[LightType Class](42c83d85-60cd-52c3-7b97-b89e81d7d9fe.htm)

[Autodesk.Revit.DB.Lighting Namespace](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)