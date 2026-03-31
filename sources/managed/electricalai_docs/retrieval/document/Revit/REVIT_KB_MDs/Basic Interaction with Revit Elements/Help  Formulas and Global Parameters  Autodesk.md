---
created: 2026-01-28T20:50:07 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Global_Parameters_Formulas_and_Global_Parameters_html
author: 
---

# Help | Formulas and Global Parameters | Autodesk

> ## Excerpt
> Formulas may be assigned to non-reporting parameters.

---
Formulas may be assigned to non-reporting parameters.

As with family parameters, formulas may be assigned to global parameters using the GlobalParameter.SetFormula() method. Since a global parameter must be non-reporting to set a formula, a reporting parameter must be changed to non-reporting prior to assigning a formula.

Value of the evaluated formula must be compatible with the value-type of the parameter. For example, it is permitted to use **Integer** parameters in a formula assigned to a Double ( **Number**) parameter, or vice versa. It is not allowed, however, to use **Length** or **Angle** arguments in a formula in a parameter whose type is ether **Integer** or **Number**.

Formulas may include all standard arithmetic operations and logical operations (as functions **and**, **or**, **not**.) Input to logical operations must be Boolean values (parameters of YesNo type). Consequently, arithmetic operations can be applied to numeric values only. While there are no operations supported for string (text) arguments, strings can be used as results of a logical **If** operation. Depending on their type (and units), parameters of different value types can be combined. However, unit-less values such as **Integer** and **Number** (double) may only be combined with each other.

Since formulas can get quite complicated, and since some formulas cannot be assigned to certain parameters, the method IsValidFormula() can be used to test whether a formula is valid for a global parameter. If SetFormula() is called with an invalid formula for the global parameter, an Exception will be thrown.

GetFormula() will return the current formula in the form of a string.

The following code sample creates four global parameters and then sets a formula to one so that it has a value of either of two other parameters depending on the boolean value of the fourth one.

