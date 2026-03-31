[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ElementPhaseStatusFilter Members

---



|  |
| --- |
| [ElementPhaseStatusFilter Class](7767020a-2564-2c46-689d-59c2abe6e777.htm)   [Constructors](#constructorTableToggle)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [ElementPhaseStatusFilter](7767020a-2564-2c46-689d-59c2abe6e777.htm)  type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [ElementPhaseStatusFilter(ElementId, ElementOnPhaseStatus)](289d18b3-49be-82f4-dc08-01957ba168e3.htm) | Constructs a new instance of a file to match elements that have a given phase status on the input phase. |
| Public method | [ElementPhaseStatusFilter(ElementId, ICollection ElementOnPhaseStatus )](652f47dc-bce8-b3f2-9033-0fef14565fbb.htm) | Constructs a new instance of a file to match elements that have a given phase statuses on the input phase. |
| Public method | [ElementPhaseStatusFilter(ElementId, ElementOnPhaseStatus, Boolean)](5f0a0056-7ecb-372c-4c7b-7543e682aec4.htm) | Constructs a new instance of a file to match elements that have a given phase status on the input phase, with the option to match all elements that have a phase status other than the input status. |
| Public method | [ElementPhaseStatusFilter(ElementId, ICollection ElementOnPhaseStatus , Boolean)](83b9c6ff-4eba-9314-ff97-f607a698a374.htm) | Constructs a new instance of a file to match elements that have a given phase statuses on the input phase, with the option to match all elements that have a phase status other than the input statuses. |

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Dispose](5d3ffdf8-dce9-0724-d101-44693775671c.htm) | (Inherited from  [ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)  .) |
| Public method | [Equals](http://msdn2.microsoft.com/en-us/library/bsc2ak47) | Determines whether the specified  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  is equal to the current  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  . (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetHashCode](http://msdn2.microsoft.com/en-us/library/zdee4b3y) | Serves as a hash function for a particular type. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetPhaseStatuses](0cb36c92-6d1c-6715-9e68-fca6a889628e.htm) | Returns the phase statuses assigned to this filter. |
| Public method | [GetType](http://msdn2.microsoft.com/en-us/library/dfwy45w9) | Gets the  [Type](http://msdn2.microsoft.com/en-us/library/42892f65)  of the current instance. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [PassesFilter(Element)](1402f6e0-995c-2644-c7a9-7016a81a4ef4.htm) | Applies the filter to a given element. (Inherited from  [ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)  .) |
| Public method | [PassesFilter(Document, ElementId)](a8e86084-b91f-c3cf-c334-e163168328d6.htm) | Applies the filter to a given element. (Inherited from  [ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)  .) |
| Public method | [ToString](http://msdn2.microsoft.com/en-us/library/7bxwbwt2) | Returns a string that represents the current object. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Inverted](ceab2eea-cc4c-d7dc-b34c-b3c1f012eda1.htm) | True if the results of the filter are inverted; elements that would normally be accepted by this filter will be rejected, and elements that would normally be rejected will be accepted. (Inherited from  [ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)  .) |
| Public property | [IsValidObject](027ccc75-b7f6-4ee2-cf98-563df96b0dbb.htm) | Specifies whether the .NET object represents a valid Revit entity. (Inherited from  [ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)  .) |
| Public property | [PhaseId](d85cff23-7fd8-b5ec-343c-b6cc069e430a.htm) | The phase id. |

# See Also

[ElementPhaseStatusFilter Class](7767020a-2564-2c46-689d-59c2abe6e777.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)