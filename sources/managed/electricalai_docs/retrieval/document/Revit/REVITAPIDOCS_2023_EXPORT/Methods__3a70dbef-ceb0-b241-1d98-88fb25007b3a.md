[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FabricationService Members

---



|  |
| --- |
| [FabricationService Class](e29ecbb2-7de0-c341-0db0-9f77bd0f5543.htm)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [FabricationService](e29ecbb2-7de0-c341-0db0-9f77bd0f5543.htm)  type exposes the following members.

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Dispose](769b9c47-e567-40a6-514a-f1033d98070f.htm) | Releases all resources used by the  [FabricationService](e29ecbb2-7de0-c341-0db0-9f77bd0f5543.htm) |
| Public method | Equals | Determines whether the specified  Object  is equal to the current  Object  . (Inherited from  Object  .) |
| Public method | [GetButton](a07bb5f7-6c08-3d6b-25ea-5891cc2dfc5e.htm) | Gets the service button for a given palette index and button index from the service. |
| Public method | [GetButtonCount](c80b99e4-736f-e357-2d3c-efe0ed2fa91d.htm) | Gets the number of buttons for a given palette in the service. |
| Public method | GetHashCode | Serves as a hash function for a particular type. (Inherited from  Object  .) |
| Public method | [GetPaletteName](0d12d23a-a3f0-48e6-fc70-be50d0ffeb23.htm) | Gets the name of a palette based on palette index. |
| Public method | GetType | Gets the  Type  of the current instance. (Inherited from  Object  .) |
| Public method | [IsCompatibleWith](e5a1a4bc-fcfb-9b02-c76c-98d42ed424a5.htm) | Check whether the service is broadly interchangable with another one without affecting part geometry. The services must have the same fabrication system template and specification. |
| Public method | [IsPaletteExcluded](a19ff9d5-04f1-dc18-d591-66f6f9c9bfa0.htm) | Get whether a service palette is excluded from being used by the Route and Fill, Design to Fabrication, or Multi Point Routing commands. The default configuration values may be overridden by SetServicePaletteExclusions. |
| Public method | [IsValidButtonIndex](1936cceb-ffc4-9631-2d90-28e937bf2578.htm) | Validates the button index. |
| Public method | [IsValidPaletteIndex](910a66d8-190d-29a4-9129-4c5deb9eb729.htm) | Validates the palette index. |
| Public method | [OverrideServiceButtonExclusion](5a0ce9ef-042c-def5-2d9a-c5f15e308040.htm) | Overrides the default service button exclusions, used by Route and Fill, Design to Fabrication, or Multi Point Routing for the current user and session only. |
| Public method | [ResetServiceExclusionOverrides](8f03af55-9ed3-1695-a046-06973e7e0322.htm) | Resets the overridden service palette and button exclusions back to default, as defined by the configuration. |
| Public method | [SetServicePaletteExclusions](c00b14ba-4728-c10d-8c07-28244dc84dcb.htm) | Sets the service palette exclusions, used by Route and Fill or Design to Fabrication commands, for the current user and session only. This will alter them from the default configuration exclusions to only exclude those palettes passed. |
| Public method | ToString | Returns a string that represents the current object. (Inherited from  Object  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Abbreviation](fcef8b4f-7eb1-f7c8-d0ff-25cd28f1f812.htm) | The short name of service. |
| Public property | [FabricationSystemName](f3911743-f9ff-2a97-02a1-4b6edb45b5df.htm) | The fabrication system name of the service. |
| Public property | [IsValidObject](de24cfdf-2390-854d-d701-a6185939a40b.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| Public property | [Name](1d2005ff-1410-f076-1020-67e4579d2075.htm) | The name of the service. |
| Public property | [PaletteCount](a421bef8-a36f-d4ef-183b-c0e4f0f30b1c.htm) | The number of palettes in the service. |
| Public property | [ServiceId](f9b3e6cc-935f-20e1-1985-323589f08e90.htm) | The service identifier of the service. |

# See Also

[FabricationService Class](e29ecbb2-7de0-c341-0db0-9f77bd0f5543.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)