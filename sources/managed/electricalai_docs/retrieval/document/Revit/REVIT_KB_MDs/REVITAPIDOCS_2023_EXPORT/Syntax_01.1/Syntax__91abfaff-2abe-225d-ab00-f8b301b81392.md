[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetFlags Method (IList(Int32))

---



|  |
| --- |
| [ValueAtPointBase Class](67c49547-b5b9-59ad-8106-65d90886a381.htm)   [See Also](#seeAlsoToggle) |

Independently sets the flags associated to all measurements.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public void SetFlags( 	IList<int> flags ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetFlags ( _ 	flags As IList(Of Integer) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetFlags( 	IList<int>^ flags ) ``` |

#### Parameters

flags
:   Type:  System.Collections.Generic IList   Int32    
     An array of flags values. Each member corresponds to a measurement. Flags values are defined in the enumerated class ValueAtPointFlags and are combined into the int value. Number of measurements is set at creation of SpatialFieldManager in method createSpatialFieldManager.

# Remarks

If you set the array of flags to only contain one value, this flags value will apply to all measurements

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ValueAtPointBase Class](67c49547-b5b9-59ad-8106-65d90886a381.htm)

[SetFlags Overload](dff6d4fa-7c12-ca4e-0439-75b1e4f80b9e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)