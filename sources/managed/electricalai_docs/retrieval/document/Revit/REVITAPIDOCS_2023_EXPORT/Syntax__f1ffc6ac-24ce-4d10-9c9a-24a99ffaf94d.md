[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Location Property

---



|  |
| --- |
| [AssemblyInstance Class](4e60704c-dfe3-72b6-7892-6440503fa078.htm)   [See Also](#seeAlsoToggle) |

This property is used to find the physical location of the assembly instance within project.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public override Location Location { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Overrides ReadOnly Property Location As Location 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual property Location^ Location { 	Location^ get () override; } ``` |

# Remarks

The Location property returns an object that can be used to find the location of an object within the project. Assembly instances return a point location object positioned at the center of the assembly instance.

# See Also

[AssemblyInstance Class](4e60704c-dfe3-72b6-7892-6440503fa078.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)