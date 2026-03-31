[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StorageType Property

---



|  |
| --- |
| [FamilyParameter Class](6175e974-870e-7fbc-3df7-46105f937a6e.htm)   [See Also](#seeAlsoToggle) |

The storage type describes the type that is used internally within the parameter to store its value.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public StorageType StorageType { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property StorageType As StorageType 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property StorageType StorageType { 	StorageType get (); } ``` |

# Remarks

The property will return one of the following possibilities: String, Integer, Double or ElementId. Based on the value of this property the correct access and set methods should be used to retrieve and set the parameter's data value.

# See Also

[FamilyParameter Class](6175e974-870e-7fbc-3df7-46105f937a6e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)