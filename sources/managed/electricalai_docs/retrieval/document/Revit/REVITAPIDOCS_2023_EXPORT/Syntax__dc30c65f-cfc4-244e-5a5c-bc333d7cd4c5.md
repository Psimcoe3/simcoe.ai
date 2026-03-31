[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Definition Property

---



|  |
| --- |
| [Parameter Class](333ff41b-e6a7-d959-60bf-c3bfae495581.htm)   [See Also](#seeAlsoToggle) |

Returns the Definition object that describes the data type, name and other details of the parameter.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public Definition Definition { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Definition As Definition 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property Definition^ Definition { 	Definition^ get (); } ``` |

# Remarks

This will always be an  [InternalDefinition](97f42435-3067-622e-7a34-919f42f6ab97.htm)  object. If you want the Guid for a shared parameter, use  [GUID](50a62dcd-6027-9c69-377a-81fd96be88e8.htm)  .

# See Also

[Parameter Class](333ff41b-e6a7-d959-60bf-c3bfae495581.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)