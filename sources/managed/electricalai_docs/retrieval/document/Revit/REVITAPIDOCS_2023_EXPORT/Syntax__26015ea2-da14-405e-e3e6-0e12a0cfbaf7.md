[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GUID Property

---



|  |
| --- |
| [ExternalDefinition Class](a3e84415-b88e-a8e0-4e11-64795d92da0e.htm)   [See Also](#seeAlsoToggle) |

Returns the GUID associated with the shared parameter definition.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual Guid GUID { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable ReadOnly Property GUID As Guid 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual property Guid GUID { 	Guid get (); } ``` |

# Remarks

Each shared parameter when created is issued a unique identifier. This identifier can then be used at a later time to retrieve the parameter from the Element ensuring that the correct parameter is always retrieved.

# See Also

[ExternalDefinition Class](a3e84415-b88e-a8e0-4e11-64795d92da0e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)