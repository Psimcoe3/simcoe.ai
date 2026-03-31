[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IRebarUpdateServer Members

---



|  |
| --- |
| [IRebarUpdateServer Interface](3e845cad-eca0-ccb3-785b-48a32a9f2677.htm)   [Methods](#methodTableToggle)   [See Also](#seeAlsoToggle) |

The  [IRebarUpdateServer](3e845cad-eca0-ccb3-785b-48a32a9f2677.htm)  type exposes the following members.

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [GenerateCurves](2b83cc23-076c-1843-f078-46d0c1f2dc74.htm) | This function is supposed to calculate the bars in set based on data received in curvesData parameter. |
| Public method | [GetCustomHandleName](7f072a66-48c3-43d1-5d3e-a8a5ae787477.htm) | This function should return the name of the handle. |
| Public method | [GetCustomHandles](37833063-e74a-26bb-bdf8-9700f7a446cb.htm) | This function should define all handles that the Rebar has. This function is called when the Rebar is created. |
| Public method | [GetDescription](ab8f162b-c7af-dafc-04f6-8cb3835caa13.htm) | Implement this method to return a description of the server. (Inherited from  [IExternalServer](91e4af0b-59c0-d640-107a-eebc4d99fa76.htm)  .) |
| Public method | [GetHandlesPosition](7f991fe0-6c77-ba43-3d52-64a8c0390809.htm) | This function is supposed to provide the positions of handles defined in GetCustomHandles(). These positions will be shown on screen when the bar constraints are edited. If a position for a handle isn't provided, that handle will not be represented on screen while edit constraints.  This function is called when edit constraints command is lunched or during edit constraints after a constraint was changed and the curve calculation was done. |
| Public method | [GetName](df64b529-27e1-3a6a-7876-2145bb8a37b4.htm) | Implement this method to return the name of the server. (Inherited from  [IExternalServer](91e4af0b-59c0-d640-107a-eebc4d99fa76.htm)  .) |
| Public method | [GetServerId](49b1955b-a729-b610-0138-592784d20171.htm) | Implement this method to return the id of the server. (Inherited from  [IExternalServer](91e4af0b-59c0-d640-107a-eebc4d99fa76.htm)  .) |
| Public method | [GetServiceId](1f8da2c8-54d9-2d69-bdcc-e801d990d463.htm) | Implement this method to return the id of the service. (Inherited from  [IExternalServer](91e4af0b-59c0-d640-107a-eebc4d99fa76.htm)  .) |
| Public method | [GetVendorId](76cf499a-4a59-9249-8995-e1ab9e629f37.htm) | Implement this method to return the id of the vendor of the server. (Inherited from  [IExternalServer](91e4af0b-59c0-d640-107a-eebc4d99fa76.htm)  .) |
| Public method | [TrimExtendCurves](6db89b01-28aa-8b95-f3c0-a0f00cdb84c5.htm) | This function is supposed to trim or extend curves that were obtained from calling GenerateCurves(). Also in this function can be set new constraints for start and end handles. |

# See Also

[IRebarUpdateServer Interface](3e845cad-eca0-ccb3-785b-48a32a9f2677.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)