<table summary="" id="GUID-2B4E911F-30B2-49D4-830B-880814F3753A__TABLE_A9CB38B47E414A8E8C0BF70AA9BB2F44"><tbody><tr><td><b>Code Region: Setting a formula</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>SetCombinationParameters</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>GlobalParameter</span><span> gpB </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>GlobalParameter</span><span> gpT </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>GlobalParameter</span><span> gpF </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>GlobalParameter</span><span> gpX </span><span>=</span><span> </span><span>null</span><span>;</span><span>

    </span><span>int</span><span> TRUE </span><span>=</span><span> </span><span>1</span><span>;</span><span>
    </span><span>int</span><span> FALSE </span><span>=</span><span> </span><span>0</span><span>;</span><span>

    </span><span>// transaction to create global parameters and set their values</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> trans </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>document</span><span>,</span><span> </span><span>"Creating global parameters"</span><span>))</span><span>
    </span><span>{</span><span>
        </span><span>// create 4 new global parameters</span><span>

        trans</span><span>.</span><span>Start</span><span>();</span><span>

        gpB </span><span>=</span><span> </span><span>GlobalParameter</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> </span><span>"GPB"</span><span>,</span><span> </span><span>SpecTypeId</span><span>.</span><span>Boolean</span><span>.</span><span>YesNo</span><span>);</span><span>
        gpT </span><span>=</span><span> </span><span>GlobalParameter</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> </span><span>"GPT"</span><span>,</span><span> </span><span>SpecTypeId</span><span>.</span><span>String</span><span>.</span><span>Text</span><span>);</span><span>
        gpF </span><span>=</span><span> </span><span>GlobalParameter</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> </span><span>"GPF"</span><span>,</span><span> </span><span>SpecTypeId</span><span>.</span><span>String</span><span>.</span><span>Text</span><span>);</span><span>
        gpX </span><span>=</span><span> </span><span>GlobalParameter</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> </span><span>"GPX"</span><span>,</span><span> </span><span>SpecTypeId</span><span>.</span><span>String</span><span>.</span><span>Text</span><span>);</span><span>

        </span><span>// assign initial values and a formula to the global parameters</span><span>

        gpB</span><span>.</span><span>SetValue</span><span>(</span><span>new</span><span> </span><span>IntegerParameterValue</span><span>(</span><span>TRUE</span><span>));</span><span>
        gpT</span><span>.</span><span>SetValue</span><span>(</span><span>new</span><span> </span><span>StringParameterValue</span><span>(</span><span>"TypeA"</span><span>));</span><span>
        gpF</span><span>.</span><span>SetValue</span><span>(</span><span>new</span><span> </span><span>StringParameterValue</span><span>(</span><span>"TypeB"</span><span>));</span><span>

        </span><span>// Set the formula to GPX so that its final value is either the value of GPT (TypeA)</span><span>
        </span><span>// or GPF (TypeB) depending on whether the value of GPB is True or False.</span><span>
        </span><span>// Note: in this particular case we are certain the formula is valid, but if weren't </span><span>
        </span><span>// certain, we could use a validation method as we are now going to illustrate here:</span><span>
        </span><span>string</span><span> expression </span><span>=</span><span> </span><span>"if(GPB,GPT,GPF)"</span><span>;</span><span> </span><span>// XPX &lt;== if (GPB == TRUE) then GPT else GPF</span><span>
        </span><span>if</span><span> </span><span>(</span><span>gpX</span><span>.</span><span>IsValidFormula</span><span>(</span><span>expression</span><span>))</span><span>
        </span><span>{</span><span>
            gpX</span><span>.</span><span>SetFormula</span><span>(</span><span>expression</span><span>);</span><span>  
        </span><span>}</span><span>

        trans</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>

    </span><span>// we can test that the formula works</span><span>
    </span><span>// since the boolean value is TRUE, the value of the GPX parameter</span><span>
    </span><span>// should be the same as the value of the GPT parameters</span><span>

    </span><span>StringParameterValue</span><span> sTrue </span><span>=</span><span> gpT</span><span>.</span><span>GetValue</span><span>()</span><span> </span><span>as</span><span> </span><span>StringParameterValue</span><span>;</span><span>
    </span><span>StringParameterValue</span><span> sFalse </span><span>=</span><span> gpF</span><span>.</span><span>GetValue</span><span>()</span><span> </span><span>as</span><span> </span><span>StringParameterValue</span><span>;</span><span>
    </span><span>StringParameterValue</span><span> sValue </span><span>=</span><span> gpX</span><span>.</span><span>GetValue</span><span>()</span><span> </span><span>as</span><span> </span><span>StringParameterValue</span><span>;</span><span>

    </span><span>if</span><span> </span><span>(</span><span>sValue</span><span>.</span><span>Value</span><span> </span><span>!=</span><span> sTrue</span><span>.</span><span>Value</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Error"</span><span>,</span><span> </span><span>"Unexpected value of a global parameter"</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>// we can also test that evaluation of the formula is affected by changes</span><span>

    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> trans </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>document</span><span>,</span><span> </span><span>"Change value of a YesNo parameter"</span><span>))</span><span>
    </span><span>{</span><span>
        trans</span><span>.</span><span>Start</span><span>();</span><span>
        gpB</span><span>.</span><span>SetValue</span><span>(</span><span>new</span><span> </span><span>IntegerParameterValue</span><span>(</span><span>FALSE</span><span>));</span><span>
        trans</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>

    sValue </span><span>=</span><span> gpX</span><span>.</span><span>GetValue</span><span>()</span><span> </span><span>as</span><span> </span><span>StringParameterValue</span><span>;</span><span>

    </span><span>if</span><span> </span><span>(</span><span>sValue</span><span>.</span><span>Value</span><span> </span><span>!=</span><span> sFalse</span><span>.</span><span>Value</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Error"</span><span>,</span><span> </span><span>"Unexpected value of a global parameter"</span><span>);</span><span>
    </span><span>}</span><span>

</span><span>}</span></code></pre></td></tr></tbody></table>
