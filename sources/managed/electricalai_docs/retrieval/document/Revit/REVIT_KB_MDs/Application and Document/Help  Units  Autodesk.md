---
created: 2026-01-28T20:43:01 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Units | Autodesk

> ## Excerpt
> The two main classes in the Revit API for working with units are Units and FormatOptions. The Units class represents a document's default settings for formatting numbers with units as strings. It contains a FormatOptions object for each unit type as well as settings related to decimal symbol and digit grouping.

---
The two main classes in the Revit API for working with units are Units and FormatOptions. The Units class represents a document's default settings for formatting numbers with units as strings. It contains a FormatOptions object for each unit type as well as settings related to decimal symbol and digit grouping.

The `Units` class stores a `FormatOptions` object for every valid unit type, but not all of them can be directly modified. Some, like `SpecTypeId.Number` and `SpecTypeId.SiteAngle`, have fixed definitions. Others have definitions which are automatically derived from other unit types. For example, `SpecTypeId.SheetLength` is derived from `SpecTypeId.Length` and `SpecTypeId.ForceScale` is derived from `SpecTypeId.Force`.

The FormatOptions class contains settings that control how to format numbers with units as strings. It contains those settings that are typically chosen by an end-user in the Format dialog and stored in the document, such as rounding, accuracy, display units, and whether to suppress spaces or leading or trailing zeros.

The FormatOptions class is used in two different ways. A FormatOptions object in the Units class represents the default settings for the document. A FormatOptions object used elsewhere represents settings that may optionally override the default settings.

The UseDefault property controls whether a FormatOptions object represents default or custom formatting. If UseDefault is true, formatting will be according to the default settings in the Units class, and none of the other settings in the object are meaningful. If UseDefault is false, the object contains custom settings that override the default settings in the Units class. UseDefault is always false for FormatOptions objects in the Units class.

## Unit Conversion

The Revit API provides utility classes to facilitate working with quantities in Revit. The UnitUtils class makes it easy to convert unit data to and from Revit's internal units.

The UnitUtils class offers a set of methods for mapping between enumeration values and ForgeTypeId values to assist clients in migrating code to ForgeTypeId such as:

-   UnitUtils.GetDiscipline()
-   UnitUtils.IsMeasurableSpec()
-   UnitUtils.IsSymbol()

Revit has seven base quantities, each with its own internal unit. These internal units are identified in the following table.

**Table 9: 7 Base Units in Revit Unit System**

<table summary="" id="GUID-099B3FD9-1C5B-459C-AC1E-EF958551DFB6__TABLE_32F4CA8500D343A8B7A6486F4FFB51DF"><tbody><tr><td><b>Base Unit</b></td><td><b>Unit In Revit</b></td><td><b>Unit System</b></td></tr><tr><td>Length</td><td>Feet (ft)</td><td>Imperial</td></tr><tr><td>Angle</td><td>Radian</td><td>Metric</td></tr><tr><td>Mass</td><td>Kilogram (kg)</td><td>Metric</td></tr><tr><td>Time</td><td>Seconds (s)</td><td>Metric</td></tr><tr><td>Electric Current</td><td>Ampere (A)</td><td>Metric</td></tr><tr><td>Temperature</td><td>Kelvin (K)</td><td>Metric</td></tr><tr><td>Luminous Intensity</td><td>Candela (cd)</td><td>Metric</td></tr></tbody></table>

Note: Since Revit stores lengths in feet and other basic quantities in metric units, a derived unit involving length will be a non-standard unit based on both the Imperial and the Metric systems. For example, since a force is measured in "mass-length per time squared", it is stored in kg-ft / s<sub id="GUID-099B3FD9-1C5B-459C-AC1E-EF958551DFB6__GUID-CDF72B07-27F9-460A-832A-5784F65CEFCD">2</sub>. The following example uses the UnitUtils.ConvertFromInternalUnits() method to get the minimum yield stress for a material in kips per square inch.

