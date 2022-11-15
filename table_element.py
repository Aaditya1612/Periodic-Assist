import mendeleev
import tabulate
import wikipedia
def represent(e_name):
    mainlist=[]
    sublist1=["At. Number:",str(mendeleev.element(e_name).atomic_number)]
    mainlist.append(sublist1)
    sublist1=["At. Weight:",str(mendeleev.element(e_name).atomic_weight)]
    mainlist.append(sublist1)
    sublist1=["Boiling Point:",str(mendeleev.element(e_name).boiling_point)]
    mainlist.append(sublist1)
    sublist1=["Melting Point:",str(mendeleev.element(e_name).melting_point)]
    mainlist.append(sublist1)
    sublist1=["Block:",str(mendeleev.element(e_name).block)]
    mainlist.append(sublist1)
    sublist1=["Group:",str(mendeleev.element(e_name).group_id)]
    mainlist.append(sublist1)
    sublist1=["Period:",str(mendeleev.element(e_name).period)]
    mainlist.append(sublist1)
    sublist1=["Electronic confi.:",str(mendeleev.element(e_name).econf)]
    mainlist.append(sublist1)
    sublist1=["E.N Value:",str(mendeleev.element(e_name).en_pauling)]
    mainlist.append(sublist1)
    sublist1=["Density:",str(mendeleev.element(e_name).density)]
    mainlist.append(sublist1)
    sublist1=["At. radius:",str(mendeleev.element(e_name).atomic_radius)]
    mainlist.append(sublist1)
    sublist1=["At. volume:",str(mendeleev.element(e_name).atomic_volume)]
    mainlist.append(sublist1)
    sublist1=["Abundance crust:",str(mendeleev.element(e_name).abundance_crust)]
    mainlist.append(sublist1)
    sublist1=["Abundance Sea:",str(mendeleev.element(e_name).abundance_sea)]
    mainlist.append(sublist1)
    sublist1=["Is radioactive:",str(mendeleev.element(e_name).is_radioactive)]
    mainlist.append(sublist1)
    sublist1=["Thermal conductivity:",str(mendeleev.element(e_name).thermal_conductivity)]
    mainlist.append(sublist1)
    sublist1=["Evaporation heat:",str(mendeleev.element(e_name).evaporation_heat)]
    mainlist.append(sublist1)
    sublist1=["Fusion heat:",str(mendeleev.element(e_name).fusion_heat)]
    mainlist.append(sublist1)
    sublist1=["Discovered at:",str(mendeleev.element(e_name).discovery_location)]
    mainlist.append(sublist1)
    sublist1=["Discoverers:",str(mendeleev.element(e_name).discoverers)]
    mainlist.append(sublist1)
    return mainlist
