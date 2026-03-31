[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FillPattern Members

---



|  |
| --- |
| [FillPattern Class](cc546ee9-ba80-c13d-4b74-8c0e2517bc28.htm)   [Constructors](#constructorTableToggle)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [FillPattern](cc546ee9-ba80-c13d-4b74-8c0e2517bc28.htm)  type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [FillPattern](ec498d1c-9e3e-5047-783a-eed9a0544114.htm) | Creates a fill pattern with FillPatternHostOrientation::FPORIENTATION\_TO\_VIEW and FillPatternTarget::FPTARGET\_NONE. |
| Public method | [FillPattern(FillPattern)](eb7e1a07-a963-9e4e-8c12-e09f5cfeec10.htm) | Constructs a new copy of the input FillPattern object. |
| Public method | [FillPattern(String, FillPatternTarget, FillPatternHostOrientation)](0b76f862-e80a-391a-fb4b-b71ae42c7d21.htm) | Creates a fill pattern based on the given name, FillPatternTarget and FillPatternHostOrientation. |
| Public method | [FillPattern(String, FillPatternTarget, FillPatternHostOrientation, Double, Double)](e8f8a300-7e69-9e4f-00bf-ff9766a6b795.htm) | Creates a simple hatch fill pattern based on the given name, angle, spacing, FillPatternTarget and FillPatternHostOrientation. |
| Public method | [FillPattern(String, FillPatternTarget, FillPatternHostOrientation, Double, Double, Double)](6e3e1d3b-454f-510b-6651-0ea4885e3c4e.htm) | Creates a simple crosshatch fill pattern based on the given name, angle, spacing, FillPatternTarget and FillPatternHostOrientation. |

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Dispose](e8ddacd6-aa4c-3784-d61e-8fff7dbfea0f.htm) | Releases all resources used by the  [FillPattern](cc546ee9-ba80-c13d-4b74-8c0e2517bc28.htm) |
| Public method | Equals | Determines whether the specified  Object  is equal to the current  Object  . (Inherited from  Object  .) |
| Public method | [ExpandDots](e64c2ae9-9c7d-412b-e4b1-3f3c084cf800.htm) | Corrects pattern dots to make them be drawn properly for Revit. |
| Public method | [GetFillGrid](71be2141-457a-b6ce-9c67-ce7b21097316.htm) | Gets the specified fill grid. |
| Public method | [GetFillGrids](d05f4cd1-d5df-093d-693e-545b4250ee29.htm) | Gets all fill grids in this fill pattern |
| Public method | GetHashCode | Serves as a hash function for a particular type. (Inherited from  Object  .) |
| Public method | GetType | Gets the  Type  of the current instance. (Inherited from  Object  .) |
| Public method | [IsEqual](6664e193-7745-d06c-1183-37a07824f083.htm) | Check if the contents and the name of the fill pattern is the same as the name and contents of this fill pattern. |
| Public method | [SetFillGrid](1f12079c-df50-838e-9693-5a1caf23de29.htm) | Sets the fill grid. |
| Public method | [SetFillGrids](843826d6-9ba4-90e2-1ca7-e1db865a2935.htm) | Set the fill grids in this fill pattern. |
| Public method | ToString | Returns a string that represents the current object. (Inherited from  Object  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [GridCount](7348c6d0-75cb-d635-5b21-c8a7110c2988.htm) | Gets the count of the fill grids in this fill pattern. |
| Public property | [HostOrientation](fa674429-b175-bfa5-8d63-45d8b3179983.htm) | Orientation to host layer. |
| Public property | [IsSolidFill](91cf0879-d401-4f6b-c26b-6b3ece4200db.htm) | Check if the fill pattern is a solid fill pattern. |
| Public property | [IsValidObject](1810b45b-9f4a-e9c1-cde4-c1a70f03c1c2.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| Public property | [LengthPerArea](12dfd512-72de-a97c-ed3d-78eb1515fc63.htm) | Gets length of all lines that placed on unit area. |
| Public property | [LinesPerLength](9d1802db-68b1-6d95-b06c-57792c1aad6f.htm) | Gets the number of solid lines that placed in unit length. |
| Public property | [Name](b213b64f-ec78-9d70-4650-de5bb265c4ac.htm) | The name of the fill pattern. |
| Public property | [StrokesPerArea](610876a6-2542-acde-7cfc-8f50e231c213.htm) | Gets the number of strokes that placed on unit area. |
| Public property | [Target](6806fd05-a364-5cd1-a545-7891a4f71b86.htm) | Target of this fill pattern applied to. |

# See Also

[FillPattern Class](cc546ee9-ba80-c13d-4b74-8c0e2517bc28.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)