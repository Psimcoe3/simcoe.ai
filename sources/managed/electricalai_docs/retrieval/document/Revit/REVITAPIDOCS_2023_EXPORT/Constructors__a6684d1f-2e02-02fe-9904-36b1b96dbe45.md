[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CustomExporter Members

---



|  |
| --- |
| [CustomExporter Class](d2437433-9183-cbb1-1c67-dedd86db5b5a.htm)   [Constructors](#constructorTableToggle)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [CustomExporter](d2437433-9183-cbb1-1c67-dedd86db5b5a.htm)  type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [CustomExporter](98f23174-e29e-36a5-e3a4-c72144708553.htm) | Constructs a new instance of a CustomExporter for a given document using the input instance of IExportContext as the output device. |

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Dispose](2a3e9fca-a6a5-f0a4-4ebf-aeea322333ce.htm) | Releases all resources used by the  [CustomExporter](d2437433-9183-cbb1-1c67-dedd86db5b5a.htm) |
| Public method | Equals | Determines whether the specified  Object  is equal to the current  Object  . (Inherited from  Object  .) |
| Public method | [Export(IList ElementId )](58d06458-fd6a-bdef-c457-2c52b50a70e8.htm) | Exports a collection of 3D or 2D views |
| Public method | [Export(View)](5a648f8c-62a0-d4c7-873c-8eab9f7abe7d.htm) | Exports one 3D or 2D view |
| Public method | GetHashCode | Serves as a hash function for a particular type. (Inherited from  Object  .) |
| Public method | GetType | Gets the  Type  of the current instance. (Inherited from  Object  .) |
| Public method Static member | [IsRenderingSupported](50882930-42d7-5d6c-f70c-c5f665b22900.htm) | Checks if view rendering is currently supported in the running instance of Revit. |
| Public method | ToString | Returns a string that represents the current object. (Inherited from  Object  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Export2DForceDisplayStyle](47ed429b-289a-207d-0176-707158a46df0.htm) | This value tells the exporter of 2D views to force the given display mode for the view. |
| Public property | [Export2DGeometricObjectsIncludingPatternLines](34ed2a39-a5e6-6ef1-1f6d-cceebd2bae7f.htm) | This flag sets the exporter of 2D views to either include or exclude output of face pattern lines as part of geometric objects when the model is being processed by the export context. |
| Public property | [Export2DIncludingAnnotationObjects](1a22bfd6-bb08-c368-f981-d02151986b5c.htm) | This flag sets the exporter of 2D views to either include or exclude output of annotation objects when the model is being processed by the export context. |
| Public property | [IncludeGeometricObjects](2ce1075e-380e-01e7-6459-b7467c2a2414.htm) | This flag sets the exporter to either include or exclude output of geometric objects such as faces and curves when the model is being processed by the export context. |
| Public property | [IsValidObject](6686c741-6cac-5940-4297-52c49a8234c9.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| Public property | [ShouldStopOnError](bc21fee5-c194-4d19-cd12-0a285e854a5e.htm) | This flag instructs the exporting process to either stop or continue in case an error occurs during any of the exporting methods. |

# See Also

[CustomExporter Class](d2437433-9183-cbb1-1c67-dedd86db5b5a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)