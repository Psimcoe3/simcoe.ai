[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ElementOwnerViewFilter Members

---



|  |
| --- |
| [ElementOwnerViewFilter Class](cfaecf4c-b6b9-1481-de4f-e8d74e743911.htm)   [Constructors](#constructorTableToggle)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [ElementOwnerViewFilter](cfaecf4c-b6b9-1481-de4f-e8d74e743911.htm)  type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [ElementOwnerViewFilter(ElementId)](154a3c37-b6b8-7e40-1027-8fd883a311a9.htm) | Constructs a new instance of a filter to match elements which are owned by a particular view. |
| Public method | [ElementOwnerViewFilter(ElementId, Boolean)](8e88e85e-eeeb-e71a-e513-90f0716bee19.htm) | Constructs a new instance of a filter to match elements which are owned by a particular view, with the option to invert the filter and find elements not owned by the given view. |

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Dispose](5d3ffdf8-dce9-0724-d101-44693775671c.htm) | (Inherited from  [ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)  .) |
| Public method | [Equals](http://msdn2.microsoft.com/en-us/library/bsc2ak47) | Determines whether the specified  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  is equal to the current  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  . (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetHashCode](http://msdn2.microsoft.com/en-us/library/zdee4b3y) | Serves as a hash function for a particular type. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetType](http://msdn2.microsoft.com/en-us/library/dfwy45w9) | Gets the  [Type](http://msdn2.microsoft.com/en-us/library/42892f65)  of the current instance. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [PassesFilter(Element)](1402f6e0-995c-2644-c7a9-7016a81a4ef4.htm) | Applies the filter to a given element. (Inherited from  [ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)  .) |
| Public method | [PassesFilter(Document, ElementId)](a8e86084-b91f-c3cf-c334-e163168328d6.htm) | Applies the filter to a given element. (Inherited from  [ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)  .) |
| Public method | [ToString](http://msdn2.microsoft.com/en-us/library/7bxwbwt2) | Returns a string that represents the current object. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Inverted](ceab2eea-cc4c-d7dc-b34c-b3c1f012eda1.htm) | True if the results of the filter are inverted; elements that would normally be accepted by this filter will be rejected, and elements that would normally be rejected will be accepted. (Inherited from  [ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)  .) |
| Public property | [IsValidObject](027ccc75-b7f6-4ee2-cf98-563df96b0dbb.htm) | Specifies whether the .NET object represents a valid Revit entity. (Inherited from  [ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)  .) |
| Public property | [ViewId](38f07408-d634-20bd-a7bf-7a3a266277e5.htm) | The view id. |

# See Also

[ElementOwnerViewFilter Class](cfaecf4c-b6b9-1481-de4f-e8d74e743911.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)