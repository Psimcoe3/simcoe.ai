[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ElementParameterFilter Members

---



|  |
| --- |
| [ElementParameterFilter Class](b0b40351-690c-eb5d-30c2-d4447a42fda1.htm)   [Constructors](#constructorTableToggle)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [ElementParameterFilter](b0b40351-690c-eb5d-30c2-d4447a42fda1.htm)  type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [ElementParameterFilter(FilterRule)](70b5d168-237b-b2d1-28cb-b022116ada4a.htm) | Constructs a new instance of an ElementParameterFilter from a single rule. |
| Public method | [ElementParameterFilter(IList FilterRule )](6d7271d3-7717-5a01-ebb1-8c3723b6ebb6.htm) | Constructs a new instance of an ElementParameterFilter from a set of rules. |
| Public method | [ElementParameterFilter(FilterRule, Boolean)](49a99572-3d2d-a0dc-920b-205b923f32ec.htm) | Constructs a new instance of an ElementParameterFilter, with the option to match all elements not passing a given filter rule. |
| Public method | [ElementParameterFilter(IList FilterRule , Boolean)](55dd89ad-62fd-6295-512c-7552b9a52312.htm) | Constructs a new instance of an ElementParameterFilter, with the option to match all elements not passing the given filter rules. |

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Dispose](5d3ffdf8-dce9-0724-d101-44693775671c.htm) | (Inherited from  [ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)  .) |
| Public method | [Equals](http://msdn2.microsoft.com/en-us/library/bsc2ak47) | Determines whether the specified  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  is equal to the current  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  . (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetHashCode](http://msdn2.microsoft.com/en-us/library/zdee4b3y) | Serves as a hash function for a particular type. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetRules](9442366a-20e8-5a36-39dc-79e0d1c98e41.htm) | Returns the set of rules contained in this filter. |
| Public method | [GetType](http://msdn2.microsoft.com/en-us/library/dfwy45w9) | Gets the  [Type](http://msdn2.microsoft.com/en-us/library/42892f65)  of the current instance. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [PassesFilter(Element)](1402f6e0-995c-2644-c7a9-7016a81a4ef4.htm) | Applies the filter to a given element. (Inherited from  [ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)  .) |
| Public method | [PassesFilter(Document, ElementId)](a8e86084-b91f-c3cf-c334-e163168328d6.htm) | Applies the filter to a given element. (Inherited from  [ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)  .) |
| Public method | [ToString](http://msdn2.microsoft.com/en-us/library/7bxwbwt2) | Returns a string that represents the current object. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Inverted](ceab2eea-cc4c-d7dc-b34c-b3c1f012eda1.htm) | True if the results of the filter are inverted; elements that would normally be accepted by this filter will be rejected, and elements that would normally be rejected will be accepted. (Inherited from  [ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)  .) |
| Public property | [IsValidObject](027ccc75-b7f6-4ee2-cf98-563df96b0dbb.htm) | Specifies whether the .NET object represents a valid Revit entity. (Inherited from  [ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)  .) |

# See Also

[ElementParameterFilter Class](b0b40351-690c-eb5d-30c2-d4447a42fda1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)