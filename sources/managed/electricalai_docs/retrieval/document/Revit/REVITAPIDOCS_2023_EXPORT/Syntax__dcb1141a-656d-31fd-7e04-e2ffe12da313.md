[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddSize Method

---



|  |
| --- |
| [ConduitSizeSettings Class](d385e4b4-f675-9bcc-d067-5ca7d1d000d4.htm)   [See Also](#seeAlsoToggle) |

Inserts a new ConduitSize in to the conduit size settings. The conduit standard name determines the location of the new size in the size table.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public void AddSize( 	string standardName, 	ConduitSize sizeInfo ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AddSize ( _ 	standardName As String, _ 	sizeInfo As ConduitSize _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AddSize( 	String^ standardName,  	ConduitSize^ sizeInfo ) ``` |

#### Parameters

standardName
:   Type:  System String    
     The conduit standard name.

sizeInfo
:   Type:  [Autodesk.Revit.DB.Electrical ConduitSize](4271b827-6390-ab67-036a-305101a712b5.htm)    
     The new ConduitSize to be added.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The conduit standard name does not exist. -or- The conduit size already exists. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The function is called during iterating the size set. |

# See Also

[ConduitSizeSettings Class](d385e4b4-f675-9bcc-d067-5ca7d1d000d4.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)