<table summary="" id="GUID-099B3FD9-1C5B-459C-AC1E-EF958551DFB6__TABLE_5CC927E9E03840619648898E366D1D5E"><tbody><tr><td><b>Code Region: Converting from Revit's internal units</b></td></tr><tr><td><pre><code><span>double</span><span> </span><span>GetYieldStressInKsi</span><span>(</span><span>Material</span><span> material</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>double</span><span> dMinYieldStress </span><span>=</span><span> </span><span>0</span><span>;</span><span>
    </span><span>// Get the structural asset for the material</span><span>
    </span><span>ElementId</span><span> strucAssetId </span><span>=</span><span> material</span><span>.</span><span>StructuralAssetId</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>strucAssetId </span><span>!=</span><span> </span><span>ElementId</span><span>.</span><span>InvalidElementId</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>PropertySetElement</span><span> pse </span><span>=</span><span> material</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>strucAssetId</span><span>)</span><span> </span><span>as</span><span> </span><span>PropertySetElement</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(</span><span>pse </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>StructuralAsset</span><span> asset </span><span>=</span><span> pse</span><span>.</span><span>GetStructuralAsset</span><span>();</span><span>

            </span><span>// Get the min yield stress and convert to ksi</span><span>
            dMinYieldStress </span><span>=</span><span> asset</span><span>.</span><span>MinimumYieldStress</span><span>;</span><span>
            dMinYieldStress </span><span>=</span><span> </span><span>UnitUtils</span><span>.</span><span>ConvertFromInternalUnits</span><span>(</span><span>dMinYieldStress</span><span>,</span><span>
                </span><span>UnitTypeId</span><span>.</span><span>KipsPerSquareInch</span><span>);</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> dMinYieldStress</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The UnitUtils can also be used to convert a value from one unit type to another, such as square feet to square meters. In the following example, a wall's top offset value that was entered in inches is converted to feet, the expected unit for setting that value.

<table summary="" id="GUID-099B3FD9-1C5B-459C-AC1E-EF958551DFB6__TABLE_2259B9502C1345ACB412C97DAE113808"><tbody><tr><td><b>Code Region: Converting between units</b></td></tr><tr><td><pre><code><span>void</span><span> </span><span>SetTopOffset</span><span>(</span><span>Wall</span><span> wall</span><span>,</span><span> </span><span>double</span><span> dOffsetInches</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// convert user-defined offset value to feet from inches prior to setting</span><span>
    </span><span>double</span><span> dOffsetFeet </span><span>=</span><span> </span><span>UnitUtils</span><span>.</span><span>Convert</span><span>(</span><span>dOffsetInches</span><span>,</span><span>
                                            </span><span>UnitTypeId</span><span>.</span><span>Inches</span><span>,</span><span>
                                            </span><span>UnitTypeId</span><span>.</span><span>Feet</span><span>);</span><span>

    </span><span>Parameter</span><span> paramTopOffset </span><span>=</span><span> wall</span><span>.</span><span>GetParameter</span><span>(</span><span>ParameterTypeId</span><span>.</span><span>WallTopOffset</span><span>);</span><span>
    paramTopOffset</span><span>.</span><span>Set</span><span>(</span><span>dOffsetFeet</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Unit formatting and parsing

Another utility class, UnitFormatUtils, can format data or parse formatted unit data.

The overloaded method Format() can be used to format a value into a string based on formatting options as the following example demonstrates. The material density is retrieved and then the value is then converted to a user-friendly value with unit using the Format() method.

<table summary="" id="GUID-099B3FD9-1C5B-459C-AC1E-EF958551DFB6__TABLE_6313BAF0D4BC49F48AAA2D7ACE10992E"><tbody><tr><td><b>Code Region: Format value to string</b></td></tr><tr><td><pre><code><span>void</span><span> </span><span>DisplayDensityOfMaterial</span><span>(</span><span>Material</span><span> material</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>double</span><span> density </span><span>=</span><span> </span><span>0</span><span>;</span><span>
    </span><span>// get structural asset of material in order to get the density</span><span>
    </span><span>ElementId</span><span> strucAssetId </span><span>=</span><span> material</span><span>.</span><span>StructuralAssetId</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>strucAssetId </span><span>!=</span><span> </span><span>ElementId</span><span>.</span><span>InvalidElementId</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>PropertySetElement</span><span> pse </span><span>=</span><span> material</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>strucAssetId</span><span>)</span><span> </span><span>as</span><span> </span><span>PropertySetElement</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(</span><span>pse </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>StructuralAsset</span><span> asset </span><span>=</span><span> pse</span><span>.</span><span>GetStructuralAsset</span><span>();</span><span>

            density </span><span>=</span><span> asset</span><span>.</span><span>Density</span><span>;</span><span>
            </span><span>// convert the density value to a user readable string that includes the units</span><span>
            </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Units</span><span> units </span><span>=</span><span> material</span><span>.</span><span>Document</span><span>.</span><span>GetUnits</span><span>();</span><span>
            </span><span>// false for maxAccuracy means accuracy specified by the FormatOptions should be used</span><span>
            </span><span>// false for forEditing since this will be for display only and no formatting modifications are necessary</span><span>
            </span><span>string</span><span> strDensity </span><span>=</span><span> </span><span>UnitFormatUtils</span><span>.</span><span>Format</span><span>(</span><span>units</span><span>,</span><span> </span><span>SpecTypeId</span><span>.</span><span>UnitWeight</span><span>,</span><span> density</span><span>,</span><span> </span><span>false</span><span>);</span><span>
            </span><span>string</span><span> msg </span><span>=</span><span> </span><span>string</span><span>.</span><span>Format</span><span>(</span><span>"Raw Value: {0}\r\nFormatted Value: {1}"</span><span>,</span><span> density</span><span>,</span><span> strDensity</span><span>);</span><span>
            </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Material Density"</span><span>,</span><span> msg</span><span>);</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The overloaded UnitFormatUtils.TryParse() method parses a formatted string, including units, into a value if possible, using the Revit internal units of the specified unit type. The following example takes a user entered length value, assumed to be a number and length unit, and attempts to parse it into a length value. The result is compared with the input string in a TaskDialog for demonstration purposes.

<table summary="" id="GUID-099B3FD9-1C5B-459C-AC1E-EF958551DFB6__TABLE_909C8B62079A453A805F5689AFADBAF9"><tbody><tr><td><b>Code Region: Parse string</b></td></tr><tr><td><pre><code><span>double</span><span> </span><span>GetLengthInput</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>String</span><span> userInputLength</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>double</span><span> dParsedLength </span><span>=</span><span> </span><span>0</span><span>;</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Units</span><span> units </span><span>=</span><span> document</span><span>.</span><span>GetUnits</span><span>();</span><span>
    </span><span>// try to parse a user entered string (i.e. 100 mm, 1'6")</span><span>
    </span><span>bool</span><span> parsed </span><span>=</span><span> </span><span>UnitFormatUtils</span><span>.</span><span>TryParse</span><span>(</span><span>units</span><span>,</span><span> </span><span>SpecTypeId</span><span>.</span><span>Length</span><span>,</span><span> userInputLength</span><span>,</span><span> </span><span>out</span><span> dParsedLength</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>parsed </span><span>==</span><span> </span><span>true</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>string</span><span> msg </span><span>=</span><span> </span><span>string</span><span>.</span><span>Format</span><span>(</span><span>"User Input: {0}\r\nParsed value: {1}"</span><span>,</span><span> userInputLength</span><span>,</span><span> dParsedLength</span><span>);</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Parsed Data"</span><span>,</span><span> msg</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> dParsedLength</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
