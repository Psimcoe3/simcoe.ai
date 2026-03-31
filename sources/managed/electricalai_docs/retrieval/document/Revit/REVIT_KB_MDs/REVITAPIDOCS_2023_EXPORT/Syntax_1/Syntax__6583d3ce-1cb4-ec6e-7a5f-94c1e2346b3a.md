[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MaximumBackups Property

---



|  |
| --- |
| [SaveAsOptions Class](f8eecf56-8b25-4140-d66e-c87f0d664ee1.htm)   [See Also](#seeAlsoToggle) |

The maximum number of backups to keep on disk.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public int MaximumBackups { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property MaximumBackups As Integer 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property int MaximumBackups { 	int get (); 	void set (int value); } ``` |

#### Field Value

A positive number means to keep at most that many backups.

The default value of -1 means to use Revit's defaults: 3 for non-workshared, 20 for workshared. After initialization, the setter can be used to choose a positive number, but cannot be used to restore this default value.

# Remarks

Non-workshared models have whole-file backups, sequentially numbered.

File-based workshared models have eager, incremental backups in a backup folder adjacent to the model itself: Every save backs up all changed data and avoids recopying unchanged elements, so the latest backup is equivalent to the main copy on disk and the backup folder does not have huge amounts of redundant data.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The requested number of backups is out of range. |

# See Also

[SaveAsOptions Class](f8eecf56-8b25-4140-d66e-c87f0d664ee1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)