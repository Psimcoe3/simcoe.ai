[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Tap Property

---



|  |
| --- |
| [MEPCurveType Class](97c98bd6-0966-5b0c-6f75-4c34f16adce1.htm)   [See Also](#seeAlsoToggle) |

The default tap fitting of the MEP curve type.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public FamilySymbol Tap { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Tap As FamilySymbol 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property FamilySymbol^ Tap { 	FamilySymbol^ get (); 	void set (FamilySymbol^ value); } ``` |

# Remarks

This property is used to retrieve the default tap fitting of the MEP curve type, and can be    a null reference (  Nothing  in Visual Basic)  if there is no default value. Use  [RoutingPreferenceManager](a8300b97-72a6-beb5-733b-ec4cfea6c472.htm)  to set this property for PipeType MEPCurves.

# See Also

[MEPCurveType Class](97c98bd6-0966-5b0c-6f75-4c34f16adce1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)