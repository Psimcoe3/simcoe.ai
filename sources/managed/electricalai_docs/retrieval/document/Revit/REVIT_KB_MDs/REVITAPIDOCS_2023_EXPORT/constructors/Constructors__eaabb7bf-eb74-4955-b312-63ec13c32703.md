[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RoutingConditions Members

---



|  |
| --- |
| [RoutingConditions Class](15fcc55d-b099-6ed4-1915-8beaee70b596.htm)   [Constructors](#constructorTableToggle)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [RoutingConditions](15fcc55d-b099-6ed4-1915-8beaee70b596.htm)  type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [RoutingConditions](a389a129-58a8-237a-570f-29424960166a.htm) | Constructs a new instance of a RoutingConditions object with an indicated error level for conditions that do not meet any routing preference rule. |

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AppendCondition](2105d8fb-9618-2b90-f983-de56b6397042.htm) | Appends a routing condition to the end of existing routing conditions. Note that the first item (indexed at 0) is the condition for the primary connector. |
| Public method | [Clear](f62c1a88-b134-4eff-cb32-e1f1726f8d0f.htm) | Clear all existing conditions |
| Public method | [Dispose](3b47a813-1bde-865b-98ce-330caaebc48a.htm) | Releases all resources used by the  [RoutingConditions](15fcc55d-b099-6ed4-1915-8beaee70b596.htm) |
| Public method | [Equals](http://msdn2.microsoft.com/en-us/library/bsc2ak47) | Determines whether the specified  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  is equal to the current  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  . (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetConditionAt](263b2107-de30-fbdf-2951-3aa4391fc64c.htm) | Gets the routing condition at the specified index position. |
| Public method | [GetHashCode](http://msdn2.microsoft.com/en-us/library/zdee4b3y) | Serves as a hash function for a particular type. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetNumberOfConditions](951a264e-7fc6-7494-5a45-87f161a64dcc.htm) | Gets the number of included routing conditions. |
| Public method | [GetType](http://msdn2.microsoft.com/en-us/library/dfwy45w9) | Gets the  [Type](http://msdn2.microsoft.com/en-us/library/42892f65)  of the current instance. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [ToString](http://msdn2.microsoft.com/en-us/library/7bxwbwt2) | Returns a string that represents the current object. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [ErrorLevel](cc96a880-9f3b-08cf-7a31-e8301a817035.htm) | The error level that the routing preference manager should post errors if the routing conditions do not meet any routing preference rule, could be None, Warning, or Error |
| Public property | [IsValidObject](a209e1ca-e1c6-1743-8dac-2aed9373585f.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| Public property | [PreferredJunctionType](476ce25e-b865-5205-6199-ec31b922de19.htm) | The junction type (Tee or Tap) to select if defined fittings of both junction types meet all routing conditions. |

# See Also

[RoutingConditions Class](15fcc55d-b099-6ed4-1915-8beaee70b596.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)