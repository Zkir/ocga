#automatically generated ocga-py 
def checkRulesMy(ctx):
    if ctx.getTag("building") != "":
        ctx.alignScopeToGeometry()
        ctx.outerRectangle("mass_model")

    if ctx.getTag("building:part") == "mass_model":
        ctx.scale("6.3", "6.3")
        ctx.split_z((('1.5', 'steps'), ('~2.0', 'stylobate'), ('~6.8', 'metal_base'), ('0.3', 'column_base'), ('~26.6', 'column'), ('~1.25', 'platform'), ('~3.8', 'column_top'), ('~6.7', 'angel_and_cross')))

    if ctx.getTag("building:part") == "angel_and_cross":
        ctx.split_z((('~4', 'cross_stem'), ('0.3', 'cross_bar'), ('~1', 'cross_stem')))

    if ctx.getTag("building:part") == "cross_stem":
        ctx.scale("0.3", "0.3")

    if ctx.getTag("building:part") == "cross_bar":
        ctx.scale("0.3", "2.5")

    if ctx.getTag("building:part") == "column_top":
        ctx.primitiveCylinder("16", "1.7")
        ctx.roof("dome", "1.5")

    if ctx.getTag("building:part") == "platform":
        ctx.scale("'0.8", "'0.8")

    if ctx.getTag("building:part") == "column":
        ctx.primitiveCylinder("16", "1.7")

    if ctx.getTag("building:part") == "column_base":
        ctx.primitiveCylinder()
        ctx.scale("'0.8", "'0.8")
        ctx.comp_border("0.8", "column_base_part")

    if ctx.getTag("building:part") == "column_base_part":
        ctx.roof("round", "'0.5")
        ctx.scale("'1", "'1", "'2")

    if ctx.getTag("building:part") == "metal_base":
        ctx.split_z((('~2', 'base1'), ('~3.5', 'base2_with_bas_relief'), ('~0.5', 'base3'), ('~1', 'base4'), ('~1', 'base5')))

    if ctx.getTag("building:part") == "base1":
        ctx.scale("'0.95", "'0.95")

    if ctx.getTag("building:part") == "base2_with_bas_relief":
        ctx.scale("'0.8", "'0.8")

    if ctx.getTag("building:part") == "base3":
        ctx.nope()

    if ctx.getTag("building:part") == "base4":
        ctx.scale("'0.9", "'0.9")

    if ctx.getTag("building:part") == "base5":
        ctx.scale("'0.8", "'0.8")

    if ctx.getTag("building:part") == "stylobate":
        ctx.nope()

    if ctx.getTag("building:part") == "steps":
        ctx.split_z((('~1', 'step3'), ('~1', 'step2'), ('~1', 'step1')))

    if ctx.getTag("building:part") == "step1":
        ctx.scale("8.1", "8.1")

    if ctx.getTag("building:part") == "step2":
        ctx.scale("9.1", "9.1")

    if ctx.getTag("building:part") == "step3":
        ctx.scale("10.1", "10.1")
        ctx.comp_border("1", "obelisk")
        ctx.restore()

    if ctx.getTag("building:part") == "obelisk":
        ctx.scale("1", "1", "1.25")
        ctx.translate("4.55", "0", "0.5")
        ctx.roof("pyramidal", "0.25")

