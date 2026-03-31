[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DrawContext Members

---



|  |
| --- |
| [DrawContext Class](b9244325-08c8-8bbd-a9f3-5d91d638d85d.htm)   [Methods](#methodTableToggle)   [See Also](#seeAlsoToggle) |

The  [DrawContext](b9244325-08c8-8bbd-a9f3-5d91d638d85d.htm)  type exposes the following members.

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method Static member | [FlushBuffer](e216a4c0-6a88-cf2c-35fa-8f43019db61d.htm) | Submits geometry for rendering. |
| Public method Static member | [GetCamera](048d5376-17c1-8581-9e2a-376a0bc20215.htm) | Gets the camera corresponding to the Revit view where rendering takes place. |
| Public method Static member | [GetClipPlanes](be439140-6dd8-f08e-de56-484f576de94f.htm) | Gets the clipping planes for the Revit view where rendering takes place. Clipping planes control the 3D extent of a view and can be set using Section Box in Revit. |
| Public method Static member | [GetClipRectangle](3befe4ef-682b-f101-c6a6-e54aa15adf04.htm) | Gets the clip rectangle for the Revit view where rendering takes place. The clip rectangle is the area currently being redrawn, which may be smaller than the view rectangle. |
| Public method Static member | [GetOverrideColor](4e25065e-24ec-4378-6c17-79530d93881a.htm) | Returns override color that will be applied to geometry during rendering. |
| Public method Static member | [GetOverrideTransparency](bded077c-4190-fddb-ec44-558a55baec01.htm) | Returns override transparency that will be applied to geometry during rendering. |
| Public method Static member | [GetViewRectangle](7ea41cc8-bf1c-d9f0-5013-8e73ff0a0bbe.htm) | Gets the rectangle that represents the extent (in 2D) of the Revit view where rendering takes place. |
| Public method Static member | [IsAvailable](7282d58a-ba94-79d1-dff1-7782ecdacf84.htm) | Checks whether the facilities of this class are available for use in the current scope. |
| Public method Static member | [IsInterrupted](7e0eb9bd-9a96-a142-5503-1a266cbafb2a.htm) | Checks whether the current rendering pass has been interrupted. |
| Public method Static member | [IsTransparentPass](e7a6cb5b-d23b-9269-591d-6ca37790176d.htm) | Determines whether the current rendering pass is for transparent objects. |
| Public method Static member | [SetWorldTransform](4917c16f-5f9e-6172-7b5d-32d6174d6adf.htm) | Sets the world transformation that will be applied to geometry during rendering. |

# See Also

[DrawContext Class](b9244325-08c8-8bbd-a9f3-5d91d638d85d.htm)

[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.htm)