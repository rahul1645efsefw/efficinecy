import streamlit as st
st.title("2305A21L63-PS10")
st.write('Calculate the efficiency of DC series generator at various loads.')
def Gen_Eff(V, CL, IL, K, Rse, Ra):
    CUL = (IL ** 2) * (Rse + Ra)
    Pout = V * IL * K
    Pin = Pout + CUL + CL
    Eff = (Pout / Pin) * 100
    return Eff, CUL

#st.title('Calculate the efficiency of DC series generator at various loads.')
col1,col2=st.columns(2)
with col1:
    with st.container(border=True):
        V = st.number_input('Voltage (V):volts', min_value=100)
        CL = st.number_input('Core Losses (CL) in watts', min_value=100)
        IL = st.number_input('Full Load Current (IL): Amps', min_value=10)
        K = st.number_input('Loading on Generator (K)', min_value=1)
        Rse = st.number_input('Series Field Resistance (Rse):ohms', min_value=10)
        Ra = st.number_input('Armature Resistance (Ra)in ohms', min_value=10)
        a=st.button("Compute")
   
    

with col2:
    if a:
        Eff, CUL = Gen_Eff(V, CL, IL, K, Rse, Ra)
        st.write(f'Efficiency: {Eff:.2f}%')
        st.write(f'Copper Losses: {CUL:.2f} watts')

