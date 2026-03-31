[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AlignmentStationLabelSetOptions Members

---



|  |
| --- |
| [AlignmentStationLabelSetOptions Class](15f4337d-738d-ec32-e7bc-4f2c569f4c59.htm)   [Constructors](#constructorTableToggle)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [AlignmentStationLabelSetOptions](15f4337d-738d-ec32-e7bc-4f2c569f4c59.htm)  type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [AlignmentStationLabelSetOptions](7d52fd51-0a7d-3ead-2c2d-ea9631dc2380.htm) | Create an object with default values. |

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | Equals | Determines whether the specified  Object  is equal to the current  Object  . (Inherited from  Object  .) |
| Public method | GetHashCode | Serves as a hash function for a particular type. (Inherited from  Object  .) |
| Public method | GetType | Gets the  Type  of the current instance. (Inherited from  Object  .) |
| Public method | ToString | Returns a string that represents the current object. (Inherited from  Object  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [EndStation](cffc9f55-aad7-6af3-2fcd-2c4499171749.htm) | The ending station for creating labels in the set, in Revit internal model units (standard Imperial feet). The default value is null. When null, the station value corresponding to the alignment's  [DisplayedEndStation](cfde7e75-8057-a6d2-4493-428a035af8e0.htm)  is used. |
| Public property | [HasLeader](5ef84857-1ef1-6287-b5cc-231a314ad0db.htm) | Specifies if the label will have a leader. The default value is true. |
| Public property | [Interval](ea9ccd2c-89fd-0fa1-d179-887a204c78e4.htm) | The interval between labels to be created in the set, in Revit internal model units (standard Imperial feet). The default value is null. When null, a predefined interval value will be used, depending on the unit setting for stationing units in the document. For standard imperial, the default is 100 ft. For survey imperial, the default is 100 USft (US survey). For metric, the default is 1000 m. |
| Public property | [Offset](896fafc5-2e25-8ecb-be66-297e2a46f8b6.htm) | The offset of the labels from the alignment, in Revit internal paper space units (standard Imperial feet). A positive offset creates labels to the right of the alignment, a negative - to the left. The default value is null. If null, a predefined offset value will be used, depending on the unit setting for stationing units in the document. For standard imperial, the default is 1/8". For survey imperial, the default is 1/8" (US survey). For metric, the default is 5 mm. |
| Public property | [StartStation](5c74eaa0-bca8-10a8-a901-78de4111477b.htm) | The starting station for creating labels in the set, in Revit internal model units (standard Imperial feet). The default value is null. When null, the station value corresponding to the alignment's  [DisplayedStartStation](0a17ad4e-4a52-a955-c1af-882e2123bf49.htm)  is used. |
| Public property | [TypeId](5b0dfa5d-bc2f-b097-a8d6-c5e78c569add.htm) | Specifies the ElementId of the labels' type. The default value is InvalidElementId. in this case,  [CreateSet(Alignment, View, AlignmentStationLabelSetOptions)](bbb3fb20-cbc6-f6aa-cc23-ae7ad73747b3.htm)  will throw an exception. |

# See Also

[AlignmentStationLabelSetOptions Class](15f4337d-738d-ec32-e7bc-4f2c569f4c59.htm)

[Autodesk.Revit.DB.Infrastructure Namespace](cedea963-42a0-acf8-0f0e-5477c4212ae9.htm)