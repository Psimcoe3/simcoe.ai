[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ComputeArea Method

---



|  |
| --- |
| [Polyloop Class](207c5546-9116-fb85-8a7e-ff79654a7877.htm)   [See Also](#seeAlsoToggle) |

Gets the area for this polygon.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public double ComputeArea() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function ComputeArea As Double ``` |

 

| Visual C++ |
| --- |
| ``` public: double ComputeArea() ``` |

#### Return Value

The area for this polygon.

# Remarks

The area of the planar non-self-intersecting polygon computed as: A = 1/2 \* (X1 Y2) - (X2 Y1) + ... + (Xn Y1) - (X1 Yn)

# See Also

[Polyloop Class](207c5546-9116-fb85-8a7e-ff79654a7877.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)