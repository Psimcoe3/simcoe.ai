[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IExportContext Members

---



|  |
| --- |
| [IExportContext Interface](7d0dc6df-db0e-6a07-3b42-8dde1bedb3c1.htm)   [Methods](#methodTableToggle)   [See Also](#seeAlsoToggle) |

The  [IExportContext](7d0dc6df-db0e-6a07-3b42-8dde1bedb3c1.htm)  type exposes the following members.

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Finish](68714169-e994-41e3-f1c6-8f929b40565f.htm) | This method is called at the very end of the export process, after all entities were processed (or after the process was cancelled). |
| Public method | [IsCanceled](31f0b662-81a1-89b8-ab2a-0de99af3b753.htm) | This method is queried at the beginning of every element. |
| Public method | [OnElementBegin](d218b0b3-bb24-0f73-806c-2ef90b16d882.htm) | This method marks the beginning of an element to be exported. |
| Public method | [OnElementEnd](14aeeee7-9389-d7fc-5a40-2b7541ce95d1.htm) | This method marks the end of an element being exported. |
| Public method | [OnFaceBegin](9a9f37ae-c8c2-7355-2c3b-f26762951f1d.htm) | This method marks the beginning of a Face to be exported. |
| Public method | [OnFaceEnd](49e6eaf6-80e3-53bd-14c2-8fe999afb70b.htm) | This method marks the end of the current face being exported. |
| Public method | [OnInstanceBegin](2db35bdb-8d14-a015-9bfb-9283f503edab.htm) | This method marks the start of processing of an instance node (e.g. a family instance). |
| Public method | [OnInstanceEnd](d1340660-fcc9-3bfd-58fb-8d114aa39517.htm) | This method marks the end of processing of an Instance Node (e.g. a family instance). |
| Public method | [OnLight](d56129ca-950b-34fc-89ac-f0fb2e7fe9f2.htm) | This method marks the beginning of export of a light which is enabled for rendering. |
| Public method | [OnLinkBegin](40d99b4a-e6aa-42d7-18ff-b546d1a5154e.htm) | This method marks the beginning of a link instance to be exported. |
| Public method | [OnLinkEnd](e6680c8d-bfb3-f873-3e3d-24aa8b29061e.htm) | This method marks the end of a link instance being exported. |
| Public method | [OnMaterial](9d2dc6b3-21a7-5362-2bf5-2cb11b42c2d4.htm) | This method marks a change of the material. |
| Public method | [OnPolymesh](6a060c37-3225-217e-b150-2eaea3a22c29.htm) | This method is called when a tessellated polymesh of a 3d face is being output. |
| Public method | [OnRPC](f84574d9-ef15-c317-c6dd-91304a0c174c.htm) | This method marks the beginning of export of an RPC object. |
| Public method | [OnViewBegin](959602b7-5257-d2c1-2c00-0b7649f145f5.htm) | This method marks the beginning of a 3D view to be exported. |
| Public method | [OnViewEnd](5df27a2c-ae84-2d1d-635e-107ec0525ebb.htm) | This method marks the end of a 3D view being exported. |
| Public method | [Start](2d93c3c6-c826-cd70-dc0a-b94f66324c35.htm) | This method is called at the very start of the export process, still before the first entity of the model was send out. |

# See Also

[IExportContext Interface](7d0dc6df-db0e-6a07-3b42-8dde1bedb3c1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)