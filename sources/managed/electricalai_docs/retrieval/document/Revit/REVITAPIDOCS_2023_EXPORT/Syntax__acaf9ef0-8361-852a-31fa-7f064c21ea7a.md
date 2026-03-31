[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### UseInTransparentPass Method

---



|  |
| --- |
| [IDirectContext3DServer Interface](7709521d-9954-ef80-1f13-3bc6ee660d5d.htm)   [See Also](#seeAlsoToggle) |

Indicates whether this server will submit geometry during the rendering pass for transparent geometry.

**Namespace:**   [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` bool UseInTransparentPass( 	View dBView ) ``` |

 

| Visual Basic |
| --- |
| ``` Function UseInTransparentPass ( _ 	dBView As View _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` bool UseInTransparentPass( 	View^ dBView ) ``` |

#### Parameters

dBView
:   Type:  [Autodesk.Revit.DB View](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)    
     The view where rendering will occur.

#### Return Value

True if the server needs to render transparent geometry, false otherwise.

# Remarks

Transparent geometry is rendered in a separate pass following the opaque geometry. If a server returns true from UseInTransparentPass(), it can provide geometry for rendering in either pass using the RenderScene() method. Otherwise, the server will be called to submit only opaque geometry.

The server has a way to determine whether it should submit opaque or transparent geometry when RenderScene() is called (see Autodesk::Revit::DB::DirectContext3D::DrawContext::IsTransparentPass(void)).

# See Also

[IDirectContext3DServer Interface](7709521d-9954-ef80-1f13-3bc6ee660d5d.htm)

[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.htm)