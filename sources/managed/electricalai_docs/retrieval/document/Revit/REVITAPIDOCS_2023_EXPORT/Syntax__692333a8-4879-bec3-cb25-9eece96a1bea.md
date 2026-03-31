[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LayerCapFlag Property

---



|  |
| --- |
| [CompoundStructureLayer Class](faece83a-6d49-41b0-2713-fe6cfaa5a3b5.htm)   [See Also](#seeAlsoToggle) |

Identifies if the layer participates in wrapping at end caps and/or inserts.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool LayerCapFlag { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property LayerCapFlag As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool LayerCapFlag { 	bool get (); 	void set (bool value); } ``` |

#### Field Value

True if the layer participates in wrapping, false otherwise. It is meaningful only for Shell layers (for Core layers, the value is always true). The default value is true.

# See Also

[CompoundStructureLayer Class](faece83a-6d49-41b0-2713-fe6cfaa5a3b5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)