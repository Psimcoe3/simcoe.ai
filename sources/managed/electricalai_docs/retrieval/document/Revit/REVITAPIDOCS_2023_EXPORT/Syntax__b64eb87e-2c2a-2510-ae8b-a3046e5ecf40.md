[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DocumentIsNotTransmitted Method

---



|  |
| --- |
| [TransmissionData Class](d78d1e9c-1cee-1336-88d5-b605dacd077d.htm)   [See Also](#seeAlsoToggle) |

Determines whether the document at a given file location is not transmitted.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static bool DocumentIsNotTransmitted( 	ModelPath filePath ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function DocumentIsNotTransmitted ( _ 	filePath As ModelPath _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool DocumentIsNotTransmitted( 	ModelPath^ filePath ) ``` |

#### Parameters

filePath
:   Type:  [Autodesk.Revit.DB ModelPath](40a84c72-e4b8-72ac-2f71-3216c66a11b3.htm)    
     The path to the document whose transmitted state will be checked.

#### Return Value

False if the document is a transmitted file, true otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[TransmissionData Class](d78d1e9c-1cee-1336-88d5-b605dacd077d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)