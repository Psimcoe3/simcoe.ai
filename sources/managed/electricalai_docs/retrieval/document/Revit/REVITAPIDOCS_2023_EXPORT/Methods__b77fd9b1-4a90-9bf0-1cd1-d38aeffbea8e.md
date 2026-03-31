[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GroupNode Members

---



|  |
| --- |
| [GroupNode Class](8b1cabde-3c37-1735-a186-2ce026555ce0.htm)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [GroupNode](8b1cabde-3c37-1735-a186-2ce026555ce0.htm)  type exposes the following members.

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Dispose](8ee082fe-ab92-67e6-f2bd-b285d419a005.htm) | (Inherited from  [RenderNode](9900b69b-7cb7-8555-75ac-4b5f22b5fa7f.htm)  .) |
| Public method | Equals | Determines whether the specified  Object  is equal to the current  Object  . (Inherited from  Object  .) |
| Public method | GetHashCode | Serves as a hash function for a particular type. (Inherited from  Object  .) |
| Public method | [GetSymbolId](dfcbb10c-a314-be18-0eef-b7f07f08c59d.htm) | **Obsolete.**   The Id of the symbol associated with the node. This property is deprecated in Revit 2023 and may be removed in a future version of Revit. For an InstanceNode please use the GetSymbolGeometryId().SymbolId. For a LinkNode please use SymbolId property. In Revit 2023 we introduced instance nodes that point to a part of the symbol's geometry. For comparing if two such nodes point to the same geometry, the SymbolId isn't enough. SymbolGeometryId can be used to identify a piece of geometry managed by a symbol element. |
| Public method | [GetTransform](13e9ba28-e94a-c79f-689c-4367883d62bd.htm) | A transformation matrix associated with the node. |
| Public method | GetType | Gets the  Type  of the current instance. (Inherited from  Object  .) |
| Public method | ToString | Returns a string that represents the current object. (Inherited from  Object  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [IsValidObject](5e642162-fd60-8697-24d2-b2c8574d4fb2.htm) | Specifies whether the .NET object represents a valid Revit entity. (Inherited from  [RenderNode](9900b69b-7cb7-8555-75ac-4b5f22b5fa7f.htm)  .) |
| Public property | [NodeName](f00a73db-fecc-70eb-c81a-67ef27212de5.htm) | A readable name of the output node. (Inherited from  [RenderNode](9900b69b-7cb7-8555-75ac-4b5f22b5fa7f.htm)  .) |

# See Also

[GroupNode Class](8b1cabde-3c37-1735-a186-2ce026555ce0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)