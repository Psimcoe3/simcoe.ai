[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Item Property

---



|  |
| --- |
| [ExportLineweightTable Class](5620708e-0c7c-ced6-9887-0237a9229800.htm)   [See Also](#seeAlsoToggle) |

A copy of the  [ExportLineweightInfo](730cd713-bb8b-8a69-739e-d9bae8eb6fa5.htm)  for the line weight's  [ExportLineweightKey](5b3250ab-f70b-6f87-afbf-dd049a64c29e.htm)  .

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public ExportLineweightInfo this[ 	ExportLineweightKey lineweightKey ] { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Default Property Item ( _ 	lineweightKey As ExportLineweightKey _ ) As ExportLineweightInfo 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual property ExportLineweightInfo^ default[ExportLineweightKey^ lineweightKey] { 	ExportLineweightInfo^ get (ExportLineweightKey^ lineweightKey) sealed; 	void set (ExportLineweightKey^ lineweightKey, ExportLineweightInfo^ value) sealed; } ``` |

#### Parameters

lineweightKey
:   Type:  [Autodesk.Revit.DB ExportLineweightKey](5b3250ab-f70b-6f87-afbf-dd049a64c29e.htm)

#### Return Value

A copy of the  [ExportLineweightInfo](730cd713-bb8b-8a69-739e-d9bae8eb6fa5.htm)  .

# Remarks

When getting this property, it returns a copy of the  [ExportLineweightInfo](730cd713-bb8b-8a69-739e-d9bae8eb6fa5.htm)  from the table. In order to make changes to the  [ExportLineweightInfo](730cd713-bb8b-8a69-739e-d9bae8eb6fa5.htm)  and use those settings during export, set the modified  [ExportLineweightInfo](730cd713-bb8b-8a69-739e-d9bae8eb6fa5.htm)  back into the table using the same key.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When getting this property: An entry with the given key is not present in the table. |

# See Also

[ExportLineweightTable Class](5620708e-0c7c-ced6-9887-0237a9229800.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)