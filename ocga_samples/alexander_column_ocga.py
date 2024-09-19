#automatically generated ocga-py 
def checkRulesMy(ctx):
    if ctx.getTag("building") != "":
        ctx.align_scope("geometry")
        ctx.tag("height", "47.5")
        ctx.outer_rectangle("mass_model")

    if ctx.getTag("building:part") == "mass_model":
        ctx.scale("6.3", "6.3")
        ctx.colour("salmon")
        ctx.material("stone")
        ctx.roof_colour("salmon")
        ctx.roof_material("stone")
        ctx.split_z((('~6.7', 'angel_and_cross'), ('~3.8', 'column_top'), ('~1.20', 'platform'), ('~26.6', 'column'), ('~6.8', 'metal_base'), ('~2.0', 'stylobate'), ('1.5', 'steps')))

    if ctx.getTag("building:part") == "angel_and_cross":
        ctx.colour("darkslategrey")
        ctx.material("metal")
        ctx.roof_colour("darkslategrey")
        ctx.roof_material("metal")
        ctx.split_z((('~1', 'cross_stem'), ('0.3', 'cross_bar'), ('~4', 'cross_stem')))

    if ctx.getTag("building:part") == "cross_stem":
        ctx.scale("0.3", "0.3")

    if ctx.getTag("building:part") == "cross_bar":
        ctx.scale("2.5", "0.3")

    if ctx.getTag("building:part") == "column_top":
        ctx.colour("darkslategrey")
        ctx.material("metal")
        ctx.roof_colour("darkslategrey")
        ctx.roof_material("metal")
        ctx.primitive_cylinder("1.5", "16")
        ctx.split_z((('~1', 'column_dome'), ('0.25', 'column_top_cornice'), ('~1', 'column_top_column')))

    if ctx.getTag("building:part") == "column_dome":
        ctx.create_roof("dome", "'0.95")

    if ctx.getTag("building:part") == "column_top_cornice":
        ctx.scale("'1.2", "'1.2")

    if ctx.getTag("building:part") == "column_top_column":
        ctx.nope()

    if ctx.getTag("building:part") == "platform":
        ctx.colour("darkslategrey")
        ctx.material("metal")
        ctx.roof_colour("darkslategrey")
        ctx.roof_material("metal")
        ctx.scale("'0.8", "'0.8")

    if ctx.getTag("building:part") == "column":
        ctx.primitive_cylinder("1.7", "16")

    if ctx.getTag("building:part") == "metal_base":
        ctx.colour("darkslategrey")
        ctx.material("metal")
        ctx.roof_colour("darkslategrey")
        ctx.roof_material("metal")
        ctx.split_z((('0.3', 'column_base'), ('~1', 'base5'), ('~1', 'base4'), ('~0.5', 'base3'), ('~3.5', 'base2_with_bas_relief'), ('~2', 'base1')))

    if ctx.getTag("building:part") == "column_base":
        ctx.primitive_cylinder("'1", "16")
        ctx.scale("'0.8", "'0.8")
        ctx.comp_border("0.8", "column_base_part")

    if ctx.getTag("building:part") == "column_base_part":
        ctx.create_roof("round", "'0.5")
        ctx.scale("'1", "'1", "'2")

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
        ctx.split_z((('~1', 'step1'), ('~1', 'step2'), ('~1', 'step3')))

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
        ctx.create_roof("pyramidal", "0.25")

