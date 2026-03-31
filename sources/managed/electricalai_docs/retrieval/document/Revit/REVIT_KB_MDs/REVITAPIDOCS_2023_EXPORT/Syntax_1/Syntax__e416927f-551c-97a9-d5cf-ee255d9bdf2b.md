[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Format Method (Units, ForgeTypeId, Double, Boolean)

---



|  |
| --- |
| [UnitFormatUtils Class](bd635989-6abd-3486-2c34-64571370065b.htm)   [See Also](#seeAlsoToggle) |

Formats a number with units into a string.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static string Format( 	Units units, 	ForgeTypeId specTypeId, 	double value, 	bool forEditing ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Format ( _ 	units As Units, _ 	specTypeId As ForgeTypeId, _ 	value As Double, _ 	forEditing As Boolean _ ) As String ``` |

 

| Visual C++ |
| --- |
| ``` public: static String^ Format( 	Units^ units,  	ForgeTypeId^ specTypeId,  	double value,  	bool forEditing ) ``` |

#### Parameters

units
:   Type:  [Autodesk.Revit.DB Units](89d89465-897f-4105-b935-27edf67aab3e.htm)    
     The units formatting settings, typically obtained from  [Document.GetUnits()](9ed56178-e9ae-b4bc-1c0e-e6a867ae3557.htm)  .

specTypeId
:   Type:  [Autodesk.Revit.DB ForgeTypeId](d9fcf276-9566-de83-2b0b-d89b65ccc8af.htm)    
     Identifier of the spec of the value to format.

value
:   Type:  System Double    
     The value to format, in Revit's internal units.

forEditing
:   Type:  System Boolean    
     True if the formatting should be modified as necessary so that the formatted string can be successfully parsed, for example by suppressing digit grouping. False if unmodified settings should be used, suitable for display only.

#### Return Value

The formatted string.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | specTypeId is not a measurable spec identifier. See UnitUtils.IsMeasurableSpec(ForgeTypeId). -or- The given value for value is not finite |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[UnitFormatUtils Class](bd635989-6abd-3486-2c34-64571370065b.htm)

[Format Overload](1c686a96-cb13-81e5-b64c-f1ab3a144032.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)