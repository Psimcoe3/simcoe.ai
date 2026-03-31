[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TryParse Method (Units, ForgeTypeId, String, ValueParsingOptions, Double, String)

---



|  |
| --- |
| [UnitFormatUtils Class](bd635989-6abd-3486-2c34-64571370065b.htm)   [See Also](#seeAlsoToggle) |

Parses a formatted string into a number with units if possible.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static bool TryParse( 	Units units, 	ForgeTypeId specTypeId, 	string stringToParse, 	ValueParsingOptions valueParsingOptions, 	out double value, 	out string message ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function TryParse ( _ 	units As Units, _ 	specTypeId As ForgeTypeId, _ 	stringToParse As String, _ 	valueParsingOptions As ValueParsingOptions, _ 	<OutAttribute> ByRef value As Double, _ 	<OutAttribute> ByRef message As String _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool TryParse( 	Units^ units,  	ForgeTypeId^ specTypeId,  	String^ stringToParse,  	ValueParsingOptions^ valueParsingOptions,  	[OutAttribute] double% value,  	[OutAttribute] String^% message ) ``` |

#### Parameters

units
:   Type:  [Autodesk.Revit.DB Units](89d89465-897f-4105-b935-27edf67aab3e.htm)    
     The units formatting settings, typically obtained from  [Document.GetUnits()](9ed56178-e9ae-b4bc-1c0e-e6a867ae3557.htm)  .

specTypeId
:   Type:  [Autodesk.Revit.DB ForgeTypeId](d9fcf276-9566-de83-2b0b-d89b65ccc8af.htm)    
     Identifier of the target spec for the value.

stringToParse
:   Type:  System String    
     The string to parse.

valueParsingOptions
:   Type:  [Autodesk.Revit.DB ValueParsingOptions](5e3782ee-a1ed-593d-8180-37ebf36eda83.htm)    
     Additional parsing options.

value
:   Type:  System Double   %    
     The parsed value. Ignore this value if the function returns false.

message
:   Type:  System String   %    
     A localized message that, if the parsing fails, explains the reason for failure.

#### Return Value

True if the string can be parsed, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | specTypeId is not a measurable spec identifier. See UnitUtils.IsMeasurableSpec(ForgeTypeId). -or- The unit in the FormatOptions in valueParsingOptions is not a valid unit for specTypeId. See UnitUtils.IsValidUnit(ForgeTypeId, ForgeTypeId) and UnitUtils.GetValidUnits(ForgeTypeId). |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[UnitFormatUtils Class](bd635989-6abd-3486-2c34-64571370065b.htm)

[TryParse Overload](3e6dcee8-6a58-efe5-67f8-3422af74545c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)