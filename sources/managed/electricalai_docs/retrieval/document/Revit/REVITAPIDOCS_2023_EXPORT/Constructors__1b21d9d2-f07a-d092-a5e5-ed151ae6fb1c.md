[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LogicalAndFilter Members

---



|  |
| --- |
| [LogicalAndFilter Class](3e334aaf-2b39-58bd-d2cc-94e9c89bac57.htm)   [Constructors](#constructorTableToggle)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [LogicalAndFilter](3e334aaf-2b39-58bd-d2cc-94e9c89bac57.htm)  type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [LogicalAndFilter(IList ElementFilter )](ce351a2d-c43e-e941-b28c-49726099c3a0.htm) | Constructs a new instance of the logical filter with any number of input filters. |
| Public method | [LogicalAndFilter(ElementFilter, ElementFilter)](f7d7e9ae-8ace-77dd-69c2-e82580849bf2.htm) | Constructs a new instance of the logical filter with two input filters. |

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Dispose](5d3ffdf8-dce9-0724-d101-44693775671c.htm) | (Inherited from  [ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)  .) |
| Public method | Equals | Determines whether the specified  Object  is equal to the current  Object  . (Inherited from  Object  .) |
| Public method | [GetFilters](e7369155-14ee-f702-132f-b19c3a300c80.htm) | Returns an array of copies of the filters that are logically combined by this ElementLogicalFilter. (Inherited from  [ElementLogicalFilter](3b8d6b55-0cab-1810-1188-840800e5eaa2.htm)  .) |
| Public method | GetHashCode | Serves as a hash function for a particular type. (Inherited from  Object  .) |
| Public method | GetType | Gets the  Type  of the current instance. (Inherited from  Object  .) |
| Public method | [PassesFilter(Element)](1402f6e0-995c-2644-c7a9-7016a81a4ef4.htm) | Applies the filter to a given element. (Inherited from  [ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)  .) |
| Public method | [PassesFilter(Document, ElementId)](a8e86084-b91f-c3cf-c334-e163168328d6.htm) | Applies the filter to a given element. (Inherited from  [ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)  .) |
| Public method | [SetFilters](8cab13fd-eb77-5f50-0d9c-e5ceda55d681.htm) | Replaces current filters in the logical filter with any number of input filters. (Inherited from  [ElementLogicalFilter](3b8d6b55-0cab-1810-1188-840800e5eaa2.htm)  .) |
| Public method | ToString | Returns a string that represents the current object. (Inherited from  Object  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Inverted](ceab2eea-cc4c-d7dc-b34c-b3c1f012eda1.htm) | True if the results of the filter are inverted; elements that would normally be accepted by this filter will be rejected, and elements that would normally be rejected will be accepted. (Inherited from  [ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)  .) |
| Public property | [IsValidObject](027ccc75-b7f6-4ee2-cf98-563df96b0dbb.htm) | Specifies whether the .NET object represents a valid Revit entity. (Inherited from  [ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)  .) |

# See Also

[LogicalAndFilter Class](3e334aaf-2b39-58bd-d2cc-94e9c89bac57.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)