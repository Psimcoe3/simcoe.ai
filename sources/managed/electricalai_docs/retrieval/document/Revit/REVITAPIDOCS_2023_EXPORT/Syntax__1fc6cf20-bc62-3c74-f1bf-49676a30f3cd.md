[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FindEntry Method

---



|  |
| --- |
| [KeyBasedTreeEntries Class](554c9024-27de-0649-7078-c778cd92be5f.htm)   [See Also](#seeAlsoToggle) |

Finds the KeyBasedTreeEntry associated with the given key value.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public KeyBasedTreeEntry FindEntry( 	string key ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function FindEntry ( _ 	key As String _ ) As KeyBasedTreeEntry ``` |

 

| Visual C++ |
| --- |
| ``` public: KeyBasedTreeEntry^ FindEntry( 	String^ key ) ``` |

#### Parameters

key
:   Type:  System String    
     The specified key value.

#### Return Value

The KeyBasedTreeEntry corresponds to the given key value.

# Remarks

If no matching KeyBasedTreeEntry can be found, null will be returned; The given key value cannot be an empty string.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | key is an empty string. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[KeyBasedTreeEntries Class](554c9024-27de-0649-7078-c778cd92be5f.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)