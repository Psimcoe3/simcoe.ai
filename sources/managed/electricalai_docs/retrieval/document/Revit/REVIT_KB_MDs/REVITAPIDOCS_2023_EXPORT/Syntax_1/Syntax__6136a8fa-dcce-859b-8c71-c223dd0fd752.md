[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LayerModifier Constructor (ModifierType, String)

---



|  |
| --- |
| [LayerModifier Class](ae7bade6-00b8-698f-d2a4-541905b668e9.htm)   [See Also](#seeAlsoToggle) |

Constructs a new LayerModifier with modifierType and separator.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public LayerModifier( 	ModifierType modifierType, 	string separator ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	modifierType As ModifierType, _ 	separator As String _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: LayerModifier( 	ModifierType modifierType,  	String^ separator ) ``` |

#### Parameters

modifierType
:   Type:  [Autodesk.Revit.DB ModifierType](14da29ca-e466-9c3f-7a5b-5988a0e0ef6b.htm)    
     The modifier type.

separator
:   Type:  System String    
     The separator string that will follow this modifier in the export layer name.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The provided separator contains invalid characters (most special characters are invalid). |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[LayerModifier Class](ae7bade6-00b8-698f-d2a4-541905b668e9.htm)

[LayerModifier Overload](f2715e73-0160-8057-c05e-e0dce23f688b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)