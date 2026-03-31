[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### JoinType Property

---



|  |
| --- |
| [LocationCurve Class](9dd6eb99-f105-a05f-dc1b-dfde17b8768c.htm)   [See Also](#seeAlsoToggle) |

Get/change the type of the join at the specified end.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public JoinType this[ 	int end ] { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property JoinType ( _ 	end As Integer _ ) As JoinType 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property JoinType JoinType[int end] { 	JoinType get (int end); 	void set (int end, JoinType value); } ``` |

#### Parameters

end
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The end of the location curve driver under question.

# Remarks

This property allows to get join type of wall and concrete beam and to set wall's join type. The new join type is expected to be different from the current one for this end.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The element is neither a wall nor a concrete beam when it tries to get the property. The element is not a wall when it tries to set the property. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | A failure occurred while attempting to set the new type. |

# See Also

[LocationCurve Class](9dd6eb99-f105-a05f-dc1b-dfde17b8768c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)