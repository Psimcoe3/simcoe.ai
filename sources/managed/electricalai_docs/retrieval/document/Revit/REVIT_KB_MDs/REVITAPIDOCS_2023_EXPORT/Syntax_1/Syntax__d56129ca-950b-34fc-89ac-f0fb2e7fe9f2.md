[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OnLight Method

---



|  |
| --- |
| [IExportContext Interface](7d0dc6df-db0e-6a07-3b42-8dde1bedb3c1.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

This method marks the beginning of export of a light which is enabled for rendering.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` void OnLight( 	LightNode node ) ``` |

 

| Visual Basic |
| --- |
| ``` Sub OnLight ( _ 	node As LightNode _ ) ``` |

 

| Visual C++ |
| --- |
| ``` void OnLight( 	LightNode^ node ) ``` |

#### Parameters

node
:   Type:  [Autodesk.Revit.DB LightNode](3904e399-f67a-a111-d963-5f91665b233c.htm)    
     A node describing the light object.

# Remarks

This method is only called for photo-rendering export (a custom exporter that implements  [IPhotoRenderContext](d09d4ea2-1090-f2b9-8073-5fb8a796babf.htm)  ).

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
/// <summary>
/// This method is called for instances of lights
/// </summary>
/// <remarks>
/// The Light API can be used to get more information about each particular light
/// </remarks>
public void OnLight(LightNode node)
{
   // Obtain local transform data of the light object.
   Transform lightTrf = node.GetTransform();

   // Note: 1. If your light coordinate system differs from the one in REvit, 
   //   The light's local transform should be adjusted to reflect the difference.

   // Note 2. This local transform describes the light source position and light direction data.
   //   It means the "TiltAngle" property of a spot light has already been accounted for.

   // If a stack of transformation is maintained by the context object,
   // the current combined transform will be multiplied by the local transform.
   Transform lightWorldTrf = m_TransformationStack.Peek().Multiply(lightTrf);

}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
' <summary>
' This method is called for instances of lights
' </summary>
' <remarks>
' The Light API can be used to get more information about each particular light
' </remarks>
Public Sub OnLight(node As LightNode) Implements IExportContext.OnLight
    ' Obtain local transform data of the light object.
    Dim lightTrf As Transform = node.GetTransform()

    ' Note: 1. If your light coordinate system differs from the one in REvit, 
    '   The light's local transform should be adjusted to reflect the difference.


    ' Note 2. This local transform describes the light source position and light direction data.
    '   It means the "TiltAngle" property of a spot light has already been accounted for.


    ' If a stack of transformation is maintained by the context object,
    ' the current combined transform will be multiplied by the local transform.
    Dim lightWorldTrf As Transform = m_TransformationStack.Peek().Multiply(lightTrf)

End Sub
```

# See Also

[IExportContext Interface](7d0dc6df-db0e-6a07-3b42-8dde1bedb3c1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)